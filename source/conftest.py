from pytest_bdd import given
import os
import config
from datetime import datetime
import platform


#Shared steps
@given('Blender is installed and prepared')
def check_blender(json_metadata):
    assert os.path.exists(config.blender_path)
    now = datetime.now()
    json_metadata['date and time']= now.strftime("%d/%m/%Y %H:%M:%S")
    json_metadata['processor info']=platform.processor()
    json_metadata['machine']=platform.machine()