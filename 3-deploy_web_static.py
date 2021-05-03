#!/usr/bin/python3
""" This module creates and distributes an archive to web servers.
"""
from fabric.api import local, run, put, env
from os import path
from datetime import datetime
env.hosts = ['35.231.30.18', '34.73.105.29']


def deploy():
    """Pack archive and distribute to web servers."""
    filename = do_pack()
    if filename is False:
        return False
    return do_deploy(filename)


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
        run('tar -xzvf /tmp/' + filename + ' -C /data/web_static/releases/' +
            filename[:-4] + '/')
        run('rm /tmp/' + filename)

        # Move uncompressed files to parent folder (file is a folder)
        run('mv /data/web_static/releases/' + filename[:-4] + '/web_static/* \
            /data/web_static/releases/' + filename[:-4] + '/')
        run('rm -rf /data/web_static/releases/' + filename[:-4] +
            '/web_static')

        # Update symbolic link
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{} /data/web_static/current'
            .format(filename[:-4]))

        return True

    except Exception as e:
        print('error:')
        print(e)
        return False


def do_pack():
    """ Create a .tgz archive from the web_static folder.
    This function returns the archive path if successful, None otherwise.
    """
    filename = "web_static_" + datetime.strftime(datetime.now(),
                                                 "%Y%m%d%H%M%S") + ".tgz"
    local("mkdir -p versions")
    try:
        local("tar -czvf ./versions/{} ./web_static" .format(filename))
        return "versions/{}".format(filename)
    except Exception as error:
        return None
