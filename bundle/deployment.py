#!/usr/bin/env python3
import os
from os import path
import sys
import shutil
import PyInstaller.__main__
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


def deploy_command(i_deploy_path, i_app_path, additional_params=""):
    # cmd = ""
    # cmd += "cd {}; ".format(i_deploy_path)
    # cmd += f"pyinstaller {additional_params} --onefile -n {i_app_name} --clean  {i_app_path};"
    # print("Build command:\n\n{}\n\n".format(cmd))
    # os.system(cmd)
    name = get_app_full_name(i_app_path)
    cmd = [i_app_path, "--onefile", "-n", name, "--clean", "--distpath", path.join(i_deploy_path, "dist"),
           "--workpath", path.join(i_deploy_path, "build"), "--specpath", i_deploy_path]
    for param in additional_params:
        cmd += [param]
    PyInstaller.__main__.run(cmd)


if __name__ == '__main__':
    main_path = os.path.abspath(os.path.dirname(sys.modules['__main__'].__file__))
    main_path = os.path.abspath(path.join(main_path, '..'))
    deploy_path = path.join(main_path, 'deploy')
    app_path = path.join(path.join(main_path, 'src'), '__main__.py')

    # ----+ deployment folder creation -----+
    print("Deployment path: {}".format(deploy_path))
    if os.path.exists(deploy_path):
        shutil.rmtree(deploy_path)
    os.makedirs(deploy_path)

    # ----+ freeze command -----+
    additional_param = []
    if sys.platform.lower() == "darwin" or sys.platform.lower() == "win32":
        app_icon = path.join(path.join(main_path, "images"), "app.ico")
        # additional_param = "-i {}".format(app_icon)
        additional_param = ["-i", app_icon]
    deploy_command(deploy_path, app_path, additional_param)
