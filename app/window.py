
import sys
import time
from PySide6.QtWidgets import QMainWindow, QGraphicsProxyWidget, QGraphicsView, QGraphicsScene, QLabel
from video_controller.local_camera_thread import LocalCameraThread
from ui.ui_core_interface import Ui_MainWindow
# from video_controller.local_camera_thread import LocalCameraThread

import cv2
from PySide6.QtCore import Slot, QSize, QRect
from PySide6.QtGui import QImage,  QPixmap



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        
        self.ui.setupUi(self)
        self.label = QLabel(self)
        self.ui.centralwidget.raise_()
        
        # self.label.setFixedSize(640, 480)

        # Thread in charge of updating the image
        self.th = LocalCameraThread(self)
        self.th.finished.connect(self.close)
        self.th.updateFrame.connect(self.setImage)

        self.ui.menuToggleButton.clicked.connect(self.handle_menu_toggle)
        self.menu_state_open = False

        self.start()

    @Slot()
    def handle_menu_toggle(self):
        if self.menu_state_open:
            self.menu_state_open = False
            self._set_toggle_container_sizes(60)
            self._set_toggle_text()
        else:
            self.menu_state_open = True
            self._set_toggle_container_sizes(250)

    def _set_toggle_container_sizes(self, size: int) -> None:
        self.ui.menuContainer.setMaximumSize(QSize(size, 16777215))
        self.ui.rightContainer.setMaximumSize(QSize(size, 16777215))
        self._set_toggle_text(empty_text = False)

    def _set_toggle_text(self, empty_text: bool = True) -> None:
        self.ui.truckLandingButton.setText("" if empty_text else "Truck-bed landing")
        self.ui.takePicture4kButton.setText("" if empty_text else "Take 4k photo")
        self.ui.homeButton.setText("" if empty_text else "Active Mission")

    @Slot(QImage)
    def setImage(self, image):
        sizes = self.frameSize()
        w = sizes.width()
        h = sizes.height()

     
        self.label.setGeometry(QRect(0, 0, w, h))
        self.label.setPixmap(QPixmap.fromImage(image))

    @Slot()
    def start(self):
        print("Starting...")

        self.th.start()