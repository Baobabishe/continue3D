# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_main_window_620_480.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1154, 624)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 1136, 534))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.loadimage = QPushButton(self.layoutWidget)
        self.loadimage.setObjectName(u"loadimage")
        self.loadimage.setMinimumSize(QSize(50, 0))

        self.verticalLayout.addWidget(self.loadimage)

        self.listWidget = QListWidget(self.layoutWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(100, 50))
        self.listWidget.setMaximumSize(QSize(300, 500))

        self.verticalLayout.addWidget(self.listWidget)

        self.loadmark = QPushButton(self.layoutWidget)
        self.loadmark.setObjectName(u"loadmark")

        self.verticalLayout.addWidget(self.loadmark)

        self.listWidget_2 = QListWidget(self.layoutWidget)
        self.listWidget_2.setObjectName(u"listWidget_2")

        self.verticalLayout.addWidget(self.listWidget_2)

        self.loadimagemark = QPushButton(self.layoutWidget)
        self.loadimagemark.setObjectName(u"loadimagemark")

        self.verticalLayout.addWidget(self.loadimagemark)

        self.listWidget_3 = QListWidget(self.layoutWidget)
        self.listWidget_3.setObjectName(u"listWidget_3")

        self.verticalLayout.addWidget(self.listWidget_3)

        self.checkBox = QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout.addWidget(self.checkBox)

        self.pushButton_4 = QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout.addWidget(self.pushButton_4)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.space_for_display_images = QLabel(self.layoutWidget)
        self.space_for_display_images.setObjectName(u"space_for_display_images")
        self.space_for_display_images.setMinimumSize(QSize(640, 480))
        self.space_for_display_images.setMaximumSize(QSize(640, 480))

        self.horizontalLayout_2.addWidget(self.space_for_display_images)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableWidget = QTableWidget(self.layoutWidget)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(240, 0))
        self.tableWidget.setMaximumSize(QSize(240, 16777215))
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.add_row = QPushButton(self.layoutWidget)
        self.add_row.setObjectName(u"add_row")
        self.add_row.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout.addWidget(self.add_row)

        self.delete_row = QPushButton(self.layoutWidget)
        self.delete_row.setObjectName(u"delete_row")
        self.delete_row.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout.addWidget(self.delete_row)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.export_table = QPushButton(self.layoutWidget)
        self.export_table.setObjectName(u"export_table")

        self.verticalLayout_2.addWidget(self.export_table)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1154, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.loadimage.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.loadmark.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0442\u0430\u0431\u043b\u0438\u0446\u0443 \u043c\u0430\u0440\u043a\u0435\u0440\u043e\u0432", None))
        self.loadimagemark.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u043c\u0430\u0440\u043a\u0435\u0440\u043e\u0432", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0443 \u043a\u0430\u043c\u0435\u0440\u044b", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.space_for_display_images.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"X", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Y", None));
        self.add_row.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0441\u0442\u0440\u043e\u043a\u0443", None))
        self.delete_row.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0441\u0442\u0440\u043e\u043a\u0443", None))
        self.export_table.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0442\u0430\u0431\u043b\u0438\u0446\u0443", None))
    # retranslateUi

