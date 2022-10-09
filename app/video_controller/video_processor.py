"""The AbstractVideoThread allows clients to processes cv2 video frames from whatever
source they choose to implement."""
import sys

from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QImage

from abc import ABC, abstractmethod


class InternalAbstractVideoThread(QThread):
    updateFrame = Signal(QImage)
    
    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.c = 0
        self.parent = parent
        
        self.status = True
        self.cap = True

    def run(self) -> None:
        while self.status:
            display_frame = self.get_display_frame()
            if display_frame:     
                self.updateFrame.emit(display_frame)
        sys.exit(-1)

    @abstractmethod
    def get_display_frame(self) -> QImage:
        """Get Display Frame interacts with whatever source the video
        source is and processes the frame into a QImage."""
        pass
