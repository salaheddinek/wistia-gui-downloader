#!/usr/bin/env python3
import os
import sys
import shutil


def join_path(i_path, i_folder_or_file):
    return os.path.abspath(os.path.join(i_path, i_folder_or_file))


def deploy_command(i_deploy_path, i_app_path, i_app_name, additional_params=""):
    cmd = ""
    cmd += "cd {}; ".format(i_deploy_path)
    cmd += f"pyinstaller {additional_params} --onefile -n {i_app_name} --clean  {i_app_path};"
    print("Build command:\n\n{}\n\n".format(cmd))
    os.system(cmd)


if __name__ == '__main__':
    main_path = os.path.dirname(sys.modules['__main__'].__file__)
    main_path = join_path(main_path, '..')
    deploy_path = join_path(main_path, 'deploy')
    images_path = join_path(main_path, 'images')
    app_path = join_path(join_path(main_path, 'src'), '__main__.py')
    app_name = "wistia_downloader"

    # ----+ deployment folder creation -----+
    print("Deployment path: {}".format(deploy_path))
    if os.path.exists(deploy_path):
        shutil.rmtree(deploy_path)
    os.makedirs(deploy_path)

    # ----+ freeze command -----+
    additional_param = ""
    if sys.platform.lower() == "darwin" or sys.platform.lower() == "win32":
        app_icon = join_path(images_path, "app.ico")
        additional_param = "-i {}".format(app_icon)
    deploy_command(deploy_path, app_path, app_name, additional_param)
