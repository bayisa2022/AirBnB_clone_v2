#!/usr/bin/python3
"""
Fabric script based on the file 3-deploy_web_static.py that deletes out-of-date archives
using the function do_clean.
"""
from fabric.api import env, run, local
from fabric.operations import put
import os


env.hosts = ['<IP web-01>', '<IP web-02>']


def do_clean(number=0):
    """
    Deletes out-of-date archives using the function do_clean.
    """
    number = int(number)
    if number < 0:
        return False
    elif number == 0 or number == 1:
        number = 1
    else:
        number += 1

    local("ls -1t versions/ | tail -n +{} | xargs -I {{}} rm versions/{{}}".format(number))

    run("ls -1t /data/web_static/releases/ | tail -n +{} | xargs -I {{}} rm -rf /data/web_static/releases/{{}}".format(number))

    return True


def deploy():
    """
    Creates and distributes an archive to your web servers using the function deploy.
    """
    archive_path = do_pack()
    if not archive_path:
        return False

    return do_deploy(archive_path)
