#!/bin/sh
import argparse
import shlex
import subprocess


def main():
    parser = argparse.ArgumentParser(description='Scripts of Push', prog='push')

    parser.add_argument('-c', '--create', help='CREATE a HEROKU project', action='store_true', required=False)
    parser.add_argument('-d', '--deploy', help='DEPLOY the HEROKU project', action='store_true', required=False)
    parser.add_argument('-g', '--git', help='PUSH SRC project to GITHUB', action='store_true', required=False)
    parser.add_argument('-cd', '--create_deploy', help='CREATE and DEPLOY the HEROKU project', action='store_true', required=False)
    parser.add_argument('-all', '--create_deploy_git', help='CREATE, DEPLOY HEROKU project and PUSH SRC to GITHUB', action='store_true', required=False)

    parser.add_argument('--version', action='version', version='%(prog)s 1.0')

    args = parser.parse_args()
    create = args.create
    deploy = args.deploy
    git = args.git

    create_deploy = args.create_deploy
    create_deploy_git = args.create_deploy_git


    # would hit just one option or pre combinations valor
    if (git and (create or deploy or create_deploy or create_deploy_git)) \
        or (create and (deploy or create_deploy or create_deploy_git)) \
        or (deploy and (create_deploy or create_deploy_git)) \
        or (create_deploy and create_deploy_git):

        msg = '*** For possible combinations, please hit --help'
        raise argparse.ArgumentError(msg)

    if create or create_deploy or create_deploy_git:
        call_process('sh-create-heroku-project')

    if deploy or create_deploy or create_deploy_git:
        call_process('sh-deploy-heroku')

    if git or create_deploy_git:
        call_process('sh-deploy-git')



def call_process(process):
    remove_pyc_files()
    subprocess.call([process])

def remove_pyc_files():
    subprocess.call(shlex.split('find . -name "*.pyc" -delete'))
    print('*** Removing .pyc files')
#
# def collectstatic():
#     subprocess.call(shlex.split('python manage.py collectstatic'))



main()