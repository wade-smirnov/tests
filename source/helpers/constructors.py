from helpers.generators import Generator

class Code_constructor:
    @staticmethod
    def import_required_packages():
        return 'import bpy\n\n'

    @staticmethod
    def create_object(mesh, size='default'):
        match mesh:
            case 'circle':
                return f"bpy.ops.mesh.primitive_circle_add(radius=1, enter_editmode=False, align='WORLD',location={Generator.location()}, scale={Generator.scale(size=size)})\nbpy.ops.object.editmode_toggle()\nbpy.ops.mesh.edge_face_add()\n"

            case 'uv_sphere':
                return f"bpy.ops.mesh.primitive_uv_sphere_add(radius=1, enter_editmode=False, align='WORLD',location={Generator.location()}, scale={Generator.scale(size=size)})\n"

            case 'torus':
                return f"bpy.ops.mesh.primitive_torus_add(align='WORLD', location={Generator.location()}, rotation={Generator.rotation()}, major_radius=1, minor_radius=0.25, abso_major_rad=1.25, abso_minor_rad=0.75)\n"

            case _:
                return f"bpy.ops.mesh.primitive_cube_add(enter_editmode=False, align='WORLD', location={Generator.location()}, scale={Generator.scale(size=size)})\n"

    @staticmethod
    def delete_object():
        return 'bpy.ops.object.delete(use_global=False)\n\n'

    @staticmethod
    def resolution_setup(resolution):
        x_res = resolution.split('x')[0]
        y_res = resolution.split('x')[1]
        return f'bpy.context.scene.render.resolution_x = {x_res}\nbpy.context.scene.render.resolution_y = {y_res}\n\n'

    @staticmethod
    def close_blender():
        return 'bpy.ops.wm.quit_blender()'
    





            
