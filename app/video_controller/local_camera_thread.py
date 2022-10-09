
from turtle import width
from video_controller.video_processor import InternalAbstractVideoThread

from PySide6.QtCore import Qt
from PySide6.QtGui import QImage
import cv2

class LocalCameraThread(InternalAbstractVideoThread):
    def __init__(self, parent=None):

        super().__init__(parent)
        self.cap = None

    def get_display_frame(self) -> QImage:
        if not self.cap:
            self.cap = cv2.VideoCapture(0)
        ret, frame = self.cap.read()        
        if not ret:
            return

        color_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        


        h, w, ch = color_frame.shape
        img = QImage(color_frame.data, w, h, ch * w, QImage.Format_RGB888)
        sizes = self.parent.frameSize()
        width = sizes.width()
        height = sizes.height()
        return img.scaled(width, height, Qt.KeepAspectRatio)

