#!/usr/bin/python3
"""
Fabric script based on the file 2-do_deploy_web_static.py that creates and distributes
an archive to your web servers using the function deploy.
"""
from fabric.api import env, run
from fabric.operations import put
from fabric.contrib import files
from datetime import datetime
import os


env.hosts = ['<IP web-01>', '<IP web-02>']


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """
    try:
        now = datetime.now()
        file_name = "web_static_{}{}{}{}{}{}.tgz".format(now.year, now.month,
                                                         now.day, now.hour,
                                                         now.minute, now.second)
        local("mkdir -p versions")
        local("tar -cvzf versions/{} web_static".format(file_name))
        return "versions/{}".format(file_name)
    except:
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers using the function do_deploy.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        file_no_ext = os.path.splitext(file_name)[0]
        remote_path = "/tmp/{}".format(file_name)
        remote_dir = "/data/web_static/releases/{}".format(file_no_ext)

        put(archive_path, remote_path)
        run("mkdir -p {}".format(remote_dir))
        run("tar -xzf {} -C {}".format(remote_path, remote_dir))
        run("rm {}".format(remote_path))
        run("mv {}/web_static/* {}".format(remote_dir, remote_dir))
        run("rm -rf {}/web_static".format(remote_dir))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(remote_dir))

        return True
    except:
        return False


def deploy():
    """
    Creates and distributes an archive to your web servers using the function deploy.
    """
    archive_path = do_pack()
    if not archive_path:
        return False

    return do_deploy(archive_path)
