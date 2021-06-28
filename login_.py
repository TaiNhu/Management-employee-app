from PySide6.QtWidgets import *
import sys
from PySide6.QtGui import *
from PySide6.QtCore import *
import progress_bar
import exit_
import registration
from data import *
import main
import random
import time


class Window_(QWidget):
    _answer = [None, None]

    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('tokidoki.ico'))
        self.setup_window()

    def setup_window(self):
        cursor = QIcon(f'./images/cursor{str(random.choice([1, 2, 3, 4, 5, 6]))}.png')
        self.pixmap = cursor.pixmap(100, QIcon.Active, QIcon.On)
        self.setCursor(QCursor(self.pixmap, hotX=31, hotY=50))
        self.setFixedSize(450, 500)
        self.setStyleSheet('outline: 0;')
        self.setFocusPolicy(Qt.ClickFocus)
        self.setWindowTitle('Login')
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet(u'QLabel#window{border-radius: 20;}\n'
                           u'QLineEdit{background-color: rgb(28, 0, 62); border:none; border-bottom: 1px solid cyan; color: white;}\n'
                           u'QCheckBox{color: white;}\n'
                           u'QPushButton#login_btn{background-color: cyan; border-radius: 10; border: none;}\n'
                           u'QPushButton#login_btn:hover{font-weight: bold;}\n'
                           u'QPushButton#login_btn:pressed{padding-top: 5px; padding-left: 5px;}\n'
                           u'QPushButton#registration_btn{border: none; background-color: none; color: cyan;}\n'
                           u'QPushButton#registration_btn:hover{text-decoration: underline;}\n'
                           u'QLabel#message{color: red;}\n')
        self.label = QLabel(self)
        self.message = QLabel(self)
        self.message.setObjectName('message')
        self.label.setObjectName('window')
        self.label.setGeometry(0, 0, 450, 500)
        self.label.setStyleSheet(u'QLabel{background-color: rgb(28, 0, 62);}\n')

        self.label_2 = QLabel(self)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setGeometry(0, 0, 450, 160)
        icon = QIcon('images/employee.png')
        pixmap = icon.pixmap(450, QIcon.Active, QIcon.On)
        self.label_2.setPixmap(pixmap)
        self.line_user = QLineEdit(self)
        self.line_user.setGeometry(75, 180, 300, 30)
        self.line_user.setPlaceholderText(' User Name')
        font_login = QFont()
        font_login.setPointSize(12)
        self.line_user.setFont(font_login)
        self.line_pass = QLineEdit(self)
        self.line_pass.setFont(font_login)
        self.line_pass.setPlaceholderText(' Password')
        self.line_pass.setGeometry(75, 250, 300, 30)
        self.message.setGeometry(75, 290, 375, 20)
        self.line_pass.setEchoMode(QLineEdit.Password)
        self.show_pass_btn = QCheckBox('Show Password', self)
        self.show_pass_btn.setGeometry(75, 310, 131, 20)
        self.show_pass_btn.setFont(QFont('Roboto', 9))
        self.show_pass_btn.stateChanged.connect(self.show_pass)
        font_btn = QFont('Roboto', 10)
        self.login_btn = QPushButton('L o g  I n', self)
        self.login_btn.setFocusPolicy(Qt.NoFocus)
        self.login_btn.setShortcut(QKeySequence(Qt.Key_Return))
        self.login_btn.setObjectName('login_btn')
        self.registration_btn = QPushButton('R e g i s t r a t i o n', self)
        self.registration_btn.setFocusPolicy(Qt.NoFocus)
        self.registration_btn.setObjectName('registration_btn')
        self.exit_button = QPushButton('E x i t', self)
        self.exit_button.setCursor(Qt.PointingHandCursor)
        self.exit_button.setFocusPolicy(Qt.NoFocus)
        self.exit_button.setObjectName('registration_btn')
        self.login_btn.setGeometry(180, 360, 90, 30)
        self.login_btn.setFont(font_btn)
        self.exit_button.setFont(font_btn)
        self.registration_btn.setFont(font_btn)
        self.registration_btn.setGeometry(150, 400, 151, 30)
        self.exit_button.setGeometry(200, 440, 51, 30)
        self.exit_button.clicked.connect(self.exit_)
        self.registration_btn.clicked.connect(self.registration_window)
        self.login_btn.clicked.connect(self.login_event)
        self.loading_label = QLabel(self)
        self.loading_text = QLabel('Loading...', self)
        self.loading_text.hide()
        self.loading_text.setStyleSheet(
            '''QLabel{
                font-size:18px;
                color: purple;
                font-weight: bold;
            }'''
        )
        self.loading_text.setGeometry(185, 230, 67, 40)
        op = QGraphicsOpacityEffect(self.loading_label)
        op.setOpacity(0.1)
        self.loading_label.setStyleSheet('''
        QLabel{
        background-color: white;
        border-radius: 20px;}''')
        self.loading_label.setGraphicsEffect(op)
        self.loading_label.setAlignment(Qt.AlignCenter)
        self.loading_label.setGeometry(0, 0, 450, 500)
        self.loading_label.hide()

    def show_pass(self, state):
        if state == Qt.Checked:
            self.line_pass.setEchoMode(QLineEdit.Normal)
        else:
            self.line_pass.setEchoMode(QLineEdit.Password)

    def mousePressEvent(self, event):
        self.setCursor(Qt.ClosedHandCursor)
        self.old_pos = event.globalPos()

    def mouseReleaseEvent(self, event):
        self.setCursor(QCursor(self.pixmap, hotX=31, hotY=50))

    def mouseMoveEvent(self, event):
        delta = self.old_pos - self.pos()
        self.move(event.globalPos().x() - delta.x(), event.globalPos().y() - delta.y())
        self.old_pos = event.globalPos()

    def exit_(self):
        self.e = exit_.ExitWindow('Exit')

    def registration_window(self):
        self.registration_window = registration.RegistrationWindow()
        self.registration_window.show()
        self.close()

    def login_event(self):
        self.worker = QThread(self)
        self.worker.run = self.login_process
        self.worker.start()
        timeout = time.time()
        self.timer = QTimer()
        self.timer.timeout.connect(self._update)
        self.timer.timeout.connect(lambda: self.loading(timeout))
        self.timer.start(15)

    def change_color_message(self, color):
        self.message.setStyleSheet(f'''
        QLabel#message{{
        color: {color};
        }}''')

    def login_process(self):
        message = login_validate(self.line_user.text(), self.line_pass.text())
        self._answer = list(message)

    def loading(self, timeout):
        self.loading_label.setHidden(False)
        self.loading_text.setHidden(False)
        if time.time() - timeout > 5:
            self.worker.quit()
            self.timer.stop()
            self.loading_label.hide()
            self.loading_text.hide()
            self.change_color_message('cyan')
            self.message.setText('Server connection timeout')
        if self._answer[0]:
            self.worker.quit()
            self.timer.stop()
            self.main = main.MainWindow(hash_user_name(self.line_user.text()), self._answer[1])
            self.main.show()
            self.close()
        elif not self._answer[0] is None:
            self.worker.quit()
            self.timer.stop()
            self.loading_label.hide()
            self.loading_text.hide()
            self.change_color_message('red')
            self.message.setText('Incorrect')
        self._answer[0] = None

    def _update(self):
        if self.loading_text.width() < 85:
            self.loading_text.setFixedWidth(self.loading_text.width() + 1)
        else:
            self.loading_text.setFixedWidth(67)


class ProgressBar(progress_bar.ProgressBar):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('tokidoki.ico'))
        self.show()
        self.timer = QTimer()
        self.timer.timeout.connect(self._update)
        self.timer.timeout.connect(self.loading)
        self.timer.start(15)

    def _update(self):
        if self.value >= 100:
            self.timer.stop()
            self.m = Window_()
            self.m.show()
            self.close()
        else:
            self.value += 1
            self.update_value(self.value)


def run1():
    app = QApplication(sys.argv)
    _window = ProgressBar()
    _window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    run1()
