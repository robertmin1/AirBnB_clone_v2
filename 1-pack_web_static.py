#!/usr/bin/python3
# Fabfile to generates a .tgz archive from the contents of web_static.
from fabric.api import local
from datetime import datetime

def do_pack():
    try:
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        archive_path = "versions/web_static_{}.tgz".format(now)
        local("tar-cvzf {} web_static".format(archive_path))
        return archive_path
    except:
        return None
