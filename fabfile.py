#coding: u8

from fabric.api import (
    env,
    roles,
    run,
    sudo,
    local,
)

env.roledefs = dict(
    product=(
        'user@host'
    ),
)

env.passwords = {
    'user@host:22': 'password'
}

proj_info = dict(
    PROJECT_SUPERVISOR_NAME='xxx',
    PROJECT_PATH_ON_SERVER='/home/path/to/project',
    PROJECT_RELEASE_BRANCH='master',
)

@roles('product')
def deploy():
    run('cd %(PROJECT_PATH_ON_SERVER)s && git pull origin %(PROJECT_RELEASE_BRANCH)s' % proj_info)
    sudo('supervisorctl restart %(PROJECT_SUPERVISOR_NAME)s' % proj_info)

@roles('product')
def up():
    local('git commit . -m dev')
    local('git push origin master')
    run('cd %(PROJECT_PATH_ON_SERVER)s && git pull origin %(PROJECT_RELEASE_BRANCH)s' % proj_info)
    sudo('supervisorctl restart %(PROJECT_SUPERVISOR_NAME)s' % proj_info)

@roles('product')
def pip():
    cmds = [
        'cd %(PROJECT_PATH_ON_SERVER)s',
        'git pull origin %(PROJECT_RELEASE_BRANCH)s',
        'source venv/bin/activate',
        'pip install -r requirements.txt',
    ]
    run((' && '.join(cmds)) % proj_info)

