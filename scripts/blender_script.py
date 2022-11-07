import bpy

bpy.ops.object.delete(use_global=False)

bpy.ops.mesh.primitive_circle_add(radius=1, enter_editmode=False, align='WORLD',location=(0,0,0), scale=(47.58728,47.14827,40.49577))
bpy.ops.object.editmode_toggle()
bpy.ops.mesh.edge_face_add()
bpy.context.scene.render.resolution_x = 1000
bpy.context.scene.render.resolution_y = 10000

bpy.ops.wm.quit_blender()