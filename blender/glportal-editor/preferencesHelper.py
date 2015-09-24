import bpy
from .updateTextures import *

def updateTriggerXrays(self, context):
    addon_prefs = context.user_preferences.addons[__package__].preferences
    triggerXrays = addon_prefs.triggerXrays
    objects = context.scene.objects

    for object in objects:
        if object.glpTypes and object.glpTypes == "trigger":
            object.show_x_ray = addon_prefs.triggerXrays

def updateSmartTexturesMapping(self, context):
    addon_prefs = context.user_preferences.addons[__package__].preferences
    SmartTextures = addon_prefs.smartTexturesMapping
    objects = context.scene.objects

    for object in objects:
        if object.glpTypes and (object.glpTypes == "wall" or object.glpTypes == "volume"):
            me = object.data

            if SmartTextures:
                me.materials[0].texture_slots[0].texture_coords = 'UV'
                me.materials[0].texture_slots[0].mapping = 'FLAT'

                UpdateTexture.updateTexture(object)
            else:
                me.materials[0].texture_slots[0].texture_coords = 'GLOBAL'
                me.materials[0].texture_slots[0].mapping = 'CUBE'
