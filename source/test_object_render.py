from helpers.constructors import Code_constructor
from pytest_bdd import scenarios, parsers, when, then
from lib.interfaces import EXTRA_TYPES
import subprocess
import time
import config

scenarios('../features/object_render.feature')


 
@when(parsers.cfparse('{size:String} {mesh:String} is added to the scene',EXTRA_TYPES))
def add_object_to_the_scene(size, mesh):
    f = open('./scripts/blender_script_object.py', "w")

    script_code = Code_constructor.import_required_packages() + Code_constructor.delete_object() + Code_constructor.create_object(mesh, size)

    f.write(script_code)
    f.close()


@then(parsers.cfparse('it can be rendered in {resolution:String}',EXTRA_TYPES))
def render_check(resolution):
    f = open('./scripts/blender_script_object.py', "a")

    script_code = Code_constructor.resolution_setup(resolution) + Code_constructor.close_blender()
    
    f.write(script_code)
    f.close()

    subprocess.run([config.blender_path,  "--log", "'*'", "--log-file", config.log_output_folder+rf"{time.time()}.txt","-P", r"./scripts/blender_script_object.py", "-o", config.render_output_folder+fr"object_{time.time()}", "--render-frame","1","kostil_exit_error_generator"], shell=True)
