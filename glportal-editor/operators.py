import bpy

from .operatorHelpers import resetTriggerSettings, itemsMaterial, itemsModel, simpleCube
from .managers import ModelManager


# we are using this for <end> (exit door)
class AddDoor(bpy.types.Operator):
  bl_idname = "glp.add_door"
  bl_label = "Add a door"
  bl_description = "Add an exit door (use only once)"
  bl_options = {'UNDO'}

  def execute(self, context):
    if ModelManager.create("Door.obj", "door/door"):
      object = bpy.context.selected_objects[0]

      if object:
        object.glpTypes = "door"

    return {'FINISHED'}


class SetPortalable(bpy.types.Operator):
  bl_idname = "glp.set_portalable"
  bl_label = "Portalable"
  bl_description = "Mark the selection as portalable wall."
  bl_options = {'UNDO'}

  def execute(self, context):
    objects = bpy.context.selected_objects
    for object in objects:
      if object.type == 'MESH':
        if object.glpTypes != "door":
          if object.glpTypes != "model":
            resetTriggerSettings(object)
            object.glpTypes = "wall"

          object.glpMaterial = "concrete/wall00"
        else:
          self.report({'ERROR'}, "Door can't be converted to the portalable wall.")
      else:
        self.report(
          {'ERROR'},
          "Object of type '%s' can't be converted to the portalable wall." % (object.type)
        )
    return {'FINISHED'}


class SetWall(bpy.types.Operator):
  bl_idname = "glp.set_wall"
  bl_label = "Metal tiles"
  bl_description = "Mark the selection as metal wall."
  bl_options = {'UNDO'}

  def execute(self, context):
    objects = bpy.context.selected_objects
    for object in objects:
      if object.type == 'MESH':
        if object.glpTypes != "door":
          if object.glpTypes != "model":
            resetTriggerSettings(object)
            object.glpTypes = "wall"

          object.glpMaterial = "metal/tiles00x3"
        else:
          self.report({'ERROR'}, "Door can't be converted to the metal wall.")
      else:
        self.report(
          {'ERROR'},
          "Object of type '%s' can't be converted to the metal wall." % (object.type)
        )
    return {'FINISHED'}


class AddWall(bpy.types.Operator):
  bl_idname = "glp.add_wall"
  bl_label = "Metal tiles"
  bl_description = "Add a metal wall."
  bl_options = {'UNDO'}

  def execute(self, context):
    if simpleCube():
      bpy.ops.glp.set_wall()
    return {'FINISHED'}


class AddPortalable(bpy.types.Operator):
  bl_idname = "glp.add_portalable"
  bl_label = "Portalable"
  bl_description = "Add a portalable wall."
  bl_options = {'UNDO'}

  def execute(self, context):
    if simpleCube():
      bpy.ops.glp.set_portalable()
    return {'FINISHED'}


class SearchMaterial(bpy.types.Operator):
  bl_idname = "glp.search_material"
  bl_label = "Set material"
  bl_property = "material"

  material = bpy.props.EnumProperty(items=itemsMaterial)

  def execute(self, context):
    objects = bpy.context.selected_objects
    for object in objects:
      if object.type == 'MESH' and object.glpTypes:
        object.glpMaterial = self.material
    return {'FINISHED'}

  def invoke(self, context, event):
    wm = context.window_manager
    wm.invoke_search_popup(self)
    return {'FINISHED'}


class SearchModel(bpy.types.Operator):
  bl_idname = "glp.search_model"
  bl_label = "Add model"
  bl_property = "model"

  model = bpy.props.EnumProperty(items=itemsModel)

  def execute(self, context):
    if self.model != "none":
      ModelManager.create(self.model)
    return {'FINISHED'}

  def invoke(self, context, event):
    wm = context.window_manager
    wm.invoke_search_popup(self)
    return {'FINISHED'}
