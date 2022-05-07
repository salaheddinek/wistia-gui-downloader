# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPlainTextEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QStatusBar, QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1068, 872)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(240, 240, 240, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(247, 247, 247, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(120, 120, 120, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(160, 160, 160, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush6 = QBrush(QColor(255, 255, 220, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush7 = QBrush(QColor(0, 0, 0, 128))
        brush7.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        MainWindow.setPalette(palette)
        font = QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_6 = QWidget(self.centralwidget)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.horizontalLayout_6 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.frame_header = QFrame(self.widget_6)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setFrameShape(QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_header)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.check_box_adv_stg = QCheckBox(self.frame_header)
        self.check_box_adv_stg.setObjectName(u"check_box_adv_stg")
        self.check_box_adv_stg.setChecked(False)

        self.horizontalLayout.addWidget(self.check_box_adv_stg)

        self.logs_check_box = QCheckBox(self.frame_header)
        self.logs_check_box.setObjectName(u"logs_check_box")
        self.logs_check_box.setChecked(False)

        self.horizontalLayout.addWidget(self.logs_check_box)

        self.btn_help = QToolButton(self.frame_header)
        self.btn_help.setObjectName(u"btn_help")

        self.horizontalLayout.addWidget(self.btn_help)


        self.horizontalLayout_6.addWidget(self.frame_header)


        self.verticalLayout_2.addWidget(self.widget_6)

        self.widget_9 = QWidget(self.centralwidget)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy)
        self.horizontalLayout_8 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(6, 6, 6, 6)
        self.widget_10 = QWidget(self.widget_9)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_5 = QVBoxLayout(self.widget_10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.widget_10)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label)

        self.text_edit_link = QPlainTextEdit(self.widget_10)
        self.text_edit_link.setObjectName(u"text_edit_link")

        self.verticalLayout_5.addWidget(self.text_edit_link)

        self.widget_2 = QWidget(self.widget_10)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 100))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_process = QPushButton(self.widget_2)
        self.btn_process.setObjectName(u"btn_process")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_process.sizePolicy().hasHeightForWidth())
        self.btn_process.setSizePolicy(sizePolicy1)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush8 = QBrush(QColor(239, 248, 232, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush9 = QBrush(QColor(247, 251, 243, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush9)
        brush10 = QBrush(QColor(119, 124, 116, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush10)
        brush11 = QBrush(QColor(159, 165, 155, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush11)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush9)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush9)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush10)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush11)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush9)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush9)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush10)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush11)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.btn_process.setPalette(palette1)

        self.horizontalLayout_3.addWidget(self.btn_process)

        self.btn_clear = QPushButton(self.widget_2)
        self.btn_clear.setObjectName(u"btn_clear")
        sizePolicy1.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.btn_clear)


        self.verticalLayout_5.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget_10)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.line_edit_vid_title = QLineEdit(self.widget_3)
        self.line_edit_vid_title.setObjectName(u"line_edit_vid_title")

        self.horizontalLayout_2.addWidget(self.line_edit_vid_title)


        self.verticalLayout_5.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget_10)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.radio_btn_360p = QRadioButton(self.widget_4)
        self.radio_btn_360p.setObjectName(u"radio_btn_360p")

        self.horizontalLayout_4.addWidget(self.radio_btn_360p)

        self.radio_btn_720p = QRadioButton(self.widget_4)
        self.radio_btn_720p.setObjectName(u"radio_btn_720p")

        self.horizontalLayout_4.addWidget(self.radio_btn_720p)

        self.radio_btn_1080p = QRadioButton(self.widget_4)
        self.radio_btn_1080p.setObjectName(u"radio_btn_1080p")

        self.horizontalLayout_4.addWidget(self.radio_btn_1080p)

        self.radio_btn_maxp = QRadioButton(self.widget_4)
        self.radio_btn_maxp.setObjectName(u"radio_btn_maxp")
        self.radio_btn_maxp.setChecked(True)

        self.horizontalLayout_4.addWidget(self.radio_btn_maxp)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout_5.addWidget(self.widget_4)


        self.horizontalLayout_8.addWidget(self.widget_10)

        self.wid_adv_stg = QWidget(self.widget_9)
        self.wid_adv_stg.setObjectName(u"wid_adv_stg")
        self.verticalLayout_6 = QVBoxLayout(self.wid_adv_stg)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(self.wid_adv_stg)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_6.addWidget(self.label_5)

        self.frame_adv_stg = QFrame(self.wid_adv_stg)
        self.frame_adv_stg.setObjectName(u"frame_adv_stg")
        self.frame_adv_stg.setFrameShape(QFrame.StyledPanel)
        self.frame_adv_stg.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_adv_stg)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_8 = QWidget(self.frame_adv_stg)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.widget_8)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_7.addWidget(self.label_4)

        self.line_edit_prefix = QLineEdit(self.widget_8)
        self.line_edit_prefix.setObjectName(u"line_edit_prefix")

        self.horizontalLayout_7.addWidget(self.line_edit_prefix)


        self.verticalLayout.addWidget(self.widget_8)

        self.widget = QWidget(self.frame_adv_stg)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_9 = QHBoxLayout(self.widget)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btn_process_title = QPushButton(self.widget)
        self.btn_process_title.setObjectName(u"btn_process_title")

        self.horizontalLayout_9.addWidget(self.btn_process_title)

        self.btn_replace_info = QToolButton(self.widget)
        self.btn_replace_info.setObjectName(u"btn_replace_info")

        self.horizontalLayout_9.addWidget(self.btn_replace_info)


        self.verticalLayout.addWidget(self.widget)

        self.check_box_generate_notes = QCheckBox(self.frame_adv_stg)
        self.check_box_generate_notes.setObjectName(u"check_box_generate_notes")
        self.check_box_generate_notes.setChecked(False)

        self.verticalLayout.addWidget(self.check_box_generate_notes)

        self.text_edit_notes = QPlainTextEdit(self.frame_adv_stg)
        self.text_edit_notes.setObjectName(u"text_edit_notes")

        self.verticalLayout.addWidget(self.text_edit_notes)


        self.verticalLayout_6.addWidget(self.frame_adv_stg)


        self.horizontalLayout_8.addWidget(self.wid_adv_stg)


        self.verticalLayout_2.addWidget(self.widget_9)

        self.plain_text_logs = QPlainTextEdit(self.centralwidget)
        self.plain_text_logs.setObjectName(u"plain_text_logs")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.plain_text_logs.sizePolicy().hasHeightForWidth())
        self.plain_text_logs.setSizePolicy(sizePolicy2)
        self.plain_text_logs.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.plain_text_logs)

        self.widget_5 = QWidget(self.centralwidget)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.btn_quit = QPushButton(self.widget_5)
        self.btn_quit.setObjectName(u"btn_quit")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush12 = QBrush(QColor(248, 232, 232, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush13 = QBrush(QColor(251, 243, 243, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush13)
        brush14 = QBrush(QColor(124, 116, 116, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush14)
        brush15 = QBrush(QColor(165, 155, 155, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush15)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette2.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush13)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush13)
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush14)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush15)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette2.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush13)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush14)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush13)
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush14)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush15)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush14)
        palette2.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush14)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette2.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush12)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.btn_quit.setPalette(palette2)

        self.horizontalLayout_5.addWidget(self.btn_quit)


        self.verticalLayout_2.addWidget(self.widget_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.check_box_adv_stg.setText(QCoreApplication.translate("MainWindow", u"Advanced settings", None))
        self.logs_check_box.setText(QCoreApplication.translate("MainWindow", u"Show logs", None))
#if QT_CONFIG(tooltip)
        self.btn_help.setToolTip(QCoreApplication.translate("MainWindow", u"About page", None))
#endif // QT_CONFIG(tooltip)
        self.btn_help.setText(QCoreApplication.translate("MainWindow", u"help", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Original Link", None))
        self.btn_process.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Video name:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Resolution:", None))
        self.radio_btn_360p.setText(QCoreApplication.translate("MainWindow", u"360p", None))
        self.radio_btn_720p.setText(QCoreApplication.translate("MainWindow", u"720p", None))
        self.radio_btn_1080p.setText(QCoreApplication.translate("MainWindow", u"1080p", None))
        self.radio_btn_maxp.setText(QCoreApplication.translate("MainWindow", u"max", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Advanced settings", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"File Prefix", None))
        self.btn_process_title.setText(QCoreApplication.translate("MainWindow", u"Replace name", None))
        self.btn_replace_info.setText(QCoreApplication.translate("MainWindow", u"i", None))
        self.check_box_generate_notes.setText(QCoreApplication.translate("MainWindow", u"Generate notes file", None))
        self.btn_quit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
    # retranslateUi

