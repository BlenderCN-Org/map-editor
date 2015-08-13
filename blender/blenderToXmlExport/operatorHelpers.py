import bpy
import os
import bmesh

def fixDoorTexture(me):
    bpy.ops.object.mode_set(mode='EDIT')
    bm = bmesh.from_edit_mesh(me)
    bm.faces.ensure_lookup_table()
    uv_layer = bm.loops.layers.uv[0]
    
    nFaces = len(bm.faces)
    bm.faces[7].loops[0][uv_layer].uv = (0.5, 0.5)
    bm.faces[7].loops[1][uv_layer].uv = (0.5, 0)
    bm.faces[7].loops[2][uv_layer].uv = (0.5, 0)
    
    bm.faces[25].loops[0][uv_layer].uv = (0.5, 0.5)
    bm.faces[25].loops[1][uv_layer].uv = (0.5, 0)
    bm.faces[25].loops[2][uv_layer].uv = (0.5, 0)
    
    bmesh.update_edit_mesh(me)
    bpy.ops.object.mode_set(mode='OBJECT')

def clearGlpProperties():
    object = bpy.context.active_object
    if object:
        object.glpTypes = "none"
        object.glpVolumeTypes = "none"
        object.glpTriggerTypes = "none"
        object.glpWallTypes = "none"

def getMaterial(texturePath, diffuse, dimensions = [1,1,1]):
    realpath = os.path.expanduser(texturePath)
    try:
        WallImage = bpy.data.images.load(realpath)
    except:
        raise NameError("Cannot load image %s" % realpath)
    
    WallTexture = bpy.data.textures.new(name = 'ColorTex', type = 'IMAGE')
    WallTexture.image = WallImage
    
    mat = bpy.data.materials.new('TexMat')
    mat.diffuse_color = diffuse
    
    # Add texture slot for color texture
    mtex = mat.texture_slots.add()
    mtex.texture = WallTexture
    mtex.texture_coords = 'GLOBAL'
    mtex.use_map_color_diffuse = True
    mtex.use_map_color_emission = True
    mtex.emission_color_factor = 0.5
    mtex.use_map_density = True
    mtex.mapping = 'CUBE'
    mtex.use_map_emit = True
    mtex.emit_factor = 0.3
#    mtex.offset = [0, -0.25, 0]
    
    return mat
