# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(420, 706)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(140, 70, 261, 31))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.startIndex = QPushButton(self.layoutWidget)
        self.startIndex.setObjectName(u"startIndex")

        self.horizontalLayout.addWidget(self.startIndex)

        self.stopIndex = QPushButton(self.layoutWidget)
        self.stopIndex.setObjectName(u"stopIndex")

        self.horizontalLayout.addWidget(self.stopIndex)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 48, 21))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 150, 48, 21))
        self.startIndex_2 = QPushButton(self.centralwidget)
        self.startIndex_2.setObjectName(u"startIndex_2")
        self.startIndex_2.setGeometry(QRect(20, 180, 381, 24))
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 240, 381, 381))
        self.layoutWidget_2 = QWidget(self.centralwidget)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(20, 210, 381, 26))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.radioButton_7 = QRadioButton(self.layoutWidget_2)
        self.radioButton_7.setObjectName(u"radioButton_7")

        self.horizontalLayout_5.addWidget(self.radioButton_7)

        self.radioButton_3 = QRadioButton(self.layoutWidget_2)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout_5.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.layoutWidget_2)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.horizontalLayout_5.addWidget(self.radioButton_4)

        self.radioButton_6 = QRadioButton(self.layoutWidget_2)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.horizontalLayout_5.addWidget(self.radioButton_6)

        self.radioButton_5 = QRadioButton(self.layoutWidget_2)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.horizontalLayout_5.addWidget(self.radioButton_5)

        self.startIndex_4 = QPushButton(self.layoutWidget_2)
        self.startIndex_4.setObjectName(u"startIndex_4")

        self.horizontalLayout_5.addWidget(self.startIndex_4)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(70, 150, 168, 22))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_3.addWidget(self.label_10)

        self.radioButton = QRadioButton(self.widget)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout_3.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.widget)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_3.addWidget(self.radioButton_2)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(20, 40, 381, 24))
        self.horizontalLayout_4 = QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.lineEdit_Id = QLineEdit(self.widget1)
        self.lineEdit_Id.setObjectName(u"lineEdit_Id")

        self.horizontalLayout_4.addWidget(self.lineEdit_Id)

        self.widget2 = QWidget(self.centralwidget)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(20, 630, 381, 26))
        self.horizontalLayout_6 = QHBoxLayout(self.widget2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.startIndex_3 = QPushButton(self.widget2)
        self.startIndex_3.setObjectName(u"startIndex_3")

        self.horizontalLayout_6.addWidget(self.startIndex_3)

        self.startIndex_5 = QPushButton(self.widget2)
        self.startIndex_5.setObjectName(u"startIndex_5")

        self.horizontalLayout_6.addWidget(self.startIndex_5)

        self.startIndex_6 = QPushButton(self.widget2)
        self.startIndex_6.setObjectName(u"startIndex_6")

        self.horizontalLayout_6.addWidget(self.startIndex_6)

        MainWindow.setCentralWidget(self.centralwidget)
        self.tableWidget.raise_()
        self.label_2.raise_()
        self.lineEdit_Id.raise_()
        self.layoutWidget.raise_()
        self.label.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.radioButton.raise_()
        self.radioButton_2.raise_()
        self.startIndex_2.raise_()
        self.startIndex_3.raise_()
        self.layoutWidget_2.raise_()
        self.startIndex_5.raise_()
        self.startIndex_6.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 420, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.startIndex.clicked.connect(MainWindow.startGoogleIndex)
        self.stopIndex.clicked.connect(MainWindow.stopGoogleIndex)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\uc0c9\uc778\uc790\ub3d9\ud654", None))
        self.startIndex.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uc791", None))
        self.stopIndex.setText(QCoreApplication.translate("MainWindow", u"\uc911\uc9c0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">\uc218\uc9d1</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">\uc0c9\uc778</span></p></body></html>", None))
        self.startIndex_2.setText(QCoreApplication.translate("MainWindow", u"\uc0c9\uc778 \ube0c\ub77c\uc6b0\uc800 \uc5f4\uae30(\ub85c\uadf8\uc778 \ud544\uc218)", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\uc218\uc9d1URL", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\uc0c1\ud0dc", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\uccb4\ud06c", None));
        self.radioButton_7.setText(QCoreApplication.translate("MainWindow", u"\uc804\uccb4", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"\ubbf8\uc0c9\uc778", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"\uc0c9\uc778\uc644\ub8cc", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"\uc5d0\ub7ec", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"\uc81c\uc678", None))
        self.startIndex_4.setText(QCoreApplication.translate("MainWindow", u"\uc0c9\uc778\uc2e4\ud589", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\uc0c9\uc778\uc720\ud615", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\uad6c\uae00", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\ub124\uc774\ubc84", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\ube14\ub85c\uadf8URL", None))
        self.startIndex_3.setText(QCoreApplication.translate("MainWindow", u"\uc0c9\uc778\uc2e4\ud589", None))
        self.startIndex_5.setText(QCoreApplication.translate("MainWindow", u"\uc0ad\uc81c", None))
        self.startIndex_6.setText(QCoreApplication.translate("MainWindow", u"\ubcf5\uc6d0", None))
    # retranslateUi

