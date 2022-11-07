from pytest_bdd import given
import os
import config

#Shared steps
@given('Blender with empty world is prepared')
def check_blender():
    assert os.path.exists(config.blender_path)