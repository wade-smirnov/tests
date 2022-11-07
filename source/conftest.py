from pytest_bdd import given
import os
import config

#Shared steps
@given('Blender is installed and prepared')
def check_blender():
    assert os.path.exists(config.blender_path)