# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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

class Ui_mw_Main(object):
    def setupUi(self, mw_Main):
        if not mw_Main.objectName():
            mw_Main.setObjectName(u"mw_Main")
        mw_Main.resize(841, 622)
        icon = QIcon()
        icon.addFile(u":/icon/yt-dlp-gui.ico", QSize(), QIcon.Normal, QIcon.Off)
        mw_Main.setWindowIcon(icon)
        self.centralwidget = QWidget(mw_Main)
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
        icon1.addFile(u":/buttons/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_add.setIcon(icon1)
        self.pb_add.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.pb_add)

        self.pb_clear = QPushButton(self.gb_controls)
        self.pb_clear.setObjectName(u"pb_clear")
        icon2 = QIcon()
        icon2.addFile(u":/buttons/clear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_clear.setIcon(icon2)
        self.pb_clear.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.pb_clear)

        self.pb_download = QPushButton(self.gb_controls)
        self.pb_download.setObjectName(u"pb_download")
        icon3 = QIcon()
        icon3.addFile(u":/buttons/download.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_download.setIcon(icon3)
        self.pb_download.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.pb_download)


        self.gridLayout.addWidget(self.gb_controls, 0, 2, 1, 1)

        self.gb_embeds = QGroupBox(self.centralwidget)
        self.gb_embeds.setObjectName(u"gb_embeds")
        self.gb_embeds.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gb_embeds.setFlat(False)
        self.gb_embeds.setCheckable(False)
        self.gridLayout_2 = QGridLayout(self.gb_embeds)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.le_cargs = QLineEdit(self.gb_embeds)
        self.le_cargs.setObjectName(u"le_cargs")

        self.gridLayout_2.addWidget(self.le_cargs, 1, 1, 1, 2)

        self.cb_thumbnail = QCheckBox(self.gb_embeds)
        self.cb_thumbnail.setObjectName(u"cb_thumbnail")

        self.gridLayout_2.addWidget(self.cb_thumbnail, 1, 3, 1, 1)

        self.dd_sponsorblock = QComboBox(self.gb_embeds)
        self.dd_sponsorblock.addItem("")
        self.dd_sponsorblock.addItem("")
        self.dd_sponsorblock.addItem("")
        self.dd_sponsorblock.setObjectName(u"dd_sponsorblock")

        self.gridLayout_2.addWidget(self.dd_sponsorblock, 2, 1, 1, 1)

        self.lb_cargs = QLabel(self.gb_embeds)
        self.lb_cargs.setObjectName(u"lb_cargs")

        self.gridLayout_2.addWidget(self.lb_cargs, 1, 0, 1, 1)

        self.cb_subtitles = QCheckBox(self.gb_embeds)
        self.cb_subtitles.setObjectName(u"cb_subtitles")

        self.gridLayout_2.addWidget(self.cb_subtitles, 2, 3, 1, 1)

        self.cb_metadata = QCheckBox(self.gb_embeds)
        self.cb_metadata.setObjectName(u"cb_metadata")

        self.gridLayout_2.addWidget(self.cb_metadata, 0, 3, 1, 1)

        self.le_filename = QLineEdit(self.gb_embeds)
        self.le_filename.setObjectName(u"le_filename")

        self.gridLayout_2.addWidget(self.le_filename, 0, 1, 1, 2)

        self.lb_filename = QLabel(self.gb_embeds)
        self.lb_filename.setObjectName(u"lb_filename")

        self.gridLayout_2.addWidget(self.lb_filename, 0, 0, 1, 1)

        self.label = QLabel(self.gb_embeds)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)


        self.gridLayout.addWidget(self.gb_embeds, 0, 1, 1, 1)

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

        self.gridLayout_4.addWidget(self.le_link, 0, 1, 1, 3)

        self.dd_format = QComboBox(self.gb_args)
        self.dd_format.addItem("")
        self.dd_format.addItem("")
        self.dd_format.addItem("")
        self.dd_format.addItem("")
        self.dd_format.setObjectName(u"dd_format")
        self.dd_format.setMinimumSize(QSize(0, 0))

        self.gridLayout_4.addWidget(self.dd_format, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(219, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 2, 2, 1, 2)


        self.gridLayout.addWidget(self.gb_args, 0, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 2)
        self.gridLayout.setRowStretch(1, 5)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        mw_Main.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(mw_Main)
        self.statusBar.setObjectName(u"statusBar")
        mw_Main.setStatusBar(self.statusBar)
        QWidget.setTabOrder(self.le_path, self.pb_add)
        QWidget.setTabOrder(self.pb_add, self.pb_clear)
        QWidget.setTabOrder(self.pb_clear, self.pb_download)
        QWidget.setTabOrder(self.pb_download, self.tw)

        self.retranslateUi(mw_Main)

        QMetaObject.connectSlotsByName(mw_Main)
    # setupUi

    def retranslateUi(self, mw_Main):
        mw_Main.setWindowTitle(QCoreApplication.translate("mw_Main", u"yt-dlp-gui", None))
        self.gb_status.setTitle(QCoreApplication.translate("mw_Main", u"Status", None))
        ___qtreewidgetitem = self.tw.headerItem()
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("mw_Main", u"ETA", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("mw_Main", u"Speed", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("mw_Main", u"Status", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("mw_Main", u"Progress", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("mw_Main", u"Size", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("mw_Main", u"Format", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("mw_Main", u"Title", None));
        self.gb_controls.setTitle(QCoreApplication.translate("mw_Main", u"Controls", None))
#if QT_CONFIG(tooltip)
        self.pb_add.setToolTip(QCoreApplication.translate("mw_Main", u"<html><head/><body><p>Add</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pb_add.setText("")
#if QT_CONFIG(tooltip)
        self.pb_clear.setToolTip(QCoreApplication.translate("mw_Main", u"<html><head/><body><p>Clear</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pb_clear.setText("")
#if QT_CONFIG(tooltip)
        self.pb_download.setToolTip(QCoreApplication.translate("mw_Main", u"<html><head/><body><p>Download</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pb_download.setText("")
        self.gb_embeds.setTitle(QCoreApplication.translate("mw_Main", u"Optional", None))
        self.cb_thumbnail.setText(QCoreApplication.translate("mw_Main", u"Thumbnail", None))
        self.dd_sponsorblock.setItemText(0, "")
        self.dd_sponsorblock.setItemText(1, QCoreApplication.translate("mw_Main", u"remove", None))
        self.dd_sponsorblock.setItemText(2, QCoreApplication.translate("mw_Main", u"mark", None))

        self.lb_cargs.setText(QCoreApplication.translate("mw_Main", u"Custom Args", None))
        self.cb_subtitles.setText(QCoreApplication.translate("mw_Main", u"Subtitles", None))
        self.cb_metadata.setText(QCoreApplication.translate("mw_Main", u"Metadata", None))
        self.le_filename.setPlaceholderText(QCoreApplication.translate("mw_Main", u"%(title)s.%(ext)s", None))
        self.lb_filename.setText(QCoreApplication.translate("mw_Main", u"Filename", None))
        self.label.setText(QCoreApplication.translate("mw_Main", u"SponsorBlock", None))
        self.gb_args.setTitle(QCoreApplication.translate("mw_Main", u"Arguments", None))
        self.lb_link.setText(QCoreApplication.translate("mw_Main", u"Link", None))
        self.lb_path.setText(QCoreApplication.translate("mw_Main", u"Path", None))
        self.tb_path.setText(QCoreApplication.translate("mw_Main", u"...", None))
        self.lb_format.setText(QCoreApplication.translate("mw_Main", u"Format", None))
        self.le_link.setPlaceholderText(QCoreApplication.translate("mw_Main", u"https://www.youtube.com/watch?v=dQw4w9WgXcQ", None))
        self.dd_format.setItemText(0, QCoreApplication.translate("mw_Main", u"mp4", None))
        self.dd_format.setItemText(1, QCoreApplication.translate("mw_Main", u"mp3", None))
        self.dd_format.setItemText(2, QCoreApplication.translate("mw_Main", u"wav", None))
        self.dd_format.setItemText(3, QCoreApplication.translate("mw_Main", u"flac", None))

    # retranslateUi

