import os

from unipath import FSPath as Path

import fabric.contrib.project as project
from fabric.api import *

FAB_ROOT = Path(os.path.dirname(__file__))

env.host_string = 'prgmr'
env.python = Path('/Users/kennethlove/.virtualenvs/gigantuan/bin/python')
env.hyde = Path('/Users/kennethlove/.virtualenvs/gigantuan/bin/hyde')

PROD_DEST_PATH = Path('/home/kennethlove/public_html/gigantuan.net/public')
LOCAL_EXPORT_PATH = Path(FAB_ROOT, 'static')

def clean():
    local('rm -rf ./static')

def generate():
    local('%s -s dynamic gen -d ../static' % env['hyde'])

def regen():
    clean()
    generate()

@hosts(env.host_string)
def publish():
    regen()
    project.rsync_project(
        remote_dir=PROD_DEST_PATH,
        local_dir=LOCAL_EXPORT_PATH.rstrip('/') + '/',
        delete=True
    )
