#!/usr/bin/python3
""" This script generates a .tgz archive from the contents of
the web_static folder in this repository. All archives shall be
stored in a versions folder.
"""


def do_pack():
    """ Create a .tgz archive from the web_static folder.
    This function returns the archive path if successful, None otherwise.
    """
    from fabric.api import local

    filename = "web_static_$(date+%Y%m%d%H%M%S).tgz"
    local("mkdir -p versions")
    try:
        path = local("tar -zcf {} ./web_static"
                     .format(filename))
        return path
    except Exception as error:
        return None
