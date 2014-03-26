#!/usr/bin/python
from fabric.api import local, lcd, settings

global deploy_env
global git_env

deploy_env = '/home/raul/dev/works-py2/heroku-tests-django/tests-django/'
git_env = '/home/raul/dev/works-py2/tests-django/'

#### DEPLOY/PUSH FOR GIT OR HEROKU' ####

def deploy(remote, origin='heroku'):
    local('pip freeze > requirements.txt')
    setup(deploy_env, origin, remote)

def git(remote, origin='origin'):
    setup(git_env, origin, remote)
    local('git push -u origin master')

def setup(env, origin, remote):
    with lcd(env):
        print(origin, remote)
        local('pwd')
        remove_pyc_files()

        local('git init')
        local('git add .')

        with settings(warn_only=True):
            print("*** Enter your Commit Comment: ")
            comment = raw_input()
            if not comment:
                comment = 'Auto Commit'

                local('git commit -m "%s"' % comment)

            error = 128;
            result = local('git remote add %s %s' %(origin, remote))
            if result.return_code == error:
                print("*** Remote already exists. Command ignored. ")

            # local('heroku maintenance:on')
            local('git push -f heroku master')
            # local('heroku maintenance:off')

def remove_pyc_files():
    local('find . -name "*.pyc" -delete')