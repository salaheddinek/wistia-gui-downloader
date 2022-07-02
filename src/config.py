import sys
import os
import logging


HELP_TEXT = """
Download wistia videos using videoplayer links:\n

Follow these steps:\n 
1. Right click on video.\n
2. Click 'copy link and thumbnail'.\n
3. Past it to link entry.\n
4. Click on <b>PROCESS</b> and wait for video to download.
"""

REPLACE_BTN_HELP_TEXT = """
Depending on the operating system, these characters can be 
forbidden to use for naming files:

  '\"', '\\', '/', ':', '?', '*', '|', '&#60;', '&#62;'
  
So these characters cannot be used in a video name. 

The <b>Replace</b> button can be used to replace these characters 
with similar usable characters in the video name entry.

It also replace space with '_'.
"""

USE_WORKING_DIR = True
HIDE_TITLE_PROCESS_BUTTON = False
MAX_VID_NAME_DISPLAY_LENGTH = 70


def get_working_dir():
    if USE_WORKING_DIR:
        return os.getcwd()
    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle, the PyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app
        # path into variable _MEIPASS'.
        folder_path = os.path.dirname(sys.executable)
    else:
        folder_path = os.path.dirname(os.path.abspath(__file__))
    if os.path.isfile(folder_path):
        folder_path = os.path.dirname(folder_path)
    return folder_path


def get_logs_path(package_name):
    parent_path = get_working_dir()
    return os.path.join(parent_path, package_name + ".log")


def get_download_folder_path(package_name):
    parent_path = get_working_dir()
    return os.path.join(parent_path, package_name + "_results")


def setup_logging(logger_name, logging_lvl, save_logs_to_file):
    init_logger = logging.getLogger(logger_name)
    init_logger.setLevel(logging_lvl)
    i_formatter = logging.Formatter('[%(levelname)s] [%(asctime)s] - %(message)s', "%Y-%m-%d %H:%M:%S")
    ch = logging.StreamHandler()
    ch.setFormatter(i_formatter)
    init_logger.addHandler(ch)
    if save_logs_to_file:
        log_file_path = get_logs_path(logger_name)
        if os.path.exists(log_file_path):
            os.remove(log_file_path)
        handler = logging.FileHandler(log_file_path, encoding='utf8')
        n_formatter = logging.Formatter('[%(levelname)s] [%(asctime)s] - %(message)s', "%Y-%m-%d %H:%M:%S")
        handler.setFormatter(n_formatter)
        handler.setLevel(logging_lvl)
        init_logger.addHandler(handler)
