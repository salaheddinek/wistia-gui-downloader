#!/usr/bin/python3
__version__ = '2.1.0'
__author__ = 'Salah Eddine Kabbour'
__package__ = "wistia_downloader"


from ui_mainwindow import Ui_MainWindow
import PySide6.QtGui as Qg
import PySide6.QtCore as Qc
import PySide6.QtWidgets as Qw
from datetime import datetime
import logging
import qt_icons
import argparse
import sys
import os
import styling
import config
import requests
import re
import json
import urllib.request


def create_output_folder():
    path = config.get_download_folder_path(__package__)
    if not os.path.isdir(path):
        try:
            os.mkdir(path)
        except OSError:
            error_msg = "Creation of the directory '{}' failed".format(path)
            print(error_msg)
            return False
    return True


class VideoDownloadWorker(Qc.QObject):
    log = Qc.Signal(str, int, int)
    complete = Qc.Signal()

    def __init__(self, in_vid_link, in_resolution, in_vid_name, in_generate_notes=False, in_notes_text=""):
        super(VideoDownloadWorker, self).__init__()
        self.vid_link = in_vid_link
        self.vid_id = None
        self.resolution = in_resolution
        self.vid_name = in_vid_name
        self.generate_notes = in_generate_notes
        self.notes_text = in_notes_text

    def run(self):
        self.log.emit(f"video link: {self.vid_link}", logging.DEBUG, 5000)
        is_ok = self._verification()
        if not is_ok:
            self.complete.emit()
            return

        path = os.path.join(config.get_download_folder_path(__package__), self.vid_name)

        self.log.emit(f"notes data:\n\n{self.notes_text}\n\n", logging.DEBUG, 5000)
        if self.generate_notes:
            self.log.emit(f"generating notes text file: {self.vid_short_name()}", logging.INFO, 5000)
            with open(path + '_notes.txt', 'w') as f:
                f.write(self.notes_text)
        self.log.emit(f"Downloading video: {self.vid_short_name()}", logging.INFO, -1)
        self.log.emit(f"Downloading video path: {path + '.mp4'}", logging.DEBUG, 5000)
        self.log.emit(f"Downloading video id: {self.vid_id}", logging.DEBUG, 5000)
        self.log.emit(f"Downloading video resolution: {self.resolution}", logging.DEBUG, 5000)

        self._download_function(path)
        if os.path.isfile(path + ".mp4"):
            self.log.emit(f"successfully downloaded video: '{self.vid_short_name()}' !!!", logging.INFO, 5000)
        else:
            self.log.emit(f"ERROR in downloading (Maybe try a different resolution), video: {self.vid_short_name()}",
                          logging.ERROR, 5000)
        self.complete.emit()

    def _download_function(self, in_path):
        r = requests.get('https://fast.wistia.net/embed/iframe/' + self.vid_id, allow_redirects=True)
        content = str(r.content).replace('\\\'', '') \
                                .replace('\\\\"', '') \
                                .replace('\\', '')
        rs = re.search("iframeInit\((.*?)\);", content)
        json_config = json.loads("[" + rs.group(1) + "]")
        self.log.emit(f"json data:\n\n{json_config}\n\n", logging.DEBUG, 5000)
        assets = json_config[0]['assets']
        chosen_link = ""
        if self.resolution == "max_p":
            max_size = 0
            for a in assets:
                if a['size'] > max_size:
                    max_size = a['size']
                    chosen_link = a['url']
        else:
            res = int(self.resolution[:-1])
            for a in assets:
                if a['height'] == res and a['ext'] == "mp4":
                    chosen_link = a['url']
        if chosen_link == "":
            return
        self.log.emit(f"chosen link: {chosen_link}", logging.DEBUG, 5000)
        urllib.request.urlretrieve(chosen_link, in_path + ".mp4")

    def _verification(self):
        if self.vid_name == "":
            self.log.emit("ERROR: Video name must not be empty", logging.ERROR, 5000)
            return False

        forbidden_characters = ["/", "\\", ":", "<", ">", ":", "\"", "|", "?", "*"]
        for fc in forbidden_characters:
            if fc in self.vid_name:
                self.log.emit(f"ERROR: Video name must NOT contains forbidden character: {forbidden_characters}",
                              logging.ERROR, 5000)
                return False

        try:
            path = os.path.join(config.get_download_folder_path(__package__), "tmp_" + self.vid_name + ".txt")
            open(path, 'w').close()
            os.unlink(path)
        except OSError as err:
            error_s = str(err)
            self.log.emit(f"ERROR: cannot create file, OS error: {error_s}", logging.ERROR, 5000)
            return False

        idx_start = self.vid_link.find("?wvideo=")
        if idx_start == -1:
            self.log.emit("ERROR: Wrong link format", logging.ERROR, 5000)
            return False
        idx_end = self.vid_link.find("\">", idx_start)
        self.vid_id = self.vid_link[idx_start + 8:idx_end]
        return True

    def vid_short_name(self):
        max_l = config.MAX_VID_NAME_DISPLAY_LENGTH
        if len(self.vid_name) < max_l:
            return self.vid_name
        else:
            return self.vid_name[0:max_l-1] + "..."


