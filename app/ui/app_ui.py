# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'appeEkGTb.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QToolButton, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)
import ui.icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1137, 622)
        icon = QIcon()
        icon.addFile(u":/icon/yt-dlp-gui.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setPointSize(9)
        self.centralwidget.setFont(font)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gb_status = QGroupBox(self.centralwidget)
        self.gb_status.setObjectName(u"gb_status")
        self.gridLayout_3 = QGridLayout(self.gb_status)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tw = QTreeWidget(self.gb_status)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setTextAlignment(5, Qt.AlignCenter);
        __qtreewidgetitem.setTextAlignment(4, Qt.AlignCenter);
        __qtreewidgetitem.setTextAlignment(3, Qt.AlignCenter);
        __qtreewidgetitem.setTextAlignment(2, Qt.AlignCenter);
        self.tw.setHeaderItem(__qtreewidgetitem)
        self.tw.setObjectName(u"tw")
        self.tw.header().setVisible(True)

        self.gridLayout_3.addWidget(self.tw, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.gb_status, 1, 0, 1, 3)

        self.gb_controls = QGroupBox(self.centralwidget)
        self.gb_controls.setObjectName(u"gb_controls")
        self.verticalLayout_2 = QVBoxLayout(self.gb_controls)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pb_add = QPushButton(self.gb_controls)
        self.pb_add.setObjectName(u"pb_add")
        icon1 = QIcon()
        icon1.addFile(u":/buttons/add.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_add.setIcon(icon1)
        self.pb_add.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.pb_add)

        self.pb_clear = QPushButton(self.gb_controls)
        self.pb_clear.setObjectName(u"pb_clear")
        icon2 = QIcon()
        icon2.addFile(u":/buttons/clear.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_clear.setIcon(icon2)
        self.pb_clear.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.pb_clear)

        self.pb_download = QPushButton(self.gb_controls)
        self.pb_download.setObjectName(u"pb_download")
        icon3 = QIcon()
        icon3.addFile(u":/buttons/download.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_download.setIcon(icon3)
        self.pb_download.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.pb_download)


        self.gridLayout.addWidget(self.gb_controls, 0, 2, 1, 1)

        self.gb_args = QGroupBox(self.centralwidget)
        self.gb_args.setObjectName(u"gb_args")
        self.gridLayout_4 = QGridLayout(self.gb_args)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lb_link = QLabel(self.gb_args)
        self.lb_link.setObjectName(u"lb_link")
        self.lb_link.setMinimumSize(QSize(0, 0))

        self.gridLayout_4.addWidget(self.lb_link, 0, 0, 1, 1)

        self.lb_path = QLabel(self.gb_args)
        self.lb_path.setObjectName(u"lb_path")
        self.lb_path.setMinimumSize(QSize(0, 0))

        self.gridLayout_4.addWidget(self.lb_path, 1, 0, 1, 1)

        self.le_path = QLineEdit(self.gb_args)
        self.le_path.setObjectName(u"le_path")
        self.le_path.setEnabled(False)
        self.le_path.setReadOnly(False)

        self.gridLayout_4.addWidget(self.le_path, 1, 1, 1, 2)

        self.tb_path = QToolButton(self.gb_args)
        self.tb_path.setObjectName(u"tb_path")

        self.gridLayout_4.addWidget(self.tb_path, 1, 3, 1, 1)

        self.lb_format = QLabel(self.gb_args)
        self.lb_format.setObjectName(u"lb_format")
        self.lb_format.setMinimumSize(QSize(0, 0))

        self.gridLayout_4.addWidget(self.lb_format, 2, 0, 1, 1)

        self.le_link = QLineEdit(self.gb_args)
        self.le_link.setObjectName(u"le_link")
        self.le_link.setClearButtonEnabled(True)

        self.gridLayout_4.addWidget(self.le_link, 0, 1, 1, 3)

        self.dd_format = QComboBox(self.gb_args)
        self.dd_format.addItem("")
        self.dd_format.addItem("")
        self.dd_format.addItem("")
        self.dd_format.addItem("")
        self.dd_format.addItem("")
        self.dd_format.setObjectName(u"dd_format")
        self.dd_format.setMinimumSize(QSize(0, 0))

        self.gridLayout_4.addWidget(self.dd_format, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(219, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 2, 2, 1, 2)


        self.gridLayout.addWidget(self.gb_args, 0, 0, 1, 1)

        self.gb_embeds = QGroupBox(self.centralwidget)
        self.gb_embeds.setObjectName(u"gb_embeds")
        self.gb_embeds.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.gb_embeds.setFlat(False)
        self.gb_embeds.setCheckable(False)
        self.gridLayout_2 = QGridLayout(self.gb_embeds)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.gb_embeds)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 4, 0, 1, 1)

        self.pb_save_preset = QPushButton(self.gb_embeds)
        self.pb_save_preset.setObjectName(u"pb_save_preset")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_save_preset.sizePolicy().hasHeightForWidth())
        self.pb_save_preset.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.pb_save_preset, 3, 2, 1, 2)

        self.lb_presets = QLabel(self.gb_embeds)
        self.lb_presets.setObjectName(u"lb_presets")

        self.gridLayout_2.addWidget(self.lb_presets, 2, 0, 1, 1)

        self.lb_filename = QLabel(self.gb_embeds)
        self.lb_filename.setObjectName(u"lb_filename")

        self.gridLayout_2.addWidget(self.lb_filename, 0, 0, 1, 1)

        self.dd_presets = QComboBox(self.gb_embeds)
        self.dd_presets.addItem("")
        self.dd_presets.setObjectName(u"dd_presets")

        self.gridLayout_2.addWidget(self.dd_presets, 2, 1, 1, 1)

        self.le_cargs = QLineEdit(self.gb_embeds)
        self.le_cargs.setObjectName(u"le_cargs")
        self.le_cargs.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.le_cargs, 1, 1, 1, 3)

        self.pb_delete_preset = QPushButton(self.gb_embeds)
        self.pb_delete_preset.setObjectName(u"pb_delete_preset")
        sizePolicy.setHeightForWidth(self.pb_delete_preset.sizePolicy().hasHeightForWidth())
        self.pb_delete_preset.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.pb_delete_preset, 2, 2, 1, 2)

        self.lb_cargs = QLabel(self.gb_embeds)
        self.lb_cargs.setObjectName(u"lb_cargs")

        self.gridLayout_2.addWidget(self.lb_cargs, 1, 0, 1, 1)

        self.dd_sponsorblock = QComboBox(self.gb_embeds)
        self.dd_sponsorblock.addItem("")
        self.dd_sponsorblock.addItem("")
        self.dd_sponsorblock.addItem("")
        self.dd_sponsorblock.setObjectName(u"dd_sponsorblock")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dd_sponsorblock.sizePolicy().hasHeightForWidth())
        self.dd_sponsorblock.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.dd_sponsorblock, 4, 1, 1, 1)

        self.le_preset_name = QLineEdit(self.gb_embeds)
        self.le_preset_name.setObjectName(u"le_preset_name")

        self.gridLayout_2.addWidget(self.le_preset_name, 3, 1, 1, 1)

        self.cb_thumbnail = QCheckBox(self.gb_embeds)
        self.cb_thumbnail.setObjectName(u"cb_thumbnail")

        self.gridLayout_2.addWidget(self.cb_thumbnail, 1, 4, 1, 1)

        self.cb_metadata = QCheckBox(self.gb_embeds)
        self.cb_metadata.setObjectName(u"cb_metadata")

        self.gridLayout_2.addWidget(self.cb_metadata, 0, 4, 1, 1)

        self.cb_subtitles = QCheckBox(self.gb_embeds)
        self.cb_subtitles.setObjectName(u"cb_subtitles")

        self.gridLayout_2.addWidget(self.cb_subtitles, 2, 4, 1, 1)

        self.le_filename = QLineEdit(self.gb_embeds)
        self.le_filename.setObjectName(u"le_filename")
        self.le_filename.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.le_filename, 0, 1, 1, 3)

        self.cb_chapters = QCheckBox(self.gb_embeds)
        self.cb_chapters.setObjectName(u"cb_chapters")

        self.gridLayout_2.addWidget(self.cb_chapters, 3, 4, 1, 1)


        self.gridLayout.addWidget(self.gb_embeds, 0, 1, 1, 1)

        self.gridLayout.setRowStretch(0, 2)
        self.gridLayout.setRowStretch(1, 5)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)
        QWidget.setTabOrder(self.le_path, self.pb_add)
        QWidget.setTabOrder(self.pb_add, self.pb_clear)
        QWidget.setTabOrder(self.pb_clear, self.pb_download)
        QWidget.setTabOrder(self.pb_download, self.tw)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"yt-dlp-gui", None))
        self.gb_status.setTitle(QCoreApplication.translate("MainWindow", u"Status", None))
        ___qtreewidgetitem = self.tw.headerItem()
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"ETA", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"Speed", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Progress", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Size", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Format", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Title", None));
        self.gb_controls.setTitle(QCoreApplication.translate("MainWindow", u"Controls", None))
