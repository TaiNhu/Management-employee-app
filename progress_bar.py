from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys


class ProgressBar(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 400)
        self.layout = QVBoxLayout()
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet('color: white; font-size: 30px; border: 5px solid rgb(45, 45, 45); background-color: cyan; border-radius: 140px; font-weight: bold; ')
        self.label.setGeometry((self.width() / 2) - 140, (self.height() / 2) - 140, 280, 280)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.value = 0
        self.label_loading = QLabel('Loading...', self)
        self.label_loading.setStyleSheet('color: rgba(68, 0, 62, 1); font-size: 15px; font-weight: bold;')
        self.label_loading.setGeometry(167.5, 220, 55, 20)
        self.label_app = QLabel('Manager App', self)
        self.label_app.setStyleSheet('color: rgba(68, 0, 62, 1); font-size: 22px; font-weight: bold; border-radius: 17px; background: rgba(0, 214, 221, 1);')
        self.label_app.setAlignment(Qt.AlignCenter)
        self.label_app.setGeometry((self.width() - 170) / 2, (self.height() / 2) - 60, 170, 35)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(QColor(178, 248, 250), 12))
        painter.begin(self)
        painter.setRenderHint(painter.Antialiasing)
        painter.drawArc((self.width() / 2) - 150, (self.height() / 2) - 150, 300, 300, -90*16, -self.value*3.6*16)
        self.label.setText(str(self.value)+'%')
        painter.end()

    def update_value(self, value):
        self.value = value
        self.repaint()

    def loading(self):
        width = self.label_loading.width()
        if width >= 68:
            width = 55
        else:
            width += 1
        self.label_loading.setFixedWidth(width)
