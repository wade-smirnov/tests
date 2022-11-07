from helpers.constructors import Code_constructor
from pytest_bdd import scenarios, parsers, when, then
from lib.interfaces import EXTRA_TYPES
import subprocess
import time
import config

scenarios('../features/material_render.feature')

@when(parsers.cfparse("material with {color:String} {metal:String} and {specular:String} intensity is applied to {mesh:String}",EXTRA_TYPES))
def set_material(color, metal, specular, mesh):
    f = open('./scripts/blender_script_material.py', "w")

    script_code = Code_constructor.import_required_packages() + Code_constructor.delete_object() + Code_constructor.create_object(mesh) + Code_constructor.create_material() + Code_constructor.adjust_material(color, metal, specular)

    f.write(script_code)
    f.close()

@then("scene can be rendered")
def render_scene():
    
    subprocess.run([config.blender_path,  "--log", "'*'", "--log-file", config.log_output_folder+rf"{time.time()}.txt","-P", r"./scripts/blender_script_material.py", "-o", config.render_output_folder+fr"material_{time.time()}", "--render-frame","1","kostil_exit_error_generator"], shell=True)