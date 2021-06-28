from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys
import exit_
import login_
from data import *
import random


class RegistrationWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('tokidoki.ico'))
        cursor = QIcon(f'./images/cursor{str(random.choice([1, 2, 3, 4, 5, 6]))}.png')
        self.pixmap = cursor.pixmap(100, QIcon.Active, QIcon.On)
        self.setCursor(QCursor(self.pixmap, hotX=31, hotY=50))
        self.setWindowTitle('Registration')
        self.setFixedSize(450, 500)
        self.setFocusPolicy(Qt.ClickFocus)
        self.background = QLabel(self)
        self.icon = QLabel(self)
        self.user_name = QLineEdit(self)
        self.password = QLineEdit(self)
        self.rely_password = QLineEdit(self)
        self.message = QLabel(self)
        self.message.setObjectName('message')
        self.submit_button = QPushButton('S u b m i t', self)
        self.login_button = QPushButton('L o g  I n', self)
        self.exit_button = QPushButton('E x i t', self)
        self.setup_background()
        self.setup_icon()
        self.setup_line()
        self.setup_button()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet('QLabel#background{background-color: rgb(28, 0, 62); border-radius: 20px;}\n'
                           'QLineEdit#pass{border:none; border-bottom: 1px solid cyan; background-color: rgb(28, 0, 62); color: white; font-size: 17px; font-family: "Roboto";}\n'
                           'QPushButton#submit{background-color: cyan; border-radius: 10px; font-size: 14px; font-family: "Roboto";}\n'
                           'QPushButton#submit:hover{font-weight: bold;}\n'
                           'QPushButton#submit:pressed{padding-top: 5px; padding-left: 5px;}\n'
                           'QPushButton#login_exit{border:none; background-color: none; color: cyan; font-size: 14px; font-family: "Roboto";}\n'
                           'QPushButton#login_exit:hover{text-decoration: underline;}\n'
                           )

    def setup_background(self):
        self.background.setGeometry(0, 0, 450, 500)
        self.background.setObjectName('background')

    def setup_icon(self):
        image = QIcon('images/employee.png')
        pixmap = image.pixmap(450, QIcon.Active, QIcon.On)
        self.icon.setObjectName('icon')
        self.icon.setAlignment(Qt.AlignCenter)
        self.icon.setPixmap(pixmap)
        self.icon.setGeometry(0, 0, 450, 160)

    def setup_button(self):
        self.submit_button.setShortcut(QKeySequence(Qt.Key_Return))
        self.submit_button.setObjectName('submit')
        self.submit_button.setFocusPolicy(Qt.NoFocus)
        self.login_button.setObjectName('login_exit')
        self.login_button.setFocusPolicy(Qt.NoFocus)
        self.exit_button.setObjectName('login_exit')
        self.exit_button.setCursor(Qt.PointingHandCursor)
        self.exit_button.setFocusPolicy(Qt.NoFocus)
        self.submit_button.setGeometry(180, 350, 90, 30)
        self.login_button.setGeometry(195, 395, 60, 30)
        self.exit_button.setGeometry(205, 430, 40, 30)
        self.exit_button.clicked.connect(self.exit)
        self.login_button.clicked.connect(self.login_window)
        self.submit_button.clicked.connect(self.submit_event)

    def setup_line(self):
        self.user_name.setObjectName('pass')
        self.password.setObjectName('pass')
        self.rely_password.setObjectName('pass')
        self.message.move(75, 320)
        self.user_name.setGeometry(75, 170, 300, 35)
        self.password.setGeometry(75, 225, 300, 35)
        self.rely_password.setGeometry(75, 275, 300, 35)
        self.user_name.setPlaceholderText(' User Name')
        self.password.setPlaceholderText(' Password')
        self.rely_password.setPlaceholderText(' Rely Password')
        self.password.setEchoMode(QLineEdit.Password)
        self.rely_password.setEchoMode(QLineEdit.Password)

    def mousePressEvent(self, event):
        self.setCursor(QCursor(Qt.ClosedHandCursor))
        self.old_pos = event.globalPos()

    def mouseReleaseEvent(self, event):
        self.setCursor(QCursor(self.pixmap, hotX=31, hotY=50))

    def mouseMoveEvent(self, event):
        delta = self.old_pos - self.pos()
        self.move(event.globalPos() - delta)
        self.old_pos = event.globalPos()

    def exit(self):
        self.mw = exit_.ExitWindow('Exit')

    def login_window(self):
        self.login_window = login_.Window_()
        self.login_window.show()
        self.close()

    def submit_event(self):
        message = registration_validate(self.user_name.text(), self.password.text(), self.rely_password.text())
        if message == 1:
            self.change_color('cyan')
            self.message.setText('Registration successfully')
            return self.message.adjustSize()
        elif message == 0:
            self.change_color('red')
            self.message.setText('User name is exist')
            return self.message.adjustSize()
        self.change_color('red')
        self.message.setText('User name must be [A][a-z][0-9] or pass not duplicate')
        return self.message.adjustSize()

    def change_color(self, color):
        self.message.setStyleSheet(f'color: {color};')
