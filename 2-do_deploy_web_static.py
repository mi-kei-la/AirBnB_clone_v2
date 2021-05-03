#!/usr/bin/python3
""" Fabric script that distributes an archive to your web servers.
"""
from fabric.api import local, run, put, env
from os import path

env.hosts = ['35.231.30.18', '34.73.105.29']


def do_deploy(archive_path):
    """This function distributes an archive to your web servers"""
    if path.exists(archive_path) is False:
        return False

    try:
        # Remove folder name and extension from file name
        slash = archive_path.find('/') + 1
        filename = archive_path[find:]

        # Upload archive to /tmp/
        put(archive_path, '/tmp/{}'.format(filename))

        # Uncompress archive and delete original
        run('mkdir -p /data/web_static/releases/')
        run('tar -xzvf /tmp/{} -C /data/web_static/releases/{}'
            .format(filename, filename[:-4]))
        run('rm /tmp/{}'.format(filename))

        # Update symbolic link
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{} /data/web_static/current'
            .format(filename[:-4]))

        return True

    except Exception as e:
        return False
