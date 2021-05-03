#!/usr/bin/python3
""" Fabric script that distributes an archive to your web servers.
"""
from fabric.api import local, run, put, env
from os import path

env.hosts = ['35.231.30.18', '34.73.105.29']


def do_deploy(archive_path):
    """This function distributes an archive to your web servers"""
    if path.exists(archive_path) is False:
        print('file not found')
        return False

    try:
        # Remove folder name and extension from file name
        slash = archive_path.find('/') + 1
        filename = archive_path[slash:]

        # Upload archive to /tmp/
        put(archive_path, '/tmp/{}'.format(filename))

        # Uncompress file and delete original
        run('mkdir -p /data/web_static/releases/' + filename[:-4])
        run('tar -xzvf /tmp/' + filename + ' -C /data/web_static/releases/'
            + filename[:-4] + '/')
        run('rm /tmp/' + filename)

        # Move uncompressed files to parent folder (file is a folder)
        run('mv /data/web_static/releases/' + filename[:-4] + '/web_static/* \
        /data/web_static/releases/' + filename[:-4] + '/')
        run('rm -rf /data/web_static/releases/' + filename[:-4]
            + '/web_static')

        # Update symbolic link
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{} /data/web_static/current'
            .format(filename[:-4]))

        return True

    except Exception as e:
        print('error:')
        print(e)
        return False
