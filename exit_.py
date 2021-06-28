from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys
import random
import login_


class ExitWindow(QWidget):
    answer = False
    def __init__(self, text, main=None):
        self.text = text
        self.main = main
        QWidget.__init__(self)
        self.setWindowIcon(QIcon('tokidoki.ico'))
        cursor = QIcon(f'./images/cursor{str(random.choice([1, 2, 3, 4, 5, 6]))}.png')
        pixmap = cursor.pixmap(100, QIcon.Active, QIcon.On)
        self.setCursor(QCursor(pixmap, hotX=31, hotY=50))
        self.setWindowTitle('Exit')
        self.setFixedSize(700, 440)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowModality(Qt.ApplicationModal)
        self.v_layout = QVBoxLayout()
        self.setLayout(self.v_layout)
        self.v_layout.setContentsMargins(0, 0, 0, 0)
        self.v_layout.setSpacing(0)
        self.header = QWidget()
        self.header.setObjectName('header')
        self.body = QWidget()
        self.body.setObjectName('body')
        self.footer = QWidget()
        self.footer.setObjectName('footer')
        self.setup_header()
        self.setup_body()
        self.setup_footer()
        self.setStyleSheet(u'QWidget#header{background-color: rgb(24, 23, 27); border-top-left-radius: 5px; border-top-right-radius: 5px;}\n'
            u'QPushButton#x_button{border: none; background: none; color: white; border-top-right-radius: 5px;}\n'
            u'QPushButton#mini_button{border: none; background: none; color: white;}\n'
            u'QPushButton#x_button:hover{background: rgba(230, 0, 0, 200);}\n'
            u'QPushButton#mini_button:hover{background: rgba(38, 37, 43, 1);}\n'
            u'QWidget#body{background-color: rgba(24, 23, 27, 1);}\n'
            u'QLabel#text_1{color: white;}\n'
            u'QPushButton#exit_button{color: rgb(222, 202, 176); background-color: rgb(57, 59, 64); border-radius: 5px;}\n'
            u'QPushButton#exit_button:hover{background-color: rgb(74, 77, 84);}\n'
            u'QPushButton#cancel_button{color: rgb(222, 202, 176); border-radius: 5px; border: 1px solid gray;}\n'
            u'QPushButton#cancel_button:hover{background-color: rgba(227, 227, 227, 1);}'
            u'QWidget#footer{background: white; border-bottom-left-radius: 10px; border-bottom-right-radius: 10px;}\n')
        self.show()

    def setup_header(self):
        font_header = QFont('Roboto', 12, QFont.Bold)
        x_button = QPushButton('X', self.header)
        x_button.setFont(font_header)
        minimize_button = QPushButton('-', self.header)
        minimize_button.setFont(font_header)
        x_button.setGeometry(660, 0, 40, 30)
        minimize_button.setGeometry(620, 0, 40, 30)
        self.header.setMaximumHeight(32)
        x_button.setObjectName('x_button')
        minimize_button.setObjectName('mini_button')
        x_button.clicked.connect(self.cancel)
        minimize_button.clicked.connect(self.mini)
        self.header.mousePressEvent = self.pressed_mouse
        self.header.mouseMoveEvent = self.move_mouse
        self.v_layout.addWidget(self.header)
    
    def setup_body(self):
        font_body = QFont('Roboto Condensed', 20, QFont.Bold)
        text_1 = QLabel(f'Do You Want to {self.text}?', self.body)
        text_1.setFont(font_body)
        image = QIcon('images/cute_armber.png')
        pixmap = image.pixmap(350, QIcon.Active, QIcon.On)
        image_container = QLabel(self.body)
        image_container.setPixmap(pixmap)
        text_1.move(30, 100)
        image_container.move(350, 40)
        text_1.setObjectName('text_1')
        image_container.setObjectName('image_container')
        self.v_layout.addWidget(self.body)

    def setup_footer(self):
        font_footer = QFont('Roboto Condensed', 14, QFont.Bold)
        cancel_button = QPushButton('Cancel', self.footer)
        exit_button = QPushButton(self.text, self.footer)
        exit_button.setFont(font_footer)
        cancel_button.setFont(font_footer)
        cancel_button.setGeometry(82.5, 15, 260, 50)
        exit_button.setGeometry(357.5, 15, 260, 50)
        exit_button.setObjectName('exit_button')
        cancel_button.setObjectName('cancel_button')
        exit_button.clicked.connect(self.exit)
        cancel_button.clicked.connect(self.cancel)
        self.footer.setMaximumHeight(80)
        self.v_layout.addWidget(self.footer)

    def cancel(self):
        self.close()

    def exit(self):
        if self.text == 'Exit':
            sys.exit(1)
        if self.text == 'Delete':
            self.answer = True
            self.close()
        else:
            self.l = login_.Window_()
            self.main.close()
            self.close()
            self.l.show()

    def pressed_mouse(self, event):
        self.old_pos = event.globalPos()

    def move_mouse(self, event):
        delta = self.old_pos - self.pos()
        self.move(event.globalPos().x() - delta.x(), event.globalPos().y() - delta.y())
        self.old_pos = event.globalPos()

    def mini(self):
        self.setWindowState(Qt.WindowMinimized)
