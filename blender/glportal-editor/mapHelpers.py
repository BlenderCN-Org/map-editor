import bpy
from bpy.props import *

def isOverObject(position, object):
    pMin = object.location[0] - abs(object.dimensions[0]) / 2
    pMax = object.location[0] + abs(object.dimensions[0]) / 2

    if position[0] > pMin and position[0] < pMax:
        pMin = object.location[1] - abs(object.dimensions[1]) / 2
        pMax = object.location[1] + abs(object.dimensions[1]) / 2

        if position[1] > pMin and position[1] < pMax:
            pMax = object.location[2] + abs(object.dimensions[2]) / 2

            if position[2] >= pMax + 1:
                return 1
            elif position[2] >= pMax:
                return 2

    return 0

def controlSpawnPosition(objects):
    # find spawn position
    for object in objects:
        if object.type == "CAMERA":
            cameraPosition = object.location
            break

    for object in objects:
        if object.type == "MESH" and object.glpTypes == "wall":
            isOver = isOverObject(cameraPosition, object)
            if isOver != 0:
                return isOver

    return 0

def countObjects(objects):
    result = {
        'camera':           0,
        'wallPortalable':   0,
        'wallMetal':        0,
        'acid':             0,
        'triggerDeath':     0,
        'light':            0,
        'exitDoor':         0
    }

    for object in objects:
        if object.glpTypes:
            type = object.glpTypes
        else:
            type = "None"

        if object.type == "LAMP":
            result['light'] += 1
        elif object.type == "CAMERA":
            result['camera'] += 1
        elif object.type == "MESH":
            if type == "door":
                result['exitDoor'] += 1
            elif type == "trigger":
                if object.glpTriggerTypes == "death":
                    result['triggerDeath'] += 1
            elif type == "wall":
                if object.glpWallTypes == "portalable":
                    result['wallPortalable'] += 1
                else:
                    result['wallMetal'] += 1
            elif type == "volume":
                if object.glpVolumeTypes == "acid":
                    result['acid'] += 1

    return result

class checkMapDialog(bpy.types.Operator):
    bl_idname = "object.map_check_dialog"
    bl_label = "Check map results"

    # define properties for popup dialog
    camera = bpy.props.IntProperty (name = "Number of cameras")
    light = bpy.props.IntProperty (name = "Number of lights")
    wallPortalable = bpy.props.IntProperty (name = "Number of portalable wall")
    wallMetal = bpy.props.IntProperty (name = "Number of metal wall")
    exitDoor = bpy.props.IntProperty (name = "Number of exit doors")

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, 400)

    def draw(self, context):
        objects = context.scene.objects
        result = countObjects(objects)
        layout = self.layout
        error = False

        if result['exitDoor'] != 1:
            self.exitDoor = result['exitDoor']
            error = True

            layout.prop(self, "exitDoor")
            layout.label(text = "There is no exit door use it exactly once.", icon = 'CANCEL')
            layout.separator()
        if result['camera'] != 1:
            self.camera = result['camera']
            error = True

            layout.prop(self, "camera")
            layout.label(text = "The camera object is used for determining the spawn position use it exactly once.",icon = 'ERROR')
            layout.separator()
        if result['light'] == 0:
            error = True

            layout.label(text = "There is no light in the map you need at least one light.", icon = 'CANCEL')
            layout.separator()
        elif result['light'] > 5:
            self.light = result['light']
            error = True

            layout.prop(self, "light")
            layout.label(text = "There are too many lights in the map.", icon = 'INFO')
            layout.label(text = "This is a performance issue and has to be fixed..", icon = 'INFO')
            layout.separator()
        if result['wallPortalable'] == 0:
            self.wallPortalable = result['wallPortalable']
            error = True

            layout.prop(self, "wallPortalable")
            layout.label(text = "There isn't a portalable wall.", icon = 'ERROR')
            layout.separator()
        if result['wallMetal'] == 0:
            self.wallMetal = result['wallMetal']
            error = True

            layout.prop(self, "wallMetal")
            layout.label(text = "There isn't a metal wall.", icon = 'INFO')
            layout.separator()
        if result['triggerDeath'] < result['acid']:
            error = True

            layout.label(text = "Acid without death trigger.", icon = 'INFO')
            layout.label(text = "Use death trigger for each volume of acid in the map.")
            layout.separator()
        if result['camera'] == 1:
            isOver = controlSpawnPosition(objects)

            if isOver == 0:
                error = True

                layout.label(text = "Camera is in the air.", icon = 'CANCEL')
                layout.label(text = "Remember, we are using camera as spawn position.", icon = 'INFO')
                layout.separator()
            elif isOver == 2:
                error = True

                layout.label(text = "Camera is very close to the floor.", icon = 'ERROR')
                layout.label(text = "Player can get stuck in the floor or unable to go through portal.", icon = 'ERROR')
                layout.label(text = "Remember, we are using camera as spawn position.", icon = 'INFO')
                layout.separator()

        if not error:
            layout.label(text = "Nice work. There are no errors or warnings in the map", icon = 'FILE_TICK')
