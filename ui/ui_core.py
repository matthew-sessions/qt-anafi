# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'core.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(877, 713)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 12, -1, -1)
        self.topBar = QWidget(self.widget)
        self.topBar.setObjectName(u"topBar")
        self.topBar.setMaximumSize(QSize(16777215, 110))
        self.horizontalLayout_3 = QHBoxLayout(self.topBar)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.toggleContainer = QFrame(self.topBar)
        self.toggleContainer.setObjectName(u"toggleContainer")
        self.toggleContainer.setMaximumSize(QSize(60, 60))
        self.toggleContainer.setStyleSheet(u"border-color: rgba(255, 255, 255, 0);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.toggleContainer.setFrameShape(QFrame.StyledPanel)
        self.toggleContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.toggleContainer)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.menuToggleButton = QPushButton(self.toggleContainer)
        self.menuToggleButton.setObjectName(u"menuToggleButton")
        self.menuToggleButton.setMaximumSize(QSize(60, 60))
        font = QFont()
        font.setKerning(True)
        self.menuToggleButton.setFont(font)
        self.menuToggleButton.setFocusPolicy(Qt.TabFocus)
        self.menuToggleButton.setStyleSheet(u"background-color: rgba(0, 0, 0, 128);\n"
"border-radius: 6;")
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu-button-of-three-horizontal-lines.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuToggleButton.setIcon(icon)
        self.menuToggleButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.menuToggleButton)


        self.horizontalLayout_3.addWidget(self.toggleContainer)

        self.frame_2 = QFrame(self.topBar)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_2)

        self.angleContainer = QFrame(self.topBar)
        self.angleContainer.setObjectName(u"angleContainer")
        self.angleContainer.setMaximumSize(QSize(110, 16777215))
        self.angleContainer.setStyleSheet(u"background-color: rgba(0, 0, 0, 128);\n"
"border-radius: 6;\n"
"color: rgb(255, 255, 255)")
        self.angleContainer.setFrameShape(QFrame.StyledPanel)
        self.angleContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.angleContainer)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, -1, 12)
        self.angleText_2 = QLabel(self.angleContainer)
        self.angleText_2.setObjectName(u"angleText_2")
        font1 = QFont()
        font1.setFamilies([u"Muli"])
        font1.setPointSize(15)
        font1.setKerning(True)
        self.angleText_2.setFont(font1)
        self.angleText_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.angleText_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.angleText_2)

        self.angleText = QLabel(self.angleContainer)
        self.angleText.setObjectName(u"angleText")
        self.angleText.setFont(font1)
        self.angleText.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.angleText.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.angleText)


        self.horizontalLayout_3.addWidget(self.angleContainer)

        self.heightFrame = QFrame(self.topBar)
        self.heightFrame.setObjectName(u"heightFrame")
        self.heightFrame.setMaximumSize(QSize(145, 16777215))
        self.heightFrame.setStyleSheet(u"background-color: rgba(0, 0, 0, 128);\n"
"border-radius: 6;\n"
"color: rgb(255, 255, 255)")
        self.heightFrame.setFrameShape(QFrame.StyledPanel)
        self.heightFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.heightFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(12, 25, -1, 12)
        self.heightCurrent = QLabel(self.heightFrame)
        self.heightCurrent.setObjectName(u"heightCurrent")
        font2 = QFont()
        font2.setFamilies([u"Muli"])
        font2.setPointSize(23)
        font2.setKerning(True)
        self.heightCurrent.setFont(font2)
        self.heightCurrent.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.heightCurrent.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.heightCurrent)

        self.heightText = QLabel(self.heightFrame)
        self.heightText.setObjectName(u"heightText")
        font3 = QFont()
        font3.setFamilies([u"Muli"])
        font3.setPointSize(18)
        font3.setKerning(True)
        self.heightText.setFont(font3)
        self.heightText.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.heightText.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.heightText)


        self.horizontalLayout_3.addWidget(self.heightFrame)


        self.verticalLayout.addWidget(self.topBar)

        self.coreWidget = QWidget(self.widget)
        self.coreWidget.setObjectName(u"coreWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.coreWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menuContainer = QWidget(self.coreWidget)
        self.menuContainer.setObjectName(u"menuContainer")
        self.menuContainer.setMaximumSize(QSize(60, 16777215))
        self.menuContainer.setStyleSheet(u"background-color: rgba(0, 0, 0, 128);\n"
"border-radius: 6;")
        self.verticalLayout_3 = QVBoxLayout(self.menuContainer)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.homeButton = QPushButton(self.menuContainer)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setMaximumSize(QSize(16777215, 58))
        self.homeButton.setStyleSheet(u"background-color: rgba(0, 0, 0, 70)")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/bird.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homeButton.setIcon(icon1)
        self.homeButton.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.homeButton)

        self.pushButton = QPushButton(self.menuContainer)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(16777215, 58))
        self.pushButton.setStyleSheet(u"background-color: rgba(255, 255, 255, 0)")
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(35, 35))

        self.verticalLayout_3.addWidget(self.pushButton)

        self.menuSpacer = QFrame(self.menuContainer)
        self.menuSpacer.setObjectName(u"menuSpacer")
        self.menuSpacer.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.menuSpacer.setFrameShape(QFrame.StyledPanel)
        self.menuSpacer.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.menuSpacer)


        self.horizontalLayout_2.addWidget(self.menuContainer)

        self.coreContainer = QWidget(self.coreWidget)
        self.coreContainer.setObjectName(u"coreContainer")

        self.horizontalLayout_2.addWidget(self.coreContainer)

        self.rightContainer = QWidget(self.coreWidget)
        self.rightContainer.setObjectName(u"rightContainer")
        self.rightContainer.setMaximumSize(QSize(60, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.rightContainer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.truckLandingButton = QPushButton(self.rightContainer)
        self.truckLandingButton.setObjectName(u"truckLandingButton")
        self.truckLandingButton.setMaximumSize(QSize(16777215, 60))
        font4 = QFont()
        font4.setFamilies([u"Muli"])
        font4.setPointSize(17)
        font4.setKerning(True)
        self.truckLandingButton.setFont(font4)
        self.truckLandingButton.setLayoutDirection(Qt.LeftToRight)
        self.truckLandingButton.setStyleSheet(u"background-color: rgba(0, 0, 0, 128);\n"
"border-radius: 6;\n"
"color: rgb(255, 255, 255)")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/pickup-truck.png", QSize(), QIcon.Normal, QIcon.Off)
        self.truckLandingButton.setIcon(icon2)
        self.truckLandingButton.setIconSize(QSize(45, 45))

        self.verticalLayout_2.addWidget(self.truckLandingButton)

        self.takePicture4kButton = QPushButton(self.rightContainer)
        self.takePicture4kButton.setObjectName(u"takePicture4kButton")
        self.takePicture4kButton.setMaximumSize(QSize(16777215, 60))
        self.takePicture4kButton.setFont(font4)
        self.takePicture4kButton.setLayoutDirection(Qt.LeftToRight)
        self.takePicture4kButton.setStyleSheet(u"background-color: rgba(0, 0, 0, 128);\n"
"border-radius: 6;\n"
"color: rgb(255, 255, 255)")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/camera.png", QSize(), QIcon.Normal, QIcon.Off)
        self.takePicture4kButton.setIcon(icon3)
        self.takePicture4kButton.setIconSize(QSize(28, 28))

        self.verticalLayout_2.addWidget(self.takePicture4kButton)

        self.spacer = QFrame(self.rightContainer)
        self.spacer.setObjectName(u"spacer")
        self.spacer.setFrameShape(QFrame.StyledPanel)
        self.spacer.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.spacer)

        self.takeoffLandButton = QPushButton(self.rightContainer)
        self.takeoffLandButton.setObjectName(u"takeoffLandButton")
        self.takeoffLandButton.setMaximumSize(QSize(16777215, 60))
        self.takeoffLandButton.setFont(font4)
        self.takeoffLandButton.setLayoutDirection(Qt.LeftToRight)
        self.takeoffLandButton.setStyleSheet(u"background-color: rgba(0, 84, 0, 145);\n"
"border-radius: 6;\n"
"color: rgb(255, 255, 255)")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/propeller.png", QSize(), QIcon.Normal, QIcon.Off)
        self.takeoffLandButton.setIcon(icon4)
        self.takeoffLandButton.setIconSize(QSize(28, 28))

        self.verticalLayout_2.addWidget(self.takeoffLandButton)


        self.horizontalLayout_2.addWidget(self.rightContainer)


        self.verticalLayout.addWidget(self.coreWidget)


        self.horizontalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuToggleButton.setText("")
        self.angleText_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.angleText.setText(QCoreApplication.translate("MainWindow", u"Cam Angle", None))
        self.heightCurrent.setText(QCoreApplication.translate("MainWindow", u"-- ft", None))
        self.heightText.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.homeButton.setText("")
        self.pushButton.setText("")
        self.truckLandingButton.setText("")
        self.takePicture4kButton.setText("")
        self.takeoffLandButton.setText("")
    # retranslateUi

