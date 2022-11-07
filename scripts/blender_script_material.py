import bpy

bpy.ops.object.delete(use_global=False)

bpy.ops.mesh.primitive_circle_add(radius=1, enter_editmode=False, align='WORLD',location=(0,0,0), scale=(1,1,1))
bpy.ops.object.editmode_toggle()
bpy.ops.mesh.edge_face_add()
object = bpy.context.object
material = bpy.data.materials.new('Test')
object.data.materials.append(material)
bpy.context.object.active_material.diffuse_color = (0.23514,0.59146,0.62389, 1)
bpy.context.object.active_material.metallic = 0.91329
bpy.context.object.active_material.specular_intensity = 0.91072
bpy.ops.wm.quit_blender()