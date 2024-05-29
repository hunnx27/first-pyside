# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FirstUi.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextBrowser, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(567, 479)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 561, 51))
        font = QFont()
        font.setFamilies([u"\uad81\uc11c\uccb4"])
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(11, 61, 36, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(11, 113, 48, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(11, 165, 36, 16))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(11, 217, 85, 16))
        self.lineEdit_Id = QLineEdit(self.centralwidget)
        self.lineEdit_Id.setObjectName(u"lineEdit_Id")
        self.lineEdit_Id.setGeometry(QRect(110, 70, 133, 22))
        self.lineEdit_Pw = QLineEdit(self.centralwidget)
        self.lineEdit_Pw.setObjectName(u"lineEdit_Pw")
        self.lineEdit_Pw.setGeometry(QRect(110, 120, 133, 22))
        self.lineEdit_Search = QLineEdit(self.centralwidget)
        self.lineEdit_Search.setObjectName(u"lineEdit_Search")
        self.lineEdit_Search.setGeometry(QRect(110, 170, 133, 22))
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 270, 271, 161))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 250, 48, 16))
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(290, 70, 261, 271))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(290, 50, 36, 16))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(110, 210, 171, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(12)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_4 = QLineEdit(self.widget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_2.addWidget(self.lineEdit_4)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.lineEdit_5 = QLineEdit(self.widget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout_2.addWidget(self.lineEdit_5)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(290, 350, 261, 81))
        self.horizontalLayout = QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.widget1)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget1)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 567, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.start)
        self.pushButton_2.clicked.connect(MainWindow.stop)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def start(self):
        self.textEdit.append('hihihi')
        print('start')
    # start

    def stop(self):
        self.textEdit.append('stop!!')
        print('end')
    # end

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700; color:#000000;\">\uc5c5\ubb34\uc790\ub3d9\ud654 \ub3c4\uc6b0\ubbf8</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\uc544\uc774\ub514", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\ube44\ubc00\ubc88\ud638", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\uac80\uc0c9\uc5b4", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"URL \uc218\uc9d1\ud398\uc774\uc9c0", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\uc791\uc131\ub0b4\uc6a9", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\uc0c1\ud0dc\ucc3d", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"~", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uc791", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\uc911\uc9c0", None))
    # retranslateUi