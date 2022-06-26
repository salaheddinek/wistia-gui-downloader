#!/usr/bin/env python3
import zipapp
import sys
from os import path
import os
import shutil
import re

APP_NAME = "wistia_downloader"
ADD_VERSION_AS_SUFFIX = False


def get_app_full_name(i_app_path):
    name = APP_NAME
    if ADD_VERSION_AS_SUFFIX:
        with open(i_app_path, "r") as f:
            txt = f.read()
            v_re = r"^__version__ = ['\"]([^'\"]*)['\"]"
            version = re.search(v_re, txt, re.M)
            if version:
                name += "_v" + version.group(1)
    return name


def is_file_accepted(i_file_path):
    if i_file_path.suffix == ".py":
        return True
    return False


if __name__ == '__main__':
    main_path = path.dirname(sys.modules['__main__'].__file__)
    main_path = path.join(main_path, '..')
    deploy_path = path.join(main_path, 'deploy')
    app_path = path.join(main_path, 'src')

    app_name = get_app_full_name(path.join(app_path, "__main__.py"))

    if os.path.exists(deploy_path):
        shutil.rmtree(deploy_path)
    os.makedirs(deploy_path)

    zipapp.create_archive(app_path, path.join(deploy_path, app_name + ".pyz"), '/usr/bin/python3',
                          filter=is_file_accepted)

    print(f"wrapping finished! Output file: {app_name}.pyz")
