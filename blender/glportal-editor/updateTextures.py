import bpy
import bmesh
import time
import math
from bpy.app.handlers import persistent

class UpdateTexture:
    isRunning = False

    def updateTexture(object):
        addon_prefs = bpy.context.user_preferences.addons[__package__].preferences

        if addon_prefs.smartTexturesMapping:
            UpdateTexture.isRunning = True

            bpy.context.scene.objects.active = object
            bpy.ops.object.mode_set(mode='EDIT')
            me = object.data
            bm = bmesh.from_edit_mesh(me)
            scale = [0.0, 0.0, 0.0]

            scale[0] = abs(object.scale[0])
            scale[1] = abs(object.scale[1])
            scale[2] = abs(object.scale[2])

            bpy.ops.uv.cube_project()

            if hasattr(bm.faces, "ensure_lookup_table"):
                bm.faces.ensure_lookup_table()

            # the real game starting now :)
            uv_layer = bm.loops.layers.uv[0]
            # back
            bm.faces[0].loops[0][uv_layer].uv = (scale[1], 0)
            bm.faces[0].loops[1][uv_layer].uv = (0, 0)
            bm.faces[0].loops[2][uv_layer].uv = (0, -scale[2])
            bm.faces[0].loops[3][uv_layer].uv = (scale[1], -scale[2])
            # right
            bm.faces[1].loops[0][uv_layer].uv = (scale[0], 0)
            bm.faces[1].loops[1][uv_layer].uv = (0, 0)
            bm.faces[1].loops[2][uv_layer].uv = (0, -scale[2])
            bm.faces[1].loops[3][uv_layer].uv = (scale[0], -scale[2])
            # front
            bm.faces[2].loops[0][uv_layer].uv = (scale[1], 0)
            bm.faces[2].loops[1][uv_layer].uv = (0, 0)
            bm.faces[2].loops[2][uv_layer].uv = (0, -scale[2])
            bm.faces[2].loops[3][uv_layer].uv = (scale[1], -scale[2])
            # left
            bm.faces[3].loops[0][uv_layer].uv = (scale[0], 0)
            bm.faces[3].loops[1][uv_layer].uv = (0, 0)
            bm.faces[3].loops[2][uv_layer].uv = (0, -scale[2])
            bm.faces[3].loops[3][uv_layer].uv = (scale[0], -scale[2])
            # bottom
            bm.faces[4].loops[0][uv_layer].uv = (0, 0)
            bm.faces[4].loops[1][uv_layer].uv = (0, -scale[1])
            bm.faces[4].loops[2][uv_layer].uv = (scale[0], -scale[1])
            bm.faces[4].loops[3][uv_layer].uv = (scale[0], 0)
            # top
            bm.faces[5].loops[0][uv_layer].uv = (scale[0], -scale[1])
            bm.faces[5].loops[1][uv_layer].uv = (scale[0], 0)
            bm.faces[5].loops[2][uv_layer].uv = (0, 0)
            bm.faces[5].loops[3][uv_layer].uv = (0, -scale[1])

            bmesh.update_edit_mesh(me)
            bm.free()
            bpy.ops.object.mode_set(mode='OBJECT')

            UpdateTexture.isRunning = False

@persistent
def sceneUpdater(scene):
    addon_prefs = bpy.context.user_preferences.addons[__package__].preferences
    object = scene.objects.active

    if addon_prefs.smartTexturesMapping:
        if object is not None and object.is_updated:
            if (object.glpTypes == "wall" or object.glpTypes == "volume"):
                if not UpdateTexture.isRunning:
                    UpdateTexture.updateTexture(object)
