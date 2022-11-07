import bpy

bpy.ops.object.delete(use_global=False)

bpy.ops.mesh.primitive_circle_add(radius=1, enter_editmode=False, align='WORLD',location=(0,0,0), scale=(0.23835,0.40685,0.48455))
bpy.ops.object.editmode_toggle()
bpy.ops.mesh.edge_face_add()
