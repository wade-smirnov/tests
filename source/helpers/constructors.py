from helpers.generators import Generator
import random

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

    @staticmethod
    def create_material():
        return "object = bpy.context.object\nmaterial = bpy.data.materials.new('Test')\nobject.data.materials.append(material)\n"

    @staticmethod
    def set_color(color='random'):
        match color:
            case 'green':
                return "bpy.context.object.active_material.diffuse_color = (0, 1, 0, 1)\n"
            case _:
                return f"bpy.context.object.active_material.diffuse_color = {Generator.random_color()}\n"

    @staticmethod
    def set_metal(metal='normal'):
        match metal:
            case 'high':
                return f"bpy.context.object.active_material.metallic = {round(random.uniform(0.9, 1),5)}\n"
            case 'low':
                return f"bpy.context.object.active_material.metallic = {round(random.uniform(0, 0.5),5)}\n"
            case _:
                return f"bpy.context.object.active_material.metallic = {round(random.uniform(0.45, 0.55),5)}\n"
    
    @staticmethod
    def set_specular(specular='normal'):
        match specular:
            case 'high':
                return f"bpy.context.object.active_material.specular_intensity = {round(random.uniform(0.8, 1),5)}\n"
            case 'low':
                return f"bpy.context.object.active_material.specular_intensity = {round(random.uniform(0, 0.5),5)}\n"
            case _:
                return f"bpy.context.object.active_material.specular_intensity = {round(random.uniform(0.45, 0.55),5)}\n\n"
    
    @staticmethod
    def adjust_material(color, metal, specular):
        return Code_constructor.set_color(color) + Code_constructor.set_metal(metal) + Code_constructor.set_specular(specular)

    @staticmethod
    def delete_light():
        return "bpy.ops.object.select_all(action='DESELECT')\nbpy.data.objects['Light'].select_set(True)\nbpy.ops.object.delete(use_global=False)\n\n"

    @staticmethod
    def set_light(light):
        match light:
            case 'sun':
                return f"bpy.ops.object.light_add(type='SUN', radius=1, align='WORLD', location={Generator.random_location()}, scale=(1, 1, 1))\n"
            case 'spot':
                return f"bpy.ops.object.light_add(type='SPOT', align='WORLD', location=(0, -0, {round(random.uniform(5, 30),5)}), scale=(1, 1, 1))\n"
            case 'area':
                return f"bpy.ops.object.light_add(type='AREA', align='WORLD', location=(0, -0, {round(random.uniform(5, 30),5)}), scale=(1, 1, 1))\n"
            case _:
                return f"bpy.ops.object.light_add(type='POINT', radius=1, align='WORLD', location={Generator.random_location()}, scale=(1, 1, 1))\n"




            
