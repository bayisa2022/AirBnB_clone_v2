#!/usr/bin/python3

from fabric.api import env, put, run, settings # Import Fabric functions
import os

# Set hosts to deploy to 
env.hosts = ['<IP web-01>', '<IP web-02>']  

def do_deploy(archive_path):

  # Check if archive file exists
  if not os.path.exists(archive_path):
    return False

  # Get archive name and dir name
  archive_name = os.path.basename(archive_path) 
  archive_dir = archive_name.split('.')[0]

  # Wrap in error handling 
  with settings(warn_only=True):
    
    # Upload archive to temp directory
    put(archive_path, '/tmp/')  

    # Create releases dir if needed
    run('mkdir -p /data/web_static/releases/{}'.format(archive_dir))

    # Uncompress archive
    run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format(
      archive_name, archive_dir))

    # Delete uploaded archive
    run('rm /tmp/{}'.format(archive_name))

    # Delete old symlink
    run('rm -rf /data/web_static/current')

    # Symlink new release
    run('ln -s /data/web_static/releases/{} /data/web_static/current'.format(
      archive_dir))

  # Print success message
  print("New version deployed!") 
  return True