#if QT_CONFIG(tooltip)
        self.pb_add.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Add</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pb_add.setText("")
#if QT_CONFIG(tooltip)
        self.pb_clear.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Clear</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pb_clear.setText("")
#if QT_CONFIG(tooltip)
        self.pb_download.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Download</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pb_download.setText("")
        self.gb_args.setTitle(QCoreApplication.translate("MainWindow", u"Arguments", None))
        self.lb_link.setText(QCoreApplication.translate("MainWindow", u"Link", None))
        self.lb_path.setText(QCoreApplication.translate("MainWindow", u"Path", None))
        self.tb_path.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.lb_format.setText(QCoreApplication.translate("MainWindow", u"Format", None))
        self.le_link.setPlaceholderText(QCoreApplication.translate("MainWindow", u"https://www.youtube.com/watch?v=dQw4w9WgXcQ", None))
        self.dd_format.setItemText(0, QCoreApplication.translate("MainWindow", u"best", None))
        self.dd_format.setItemText(1, QCoreApplication.translate("MainWindow", u"mp4", None))
        self.dd_format.setItemText(2, QCoreApplication.translate("MainWindow", u"mp3", None))
        self.dd_format.setItemText(3, QCoreApplication.translate("MainWindow", u"wav", None))
        self.dd_format.setItemText(4, QCoreApplication.translate("MainWindow", u"flac", None))

        self.gb_embeds.setTitle(QCoreApplication.translate("MainWindow", u"Optional", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"SponsorBlock", None))
        self.pb_save_preset.setText(QCoreApplication.translate("MainWindow", u"Save Preset", None))
        self.lb_presets.setText(QCoreApplication.translate("MainWindow", u"Presets", None))
        self.lb_filename.setText(QCoreApplication.translate("MainWindow", u"Filename", None))
        self.dd_presets.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))

