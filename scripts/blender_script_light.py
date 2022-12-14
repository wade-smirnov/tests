import bpy

bpy.ops.object.delete(use_global=False)

bpy.ops.mesh.primitive_torus_add(align='WORLD', location=(0,0,0), rotation=(0,0,0), major_radius=1, minor_radius=0.25, abso_major_rad=1.25, abso_minor_rad=0.75)
object = bpy.context.object
material = bpy.data.materials.new('Test')
object.data.materials.append(material)
bpy.context.object.active_material.diffuse_color = (0.96042,0.72257,0.55249, 1)
bpy.context.object.active_material.metallic = 0.5345
bpy.context.object.active_material.specular_intensity = 0.52688

bpy.ops.object.select_all(action='DESELECT')
bpy.data.objects['Light'].select_set(True)
bpy.ops.object.delete(use_global=False)

bpy.ops.object.light_add(type='AREA', align='WORLD', location=(0, -0, 8.66276), scale=(1, 1, 1))
