import bpy
from bpy.props import *
from bpy_extras.io_utils import ExportHelper
import os
import xml.etree.cElementTree as tree
import xml.dom.minidom as minidom
import mathutils
import math
import string
from mathutils import Vector
import re

# decimal points for rounding
d_p = 5

def storePosition(element, object):
    element.set("x", str(round(object.location[0], d_p)))
    element.set("y", str(round(object.location[2], d_p)))
    element.set("z", str(-round(object.location[1], d_p)))

# prepare rotation before exporting
def prepareRot(degree):
    return str(round(degree % 360, d_p))

def checkRotation(object):
    x = math.degrees(object.rotation_euler[0])
    y = math.degrees(object.rotation_euler[2])
    z = math.degrees(-object.rotation_euler[1])

    if prepareRot(x) == "0.0" and prepareRot(y) == "0.0" and prepareRot(z) == "0.0":
        return False
    else:
        return True

def storeRotation(element, object):
    element.set("x", prepareRot(math.degrees(object.rotation_euler[0])))
    element.set("y", prepareRot(math.degrees(object.rotation_euler[2])))
    element.set("z", prepareRot(math.degrees(-object.rotation_euler[1])))

def storeScale(element, object):
    element.set("x", str(round(object.dimensions[0], d_p)))
    element.set("y", str(round(object.dimensions[2], d_p)))
    element.set("z", str(round(object.dimensions[1], d_p)))

def writeLampToTree(object, targetTree):
    lamp = object.data

    colorArray = lamp.color
    lightDistance = lamp.distance
    lightEnergy = lamp.energy

    lightElement = tree.SubElement(targetTree, "light")
    storePosition(lightElement, object);

    lightElement.set("r", str(round(colorArray[0], d_p)))
    lightElement.set("g", str(round(colorArray[1], d_p)))
    lightElement.set("b", str(round(colorArray[2], d_p)))

    lightElement.set("distance", str(round(lightDistance, d_p)))
    lightElement.set("energy", str(round(lightEnergy, d_p)))

    if lamp.use_specular:
        lightElement.set("specular", "1")

class Exporter():
    filepath = ""

    def execute(self, context):
        dir = os.path.dirname(self.filepath)
        objects = context.scene.objects
        root = tree.Element("map")

        # Materials
        materialElement = tree.SubElement(root, "materials")
        material1 = tree.SubElement(materialElement, "mat")
        material2 = tree.SubElement(materialElement, "mat")

        material1.set("mid", "1")
        material1.set("name", "concrete/wall00")
        material2.set("mid", "2")
        material2.set("name", "metal/tiles00x3")

        # Exporting
        for object in objects:
            object.select = False
        for object in objects:
            if object.glpTypes:
                type = object.glpTypes
            else:
                type = "None"

            if object.type == "LAMP":
                writeLampToTree(object, root)
            elif object.type == "CAMERA":
                boxElement = tree.SubElement(root, "spawn")

                positionElement = tree.SubElement(boxElement, "position")
                storePosition(positionElement, object);

                rotationElement = tree.SubElement(boxElement, "rotation")
                rotationElement.set("x", prepareRot(math.degrees(object.rotation_euler[0]) - 90))
                rotationElement.set("y", prepareRot(math.degrees(object.rotation_euler[2])))
                rotationElement.set("z", "0")
            elif object.type == "MESH" and type == "door":
                # tempotary add <end> instead of <door>
                boxElement = tree.SubElement(root, "end")

                positionElement = tree.SubElement(boxElement, "position")
                storePosition(positionElement, object);

                rotationElement = tree.SubElement(boxElement, "rotation")
                rotationElement.set("x", prepareRot(math.degrees(object.rotation_euler[0]) - 90))
                rotationElement.set("y", prepareRot(math.degrees(object.rotation_euler[2])))
                rotationElement.set("z", prepareRot(math.degrees(-object.rotation_euler[1])))
            elif object.type == "MESH":
                boxElement = None

                if type == "trigger":
                    boxElement = tree.SubElement(root, "trigger")
                    if object.glpTriggerTypes:
                        boxElement.set("type", object.glpTriggerTypes)
                elif type == "wall":
                    boxElement = tree.SubElement(root, "wall")
                    if object.glpWallTypes == "portalable":
                        boxElement.set("mid", "1")
                    else:
                        boxElement.set("mid", "2")
                elif type == "volume":
                    if object.glpVolumeTypes == "acid":
                        boxElement = tree.SubElement(root, "acid")
                # disabled, will be enabled in the future
#                else:
#                    boxElement = tree.SubElement(root, "door")
                if boxElement != None:
                    object.select = True

                    positionElement = tree.SubElement(boxElement, "position")
                    storePosition(positionElement, object);

                    if checkRotation(object):
                        rotationElement = tree.SubElement(boxElement, "rotation")
                        storeRotation(rotationElement, object);

                    scaleElement = tree.SubElement(boxElement, "scale")
                    storeScale(scaleElement, object);

                    object.select = False

        xml = minidom.parseString(tree.tostring(root))

        file = open(self.filepath, "w")
        fix = re.compile(r'((?<=>)(\n[\t]*)(?=[^<\t]))|(?<=[^>\t])(\n[\t]*)(?=<)')
        fixed_output = re.sub(fix, '', xml.toprettyxml())
        file.write(fixed_output)
        file.close()

        return {'FINISHED'}

    def setFilepath(target):
        self.filepath = target

class ExportGlPortalFormat(bpy.types.Operator, ExportHelper):
    bl_idname = "export_glportal_xml.xml"
    bl_label = "Export GlPortal XML"
    bl_description = "Export to GlPortal XML file (.xml)"
    bl_options = {'PRESET'}
    filename_ext = ".xml"
    filter_glob = StringProperty(default="*.xml", options={'HIDDEN'})

    def execute(self, context):
        Exporter.filepath = self.filepath
        Exporter.execute(self, context)

        return {'FINISHED'}
