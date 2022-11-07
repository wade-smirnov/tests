import bpy

bpy.ops.object.delete(use_global=False)

bpy.ops.mesh.primitive_uv_sphere_add(radius=1, enter_editmode=False, align='WORLD',location=(0,0,0), scale=(1,1,1))
object = bpy.context.object
material = bpy.data.materials.new('Test')
object.data.materials.append(material)
bpy.context.object.active_material.diffuse_color = (0.37215,0.35971,0.64635, 1)
bpy.context.object.active_material.metallic = 0.25094
bpy.context.object.active_material.specular_intensity = 0.89478
