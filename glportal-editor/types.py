import bpy
from bpy.props import EnumProperty, StringProperty

glpTypes = [
  ("none",    "None",    "No special property"),
  ("wall",    "Wall",    "Wall"),
  ("door",    "Door",    "Door"),# REMOVE this
  ("volume",  "Volume",  "Volume"),
  ("trigger", "Trigger", "Trigger"),
  ("model",   "Model",   "Model")
]
glpVolumeTypes = [
  ("none", "None",      "No special property"),
  ("acid", "Acid Pool", "A pool full of acid, hurts..")
]
glpTriggerTypes = [
  ("none",      "None",      "No special property"),
  ("win",       "Win",       "Area triggers win"),
  ("death",     "Death",     "Area triggers death"),
  ("radiation", "Radiation", "Area triggers radiation")
]
glpMaterialTypes = [
  ("none", "None", "No material")
]


def setProperties():
  bpy.types.Object.glpTypes = EnumProperty (
    items = glpTypes,
    name = "Type",
    default = "none"
  )
  bpy.types.Object.glpVolumeTypes = EnumProperty (
    items = glpVolumeTypes,
    name = "Volume Type",
    default = "none"
  )
  bpy.types.Object.glpTriggerTypes = EnumProperty (
    items = glpTriggerTypes,
    name = "Trigger Type",
    default = "none"
  )
  bpy.types.Object.glpModel = StringProperty (
    name = "Model",
    default = "none"
  )
  bpy.types.WindowManager.importedFilepath = StringProperty (
    name = "Imported filepath",
    default = "none"
  )

setProperties()
