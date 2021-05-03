#!/usr/bin/python3
""" This script deletes out-of-date archives from
/data/web_static/releases and versions folders of
a given server (or two in this case).
"""
from fabric.api import local, run, env
env.hosts = ['35.231.30.18', '34.73.105.29']


def do_clean(number=0):
    """ This function takes a 'number' parameter that states
    how many versions of archives shall be kept. If number is
    0 or 1, keep only the most recent version. If number is 2,
    keep latest and second latest version, and so on. """
    num = int(number)
    if num < 0:
        return

    if (num < 2):
        local('cd versions; ls -t | tail -n +2 | xargs rm -f')
        run('cd /data/web_static/releases; \
            ls -t | tail -n +2 | xargs rm -rf')
    else:
        number = number + 1
        local('cd versions; ls -t | tail -n +' +
              number + ' | xargs rm -rf')
        run('cd /data/web_static/releases; ls -t | tail -n +' +
            number + ' | xargs rm -rf')
