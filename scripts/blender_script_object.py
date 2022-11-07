import bpy

bpy.ops.object.delete(use_global=False)

bpy.ops.mesh.primitive_circle_add(radius=1, enter_editmode=False, align='WORLD',location=(0,0,0), scale=(0.25469,0.31451,0.24678))
bpy.ops.object.editmode_toggle()
bpy.ops.mesh.edge_face_add()
bpy.context.scene.render.resolution_x = 640
bpy.context.scene.render.resolution_y = 480

bpy.ops.wm.quit_blender()