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
    if number < 0:
        return

    if (number < 2):
        local('ls -t ./versions | tail -n +1 | xargs rm -f')
        with ('cd /data/web_static/releases'):
            run('ls -t | tail -n +1 | xargs rm -f')
    else:
        local('ls -t ./versions | tail -n +{} | xargs rm -f'.format(number))
        with ('cd /data/web_static/releases'):
            run('ls -t | tail -n +{} | xargs rm -f'.format(number))