#if QT_CONFIG(tooltip)
        self.dd_presets.setToolTip(QCoreApplication.translate("MainWindow", u"Select a preset or use custom args", None))
#endif // QT_CONFIG(tooltip)
        self.pb_delete_preset.setText(QCoreApplication.translate("MainWindow", u"Delete Preset", None))
        self.lb_cargs.setText(QCoreApplication.translate("MainWindow", u"Custom Args", None))
        self.dd_sponsorblock.setItemText(0, "")
        self.dd_sponsorblock.setItemText(1, QCoreApplication.translate("MainWindow", u"remove", None))
        self.dd_sponsorblock.setItemText(2, QCoreApplication.translate("MainWindow", u"mark", None))

        self.le_preset_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter preset name", None))
        self.cb_thumbnail.setText(QCoreApplication.translate("MainWindow", u"Thumbnail", None))
        self.cb_metadata.setText(QCoreApplication.translate("MainWindow", u"Metadata", None))
        self.cb_subtitles.setText(QCoreApplication.translate("MainWindow", u"Subtitles", None))
        self.le_filename.setPlaceholderText(QCoreApplication.translate("MainWindow", u"%(title)s.%(ext)s", None))
        self.cb_chapters.setText(QCoreApplication.translate("MainWindow", u"Split Chapters", None))
    # retranslateUi

