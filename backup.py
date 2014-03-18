#!/bin/sh
import argparse
import shlex
import subprocess
import datetime
import os

def main():
    parser = argparse.ArgumentParser(description='Scripts of Backup', prog='backup')

    parser.add_argument('-b', '--build', help='Make a backup of builds file', action='store_true', required=False)

    parser.add_argument('--version', action='version', version='%(prog)s 1.0')

    args = parser.parse_args()
    build = args.build

    time_stamp = datetime.datetime.utcnow().isoformat()
    time_stamp = time_stamp.replace(':', '-')
    src_folder_name = 'builds'
    dest_folder_name = src_folder_name + '-' + time_stamp

    src_path = '/home/raul/dev/works-py2/tests-django/'
    dest_path = '/home/raul/dev/gdrive/Projects/'

    # /home/raul/dev/works-py2/tests-django/builds
    src_root = src_path + src_folder_name
    # /home/raul/dev/gdrive/Projects/builds-2014-03-18T11-19-46.797044
    dest_root = dest_path + dest_folder_name


    if build:
        ### Folder builds/ ###
        subprocess.call(['cp', '-r', src_root, dest_path])
        subprocess.call(['mv', dest_path + src_folder_name, dest_root])
        subprocess.call(['sudo', 'rm', '-r', dest_path + dest_folder_name + '/' + 'node_modules'])
        # subprocess.call(['tar', '-cvf', dest_root + '.tar', dest_root])
        # subprocess.call(['nautilus', '--browser', dest_root])
        # subprocess.call(['gnome-open', dest_root])


        ### Gruntfile.js ###
        src_gruntfile_name = 'Gruntfile.js'
        # /home/raul/dev/works-py2/Gruntfile.js2014-03-18T11-52-53.546496
        dest_gruntfile_name = src_gruntfile_name + time_stamp
        # /home/raul/dev/gdrive/Projects/Gruntfile.js2014-03-18T11-52-53.546496
        dest_gruntfile_root = dest_path + dest_gruntfile_name

         ### File package.json ###
        src_package_name = 'package.json'
        # /home/raul/dev/works-py2/package.js2014-03-18T11-52-53.546496
        dest_package_name = src_package_name + time_stamp
        # /home/raul/dev/gdrive/Projects/package.js2014-03-18T11-52-53.546496
        dest_package_root = dest_path + dest_package_name

        file_names = [src_gruntfile_name, src_package_name]
        dest_files_root = [dest_gruntfile_root, dest_package_root]


        for i,j in enumerate(file_names):
            subprocess.call(['cp', '-r', '/home/raul/dev/works-py2/%s' %(file_names[i]), dest_path])
            subprocess.call(['mv', dest_path + file_names[i], dest_files_root[i]])

            #
            # subprocess.call(['cp', '-r', '/home/raul/dev/works-py2/package.js', dest_path])
            # subprocess.call(['mv', dest_path + src_package_name, dest_package_root])

        os.chdir('/home/raul/dev/gdrive/')
        subprocess.call(['grive'])
        subprocess.call(shlex.split('google-chrome https://drive.google.com/?tab=yo&authuser=0#folders/0B7xj8KJbuS8vNnZadWhhT0I3bnc'))

    # if deploy or create_deploy or create_deploy_git:
    #     call_process('sh-deploy-heroku')
    #
    # if git or create_deploy_git:
    #     call_process('sh-deploy-git')



def remove_pyc_files():
    subprocess.call(shlex.split('find . -name "*.pyc" -delete'))
    print('*** Removing .pyc files')
#
# def collectstatic():
#     subprocess.call(shlex.split('python manage.py collectstatic'))



main()