class MainWindow(Qw.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.i = qt_icons.qt_icon_from_text_image(qt_icons.APP_ICON)
        self.setWindowIcon(self.i)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.help_msg = Qw.QMessageBox(self)
        self.replace_btn_help_msg = Qw.QMessageBox(self)
        self.setWindowTitle("Wistia downloader")
        self.thread = None
        self.downloader = None
        self._style_app()
        self._connect_signals()
        self.update_ui_elements()
        if config.HIDE_TITLE_PROCESS_BUTTON:
            self.ui.btn_process_title.hide()

    def process_link(self):
        original_link_text = self.ui.text_edit_link.toPlainText()
        video_title = self.ui.line_edit_prefix.text() + self.ui.line_edit_vid_title.text()
        res_opt = "720p"
        if self.ui.radio_btn_360p.isChecked():
            res_opt = "360p"
        elif self.ui.radio_btn_1080p.isChecked():
            res_opt = "1080p"
        elif self.ui.radio_btn_maxp.isChecked():
            res_opt = "max_p"

        is_generate_notes = self.ui.check_box_generate_notes.isChecked()
        notes_text = self.ui.text_edit_notes.toPlainText()

        self.thread = Qc.QThread()
        self.downloader = VideoDownloadWorker(original_link_text, res_opt, video_title, is_generate_notes, notes_text)
        self.downloader.moveToThread(self.thread)

        # Connect signals and slots
        self.thread.started.connect(self.downloader.run)
        self.thread.finished.connect(self.thread.deleteLater)

        self.downloader.complete.connect(self.thread.quit)
        self.downloader.complete.connect(self.downloader.deleteLater)
        self.downloader.log.connect(self.log)

        # start the thread
        self.thread.start()

        self.ui.btn_process.setEnabled(False)
        self.thread.finished.connect(
            lambda: self.ui.btn_process.setEnabled(True)
        )

    def clear_entries(self):
        self.log("Entries cleared")
        self.ui.text_edit_link.clear()
        self.ui.line_edit_vid_title.clear()
        self.ui.text_edit_notes.clear()

    def close_app(self):
        self.log("Closing app", logging.DEBUG)
        self.close()

    def replace_characters_in_title(self):
        txt = self.ui.line_edit_vid_title.text()
        # ["/", "\\", ":", "<", ">", ":", "\"", "|", "?", "*"]
        replace_dict = {"\\": "-", "/": "-", " ": "_", "é": "e", "è": "e", ":": "=", "?": "", "*": "+", "|": "-",
                        "<": "", ">": ""}

        for key in replace_dict:
            txt = txt.replace(key, replace_dict[key])

        txt = txt.replace("_-_", "-")
        self.ui.line_edit_vid_title.setText(txt)

    def update_ui_elements(self):
        if self.ui.logs_check_box.isChecked():
            self.ui.plain_text_logs.show()
        else:
            self.ui.plain_text_logs.hide()

        if self.ui.check_box_adv_stg.isChecked():
            self.ui.wid_adv_stg.show()
        else:
            self.ui.wid_adv_stg.hide()

        if self.ui.check_box_generate_notes.isChecked():
            self.ui.text_edit_notes.setDisabled(False)
        else:
            self.ui.text_edit_notes.setDisabled(True)

    def _connect_signals(self):
        self.ui.btn_process.clicked.connect(self.process_link)
        self.ui.btn_clear.clicked.connect(self.clear_entries)
        self.ui.btn_quit.clicked.connect(self.close_app)
        self.ui.logs_check_box.clicked.connect(self.update_ui_elements)
        self.ui.check_box_adv_stg.clicked.connect(self.update_ui_elements)
        self.ui.check_box_generate_notes.clicked.connect(self.update_ui_elements)
        self.ui.btn_help.clicked.connect(self.help_msg.exec)
        self.ui.btn_replace_info.clicked.connect(self.replace_btn_help_msg.exec)
        self.ui.btn_process_title.clicked.connect(self.replace_characters_in_title)
        # Qc.QObject.connect(self.ui.btn_process, Qc.SIGNAL("clicked()"), self.process_link())

    def _style_app(self):

        # general frames
        self.ui.frame_header.setStyleSheet(styling.generate_frame_stylesheet(exclusive_id="frame_header"))
        self.ui.frame_adv_stg.setStyleSheet(styling.generate_frame_stylesheet(exclusive_id="frame_adv_stg"))

        # plain text edit
        entries = [self.ui.text_edit_notes, self.ui.text_edit_link, self.ui.plain_text_logs]
        for entry in entries:
            entry.setStyleSheet(styling.generate_frame_stylesheet(bg_color=styling.COLORS["entry_bg"]))

        # line edit
        line_edit_ss = styling.generate_line_edit_stylesheet(bg_color=styling.COLORS["entry_bg"])
        self.ui.line_edit_vid_title.setStyleSheet(line_edit_ss)
        self.ui.line_edit_prefix.setStyleSheet(line_edit_ss)

        # buttons
        self.Buttons_list = [self.ui.btn_process, self.ui.btn_quit, self.ui.btn_clear, self.ui.btn_process_title]
        for button in self.Buttons_list:
            btn_color = button.palette().color(Qg.QPalette.Button).name()
            button.setStyleSheet(styling.generate_button_stylesheet(btn_color))

        self.Tool_Buttons_list = [self.ui.btn_help, self.ui.btn_replace_info]
        for button in self.Tool_Buttons_list:
            btn_color = button.palette().color(Qg.QPalette.Button).name()
            button.setStyleSheet(styling.generate_tool_button_stylesheet(btn_color))

        # icons
        self.i_pro = qt_icons.qt_icon_from_text_image(qt_icons.SAVE_ICON)
        self.ui.btn_process.setIcon(self.i_pro)

        self.i_q = qt_icons.qt_icon_from_text_image(qt_icons.EXIT_ICON)
        self.ui.btn_quit.setIcon(self.i_q)

        self.i_c = qt_icons.qt_icon_from_text_image(qt_icons.CLEAR_ICON)
        self.ui.btn_clear.setIcon(self.i_c)

        self.i_h = qt_icons.qt_icon_from_text_image(qt_icons.INFO_ICON)
        self.ui.btn_help.setIcon(self.i_h)

        self.i_r = qt_icons.qt_icon_from_text_image(qt_icons.REPLACE_ICON)
        self.ui.btn_process_title.setIcon(self.i_r)

        self.i_i = qt_icons.qt_icon_from_text_image(qt_icons.BUTTON_INFO_ICON)
        self.ui.btn_replace_info.setIcon(self.i_i)

        # about us
        self.help_msg.setWindowTitle("About page")
        self.help_msg.setText(config.HELP_TEXT)

        self.replace_btn_help_msg.setWindowTitle("Replace name button info")
        self.replace_btn_help_msg.setText(config.REPLACE_BTN_HELP_TEXT)

    @Qc.Slot()
    def log(self, msg, log_lvl=logging.INFO, time=5000):
        logger = logging.getLogger(__package__)
        logger.log(log_lvl, msg)
        if log_lvl == logging.INFO or log_lvl == logging.WARNING or log_lvl == logging.ERROR:

            bar_msg = " " + msg.capitalize()
            now = datetime.now()
            ui_log = "<span>[<span style='color: {};'>{}</span>] [{}] - {}</span>"
            keys = {logging.INFO: "INFO", logging.WARNING: "WARN", logging.ERROR: "ERROR"}
            self.ui.plain_text_logs.appendHtml(ui_log.format(styling.LOGS_COLORS[log_lvl],
                                                             keys[log_lvl],
                                                             now.strftime("%H:%M:%S"),
                                                             msg.capitalize()))
            s_font = self.ui.statusbar.font()
            self.ui.statusbar.setStyleSheet(f"color: {styling.LOGS_COLORS[log_lvl]}")
            self.ui.statusbar.setFont(s_font)
            self.ui.statusbar.showMessage(bar_msg, time)


def boolean_string(s):
    if s not in {'False', 'True'}:
        raise ValueError('Not a valid boolean string')
    return s == 'True'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     description='Download wistia videos using videoplayer links')
    parser.add_argument('-s', '--style', help='Qt application style', type=str,
                        default="Fusion", metavar='\b')
    parser.add_argument('-l', '--log_level', help='FATAL = 50, ERROR = 40, WARNING = 30, INFO = 20, DEBUG = 10, '
                                                  'NOTSET = 0', type=int, default=20, metavar='\b')
    parser.add_argument('-k', '--style_keys', help='Show available styles for Qt application', type=boolean_string,
                        default=False, metavar='\b')
    parser.add_argument('-f', '--logs_file', help='Output logs to file', type=boolean_string,
                        default=False, metavar='\b')
    args = parser.parse_args()

    if args.style_keys:
        print(Qw.QStyleFactory.keys())
        exit(0)

    # Initiate logger
    config.setup_logging(__package__, args.log_level, args.logs_file)

    #  create output folder
    creation_ok = create_output_folder()
    if not creation_ok:
        exit(1)

    # initiate App
    app = Qw.QApplication(sys.argv)
    app.setStyle(args.style)
    window = MainWindow()

    window.show()
    sys.exit(app.exec())
