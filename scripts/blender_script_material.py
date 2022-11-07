import bpy

bpy.ops.object.delete(use_global=False)

bpy.ops.mesh.primitive_uv_sphere_add(radius=1, enter_editmode=False, align='WORLD',location=(0,0,0), scale=(1,1,1))
object = bpy.context.object
material = bpy.data.materials.new('Test')
object.data.materials.append(material)
bpy.context.object.active_material.diffuse_color = (0.81785,0.19107,0.46983, 1)
bpy.context.object.active_material.metallic = 0.13478
bpy.context.object.active_material.specular_intensity = 0.83391
bpy.ops.wm.quit_blender()