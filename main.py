from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtWidgets import QFrame
import exit_
from data import *
import exit_
import binascii
import time


class MainWindow(QMainWindow):
    _employee_temp = {}
    _index_of_dict = 0
    result = None

    def __init__(self, user_name=None, avatar=None):
        super().__init__()
        self.s = QRect(0, 0, 0, 0)
        self.avatar = avatar
        self.setWindowIcon(QIcon('tokidoki.ico'))
        self.setStyleSheet('outline: 0;')
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet('''QToolTip{background-color: rgb(32, 34, 37);
        color: white;
        border: 1px solid white;
        font-weight: bold;}''')
        self._user_name = user_name
        self.setWindowTitle('App')
        self.setMinimumSize(QSize(800, 500))
        self.central_widget = QWidget()
        self.central_widget.setObjectName('central')
        self.central_widget.setStyleSheet(
            u'QFrame#header{background-color: rgb(32, 34, 37); border-top-left-radius: 12px;}'
            u'QWidget#central{background-color: rgb(32, 34, 37); border: 3px solid rgb(62, 64, 67); border-radius: 12px;}'
            u'QPushButton#exit_btn{background-color: rgb(32, 34, 37); border:none; color: rgb(132, 138, 150);}'
            u'QPushButton#exit_btn:hover{background-color: rgb(199, 69, 69);}'
            u'QPushButton#minimize_btn{background-color: rgb(32, 34, 37); border:none; color: rgb(132, 138, 150);}'
            u'QPushButton#minimize_btn:hover{background-color: rgb(52, 54, 57);}'
            u'QFrame#body{background-color: rgb(54, 57, 63);}'
            u'QFrame#nav{background-color: rgb(47, 49, 54);}'
            u'QPushButton#new{border: none; background-color: none; color: white; font-weight: bold; background-image: url("./images/new.png"); background-repeat: none; background-position: left; text-align: left; padding-left: 80px;}'
            u'QPushButton#save{border: none; background-color: none; color: white; font-weight: bold; background-image: url("./images/save.png"); background-repeat: none; background-position: left; text-align: left; padding-left: 80px;}'
            u'QPushButton#modify{border: none; background-color: none; color: white; font-weight: bold; background-image: url("./images/modify.png"); background-repeat: none; background-position: left; text-align: left; padding-left: 80px;}'
            u'QPushButton#table{border: none; background-color: none; color: white; font-weight: bold; background-image: url("./images/table.png"); background-repeat: none; background-position: left; text-align: left; padding-left: 80px;}'
            u'QPushButton#setting{border: none; background-color: none; color: white; font-weight: bold; background-image: url("./images/setting.png"); background-repeat: none; background-position: left; text-align: left; padding-left: 80px;}'
            u'QPushButton#logout{border: none; background-color: none; color: white; font-weight: bold; background-image: url("./images/logout.png"); background-repeat: none; background-position: left; text-align: left; padding-left: 80px;}'
            u'QPushButton#new:hover{border-radius: 20px; background-color: rgb(54, 56, 58); background-image: url("./images/new.png"); background-repeat: none; background-position: left;}'
            u'QPushButton#save:hover{border-radius: 20px; background-color: rgb(54, 56, 58); background-image: url("./images/save.png"); background-repeat: none; background-position: left;}'
            u'QPushButton#modify:hover{border-radius: 20px; background-color: rgb(54, 56, 58); background-image: url("./images/modify.png"); background-repeat: none; background-position: left;}'
            u'QPushButton#table:hover{border-radius: 20px; background-color: rgb(54, 56, 58); background-image: url("./images/table.png"); background-repeat: none; background-position: left;}'
            u'QPushButton#setting:hover{border-radius: 20px; background-color: rgb(54, 56, 58); background-image: url("./images/setting.png"); background-repeat: none; background-position: left;}'
            u'QPushButton#logout:hover{border-radius: 20px; background-color: rgb(54, 56, 58); background-image: url("./images/logout.png"); background-repeat: none; background-position: left;}'
            u'QScrollBar::vertical{background-color: rgb(41, 43, 47); width: 9px; border-top-left-radius: 2px; border-top-right-radius: 2px; border-bottom-left-radius: 2px; border-bottom-right-radius: 2px; margin: 0px 2px 0px 2px;}'
            u'QScrollBar::handle::vertical{background-color: rgb(64, 67, 73); border: none; border-top-left-radius: 2px; border-top-right-radius: 2px; border-bottom-left-radius: 2px; border-bottom-right-radius: 2px;}'
            u'QScrollBar::sub-page::vertical, QScrollBar::add-page::vertical{ background-color: none;}'
            u'QScrollBar::sub-line::vertical, QScrollBar::add-line::vertical{background-color: none; border: none;}'
            u'QScrollBar::up-arrow::vertical, QScrollBar::down-arrow::vertical{background-color: none;}'
            u'QScrollBar::horizontal{background-color: rgb(41, 43, 47); height: 8px; border-top-left-radius: 4px; border-top-right-radius: 4px; border-bottom-left-radius: 4px; border-bottom-right-radius: 4px; }'
            u'QScrollBar::handle::horizontal{background-color: rgb(64, 67, 73); border: none; border-top-left-radius: 4px; border-top-right-radius: 4px; border-bottom-left-radius: 4px; border-bottom-right-radius: 4px;}'
            u'QScrollBar::sub-page::horizontal, QScrollBar::add-page::horizontal{ background-color: none;}'
            u'QScrollBar::sub-line::horizontal, QScrollBar::add-line::horizontal{background-color: none; border: none;}'
            u'QScrollBar::up-arrow::horizontal, QScrollBar::down-arrow::horizontal{background-color: none;}'
            u'QFrame#user_nav{background-color: rgb(32, 34, 37);}'
            u'QPushButton#extend{border: 0px; color: white; font-weight: bold; text-align: left; padding-left: 80px; background-image: url("./images/extend.png"); background-repeat: none; background-position: left;}'
            u'QPushButton#extend:hover{border-radius: 20px; background-color: rgb(54, 56, 58); background-image: url("./images/extend.png"); background-repeat: none; background-position: left;}')
        self.central_layout = QVBoxLayout()
        self.central_layout.setSpacing(0)
        self.central_layout.setContentsMargins(3, 3, 9, 15)
        self.central_widget.setLayout(self.central_layout)
        self.setCentralWidget(self.central_widget)
        self.window_header = QFrame()
        self.window_body = QFrame()
        self.setup_window_header()
        self.setup_body()
        self.load_data()

    def setup_window_header(self):
        self.window_header.mousePressEvent = self.header_mouse_press
        self.window_header.mouseMoveEvent = self.header_mouse_move
        self.window_header.mouseReleaseEvent = self.header_mouse_release
        self.window_header.setObjectName('header')
        label_group = QFrame()
        label_group.setFrameShape(QFrame.NoFrame)
        label_layout = QHBoxLayout()
        label_layout.setSpacing(0)
        label_layout.setContentsMargins(0, 0, 0, 0)
        label_layout.setAlignment(Qt.AlignLeft)
        logo = QIcon('images/logo.png')
        label_logo = QLabel()
        label_logo.setStyleSheet('border-top-left-radius: 6px;')
        label_logo.setPixmap(logo.pixmap(98, QIcon.Active, QIcon.On))
        label_layout.addWidget(label_logo)
        label_group.setLayout(label_layout)
        window_header_layout = QHBoxLayout()
        window_header_layout.setSpacing(0)
        window_header_layout.setContentsMargins(0, 0, 0, 0)
        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignRight)
        button_layout.setSpacing(0)
        button_layout.setContentsMargins(0, 0, 0, 0)
        button_group = QFrame()
        button_group.setFrameShape(QFrame.NoFrame)
        button_group.setLayout(button_layout)
        exit_btn = QPushButton('X')
        exit_btn.setFocusPolicy(Qt.NoFocus)
        minimize_btn = QPushButton('-')
        minimize_btn.setFocusPolicy(Qt.NoFocus)
        maximum_btn = QPushButton()
        maximum_btn.setFocusPolicy(Qt.NoFocus)
        maximum_btn.setIcon(QIcon('./images/maximum.png'))
        maximum_btn.clicked.connect(self.window_state)
        maximum_btn.setFixedSize(20, 20)
        maximum_btn.setObjectName('minimize_btn')
        exit_btn.setFixedSize(20, 20)
        minimize_btn.setFixedSize(20, 20)
        button_layout.addWidget(minimize_btn)
        button_layout.addWidget(maximum_btn)
        button_layout.addWidget(exit_btn)
        window_header_layout.addWidget(label_group)
        window_header_layout.addWidget(button_group)
        exit_btn.setObjectName('exit_btn')
        exit_btn.clicked.connect(self.exit_event)
        minimize_btn.setObjectName('minimize_btn')
        minimize_btn.clicked.connect(self.minimize_event)
        self.window_header.setFixedHeight(22)
        self.window_header.setLayout(window_header_layout)
        self.central_layout.addWidget(self.window_header)

    def setup_body(self):
        self.window_body.setObjectName('body')
        self.window_body.setFrameShape(QFrame.NoFrame)
        body_layout = QHBoxLayout()
        body_layout.setSpacing(0)
        body_layout.setContentsMargins(0, 0, 0, 0)
        self.article = QFrame()
        self.article.setObjectName('article')
        self.nav = QFrame()
        self.nav.setObjectName('nav')
        self.user_nav = QFrame()
        self.user_nav.setObjectName('user_nav')
        self.setup_user_nav()
        self.setup_article()
        self.setup_nav()
        body_layout.addWidget(self.user_nav)
        body_layout.addWidget(self.nav)
        body_layout.addWidget(self.article)
        self.window_body.setLayout(body_layout)
        self.central_layout.addWidget(self.window_body)

    def setup_article(self):
        article_layout = QVBoxLayout()
        article_layout.setSpacing(0)
        article_layout.setContentsMargins(0, 0, 0, 0)
        self.article.setFrameShape(QFrame.NoFrame)
        self.article.setLayout(article_layout)
        stack_widget = QStackedWidget()
        user_info = QFrame()
        user_info.setFrameShape(QFrame.NoFrame)
        table = QFrame()
        table.setFrameShape(QFrame.NoFrame)
        stack_widget.addWidget(user_info)
        self.setup_user_info(user_info)
        stack_widget.addWidget(table)
        article_layout.addWidget(stack_widget)

    def setup_user_info(self, user_info):
        user_info.setFocusPolicy(Qt.ClickFocus)
        user_info_layout = QVBoxLayout()
        user_info_layout.setSpacing(0)
        user_info_layout.setContentsMargins(0, 0, 0, 0)
        font = QFont('Roboto', 12, QFont.Bold)
        self.id = QLineEdit()
        self.id.setFont(font)
        self.id.setObjectName('info')
        self.id.setPlaceholderText(' ID...')
        self.name = QLineEdit()
        self.name.setFont(font)
        self.name.setObjectName('info')
        self.name.setPlaceholderText(' Name...')
        self.age = QLineEdit()
        self.age.setFont(font)
        self.age.setObjectName('info')
        self.age.setPlaceholderText(' Age...')
        self.salary = QLineEdit()
        self.salary.setFont(font)
        self.salary.setObjectName('info')
        self.salary.setPlaceholderText(' Salary...')
        self.email = QLineEdit()
        self.email.setFont(font)
        self.email.setObjectName('info')
        self.email.setPlaceholderText(' Email...')
        self.search = QLineEdit()
        self.search.setMaximumWidth(100)
        self.search.focusInEvent = self.anima
        self.search.focusOutEvent = self.anima
        self.search.setTextMargins(6, 0, 0, 0)
        self.search.setFont(font)
        self.search.setObjectName('search')
        self.search.setPlaceholderText(' Search...')
        search_btn = QPushButton()
        search_btn.setFixedSize(30, 28)
        search_btn.setObjectName('search-btn')
        search_btn.clicked.connect(self.search_event)
        search_widget = QFrame()
        search_widget.setFrameShape(QFrame.NoFrame)
        search_widget_layout = QHBoxLayout()
        search_widget_layout.setAlignment(Qt.AlignRight)
        search_widget_layout.setSpacing(0)
        search_widget_layout.setContentsMargins(0, 0, 0, 0)
        search_widget_layout.addWidget(self.search)
        search_widget_layout.addWidget(search_btn)
        search_widget.setLayout(search_widget_layout)
        control = QFrame()
        control.setStyleSheet('''
        QPushButton{
            background-color: rgb(54, 57, 63);
            border: none;
            background-image: url("./images/search.png");
            background-repeat: none;
        }
        QPushButton:hover{
            background-image: url("./images/search2.png");
            background-repeat: none;
            background-position: left;
        }
        QLineEdit#info{
            background-color: rgb(54, 57, 63);
            color: white;
            height: 25px;
            border: none;
            border-bottom: 1px solid cyan;
        }
        QLineEdit#search{
            background-color: rgb(54, 57, 63);
            color: white;
            height: 28px;
            border: 1px solid white;
            border-radius: 14px;
        }
        QLabel#title{
            color: cyan;
            font-size: 20px;
            font-weight: bold;
        }
        ''')
        control.setFrameShape(QFrame.NoFrame)
        control_layout = QGridLayout()
        control_layout.setSpacing(20)
        control_layout.setContentsMargins(20, 50, 20, 18)
        title = QLabel('Employee Information')
        title.setObjectName('title')
        self.error = QLabel()
        self.error.setAlignment(Qt.AlignCenter)
        self.error.setObjectName('error')
        control_layout.setColumnStretch(0, 1)
        control_layout.setColumnStretch(3, 1)
        control_layout.addWidget(title, 0, 1)
        control_layout.addWidget(search_widget, 0, 2)
        control_layout.addWidget(self.id, 1, 1)
        control_layout.addWidget(self.name, 1, 2)
        control_layout.addWidget(self.age, 2, 1)
        control_layout.addWidget(self.salary, 2, 2)
        control_layout.addWidget(self.email, 3, 1)
        control_layout.addWidget(self.error, 4, 0, 4, 0)
        control_layout.setColumnMinimumWidth(1, 550)
        control_layout.setColumnMinimumWidth(2, 550)
        control.setLayout(control_layout)
        user_info_layout.addWidget(control)
        self.table = QTableWidget()
        self.table.verticalHeader().hide()
        self.table.itemClicked.connect(self.table_click_event)
        self.table.setFocusPolicy(Qt.NoFocus)
        self.table.setSelectionMode(QTableWidget.SingleSelection)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setEditTriggers(QTableWidget().NoEditTriggers)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setStyleSheet('''
        QTableView{
            background-color: rgb(54, 57, 63);
            color: white;
            outline: 0;
            font-weight: bold;
        }
        QHeaderView::section::horizontal{
            background-color: rgb(54, 57, 63);
            border: 0px;
            color: white;
            font-weight: bold;
        }
        QTableCornerButton::section{
            background-color: rgb(54, 57, 63);
            border: none;
        }
        QTableView::Item:selected{
            background-color: rgb(42, 46, 53);
        }
        QTableView:Item{
            color: cyan;
        }
        QHeaderView{
            background-color: rgb(54, 57, 63);
        }
        QHeaderView::section::vertical{
            background-color: rgb(54, 57, 63);
            color: white;
            font-weight: bold;
            border: 0px;
            padding-left: 4px;
        }
        ''')
        self.table.setFrameShape(QFrame.NoFrame)
        self.table.setColumnCount(5)
        self.table.setColumnWidth(0, 55)
        self.table.setColumnWidth(1, 170)
        self.table.setColumnWidth(2, 55)
        self.table.setHorizontalHeaderLabels(['ID', 'Name', 'Age', 'Salary (M)', 'Email'])
        table_layout = QVBoxLayout()
        table_widget = QFrame()
        table_widget.setFrameShape(QFrame.NoFrame)
        table_layout.setSpacing(0)
        table_layout.setContentsMargins(18, 0, 18, 0)
        table_layout.addWidget(self.table)
        table_widget.setLayout(table_layout)
        user_info_layout.addWidget(table_widget)
        user_info.setLayout(user_info_layout)

    def setup_nav(self):
        self.nav.setFixedWidth(70)
        self.nav.setFrameShape(QFrame.NoFrame)
        nav_layout = QVBoxLayout()
        nav_layout.setSpacing(0)
        nav_layout.setContentsMargins(0, 0, 0, 0)
        group_btn = QFrame()
        group_btn.setFrameShape(QFrame.NoFrame)
        group_layout = QVBoxLayout()
        group_layout.setSpacing(0)
        group_layout.setContentsMargins(0, 0, 0, 0)
        group_layout.setAlignment(Qt.AlignTop)
        avatar_group = QFrame(group_btn)
        avatar_group.setToolTip('Avatar')
        avatar_layout = QHBoxLayout()
        avatar_layout.setContentsMargins(10, 0, 0, 0)
        avatar_layout.setSpacing(0)
        avatar_group.setFrameShape(QFrame.NoFrame)
        self.avatar_label = QLabel(avatar_group)
        self.avatar_label.setAlignment(Qt.AlignCenter)
        if not self.avatar:
            avatar_image = QIcon('images/default.png')
            pixmap = avatar_image.pixmap(48, QIcon.Active, QIcon.On)
        else:
            try:
                with open(f'images/anhdaidien{self._user_name}.jpg', 'rb') as file:
                    pixmap = self.mask_image(file.read())
            except:
                pixmap = QIcon('images/default.png').pixmap(48, QIcon.Active, QIcon.On)
        self.avatar_label.setFixedWidth(50)
        self.avatar_label.setPixmap(pixmap)
        avatar_btn = QPushButton('Avatar')
        avatar_btn.setStyleSheet('''
         border: none; background-color: none; color: white; font-weight: bold; text-align: left; margin-left: 20px; padding-left: 10px;
                ''')
        avatar_btn.setFocusPolicy(Qt.NoFocus)
        avatar_btn.setObjectName('avatar')
        avatar_btn.setFixedHeight(50)
        avatar_layout.addWidget(self.avatar_label)
        avatar_layout.addWidget(avatar_btn)
        avatar_group.setLayout(avatar_layout)
        avatar_group.setContextMenuPolicy(Qt.CustomContextMenu)
        avatar_group.customContextMenuRequested.connect(self.change_avatar)
        new_btn = QPushButton('New')
        new_btn.setToolTip('New')
        new_btn.setObjectName('new')
        new_btn.setFocusPolicy(Qt.NoFocus)
        new_btn.setFixedHeight(50)
        new_btn.clicked.connect(self.new_event)
        save_btn = QPushButton('Save')
        save_btn.setObjectName('save')
        save_btn.setToolTip('Save')
        save_btn.setFocusPolicy(Qt.NoFocus)
        save_btn.clicked.connect(self.insert_data)
        save_btn.setFixedHeight(50)
        save_btn.setShortcut(QKeySequence(Qt.Key_Return))
        modify_btn = QPushButton('Modify')
        modify_btn.setObjectName('modify')
        modify_btn.setToolTip('Modify')
        modify_btn.setFocusPolicy(Qt.NoFocus)
        modify_btn.setFixedHeight(50)
        modify_btn.clicked.connect(self.modify_event)
        delete_btn = QPushButton('Delete')
        delete_btn.setObjectName('table')
        delete_btn.setToolTip('Delete')
        delete_btn.setFocusPolicy(Qt.NoFocus)
        delete_btn.setFixedHeight(50)
        delete_btn.clicked.connect(self.delete_event)
        group_layout.addWidget(avatar_group)
        group_layout.addWidget(new_btn)
        group_layout.addWidget(save_btn)
        group_layout.addWidget(modify_btn)
        group_layout.addWidget(delete_btn)
        group_btn.setLayout(group_layout)
        nav_layout.addWidget(group_btn)
        setting_group = QFrame()
        setting_group.setFrameShape(QFrame.NoFrame)
        setting_layout = QVBoxLayout()
        setting_layout.setSpacing(0)
        setting_layout.setContentsMargins(0, 0, 0, 0)
        setting_layout.setAlignment(Qt.AlignBottom)
        setting_group.setLayout(setting_layout)
        setting_btn = QPushButton('Setting')
        setting_btn.setFocusPolicy(Qt.NoFocus)
        setting_btn.setObjectName('setting')
        setting_btn.setToolTip('Setting')
        setting_btn.setFixedHeight(50)
        setting_btn.clicked.connect(lambda: self.setting_click(self.nav))
        setting_layout.addWidget(setting_btn)
        log_out_btn = QPushButton('Log out')
        log_out_btn.setFocusPolicy(Qt.NoFocus)
        log_out_btn.clicked.connect(self.log_out_event)
        log_out_btn.setFixedHeight(50)
        log_out_btn.setObjectName('logout')
        log_out_btn.setToolTip('Log out')
        setting_layout.addWidget(log_out_btn)
        nav_layout.addWidget(setting_group)
        self.nav.setLayout(nav_layout)

    def setup_user_nav(self):
        self.user_nav.setFixedWidth(70)
        self.user_nav.setFrameShape(QFrame.NoFrame)
        self.user_nav.setFocusPolicy(Qt.NoFocus)
        user_nav_layout = QVBoxLayout()
        user_nav_layout.setSpacing(0)
        user_nav_layout.setContentsMargins(5, 0, 0, 0)
        users = QFrame()
        users.setFocusPolicy(Qt.NoFocus)
        users.setObjectName('users')
        users.setStyleSheet(u'QFrame#users{background-color: rgb(32, 34, 37);}')
        users_layout = QVBoxLayout()
        users_layout.setSpacing(0)
        users_layout.setContentsMargins(0, 0, 0, 0)
        scroll_area = QScrollArea()
        scroll_area.horizontalScrollBar().setHidden(True)
        scroll_area.setStyleSheet(
            u'QScrollArea{background-color: rgb(32, 34, 37);}'
            u'QPushButton{border: 0px; color: white; height: 50px; background-color: rgb(88, 101, 242); text-align: left; padding-left: 55px; border-radius: 20px; margin-bottom: 6px; background-image: url("./images/employee2.png"); background-repeat: none; background-position: left; font-weight: bold;}'
            u'QPushButton:hover{border-radius: 20px; background-color: rgb(54, 56, 58);}'
        )
        scroll_area.setFrameShape(QFrame.NoFrame)
        self.user_icon = QFrame()
        self.user_icon.setFrameShape(QFrame.NoFrame)
        self.user_icon.setFixedWidth(55)
        self.user_icon.setObjectName('user_icon')
        self.user_icon.setStyleSheet(u'QFrame#user_icon{background-color: rgb(32, 34, 37);}')
        self.users_icon_layout = QVBoxLayout()
        self.users_icon_layout.setAlignment(Qt.AlignTop)
        self.users_icon_layout.setSpacing(0)
        self.users_icon_layout.setContentsMargins(0, 0, 0, 0)
        self.user_icon.setLayout(self.users_icon_layout)
        scroll_area.setWidget(self.user_icon)
        scroll_area.setWidgetResizable(True)
        users_layout.addWidget(scroll_area)
        users.setLayout(users_layout)
        user_nav_layout.addWidget(users)
        extend = QFrame()
        extend.setFrameShape(QFrame.NoFrame)
        extend_layout = QHBoxLayout()
        extend_layout.setSpacing(0)
        extend_layout.setContentsMargins(0, 0, 0, 0)
        extend_btn = QPushButton('Extend')
        extend_btn.setFocusPolicy(Qt.NoFocus)
        extend_btn.setObjectName('extend')
        extend_btn.setFixedHeight(50)
        extend_btn.setToolTip('Extend')
        extend_btn.clicked.connect(lambda: self.setting_click(self.user_nav))
        extend_layout.addWidget(extend_btn)
        extend.setLayout(extend_layout)
        user_nav_layout.addWidget(extend)
        self.user_nav.setLayout(user_nav_layout)

    #   EVENT
    def setting_click(self, target):
        width = target.width()
        if width > 70:
            width_extend = 70
        else:
            width_extend = 200
        self.ani = QPropertyAnimation(target, b'minimumWidth')
        self.ani.setStartValue(width)
        self.ani.setEndValue(width_extend)
        self.ani.setDuration(300)
        self.ani.start()
        self.ani2 = QPropertyAnimation(self.user_icon, b'minimumWidth')
        self.ani2.setStartValue(width)
        self.ani2.setEndValue(width_extend - 15)
        self.ani2.setDuration(300)
        if 'user_nav' in str(target):
            self.ani2.start()

    def exit_event(self):
        self.e = exit_.ExitWindow('Exit')

    def minimize_event(self):
        self.setWindowState(Qt.WindowMinimized)

    def anima(self, e):
        if self.search.hasFocus():
            self.ani3 = QPropertyAnimation(self.search, b'maximumWidth')
            self.ani3.setStartValue(self.search.width())
            self.ani3.setEndValue(300)
            self.ani3.setDuration(199)
            self.ani3.start()
        else:
            self.ani3 = QPropertyAnimation(self.search, b'maximumWidth')
            self.ani3.setStartValue(self.search.width())
            self.ani3.setEndValue(100)
            self.ani3.setDuration(305)
            self.ani3.start()

    def log_out_event(self):
        self.w = exit_.ExitWindow('Log Out', self)

    def new_event(self):
        self.id.clear()
        self.name.clear()
        self.salary.clear()
        self.age.clear()
        self.email.clear()
        self.id.setFocus()
        self.table.clearSelection()
        for j in self._employee_temp:
            self._employee_temp[j][4].setStyleSheet(
                u'border: 0px; color: white; height: 50px; background-color: rgb(88, 101, 242); text-align: left; padding-left: 55px; border-radius: 20px; margin-bottom: 6px; background-image: url("./images/employee2.png"); background-repeat: none; background-position: left; font-weight: bold;}')
            self._employee_temp[j][4].setStyleSheet(
                u'QPushButton:hover{border-radius: 20px; background-color: rgb(54, 56, 58);}')

    def add_user(self, manv=None, tennv=None):
        if not manv and not tennv:
            new_user = QPushButton(
                self.name.text() + '                                                                             ' + self.id.text())
            new_user.setToolTip(self.name.text())
            new_user.setFocusPolicy(Qt.NoFocus)
            new_user.clicked.connect(lambda: self.display_info(new_user))
            self.users_icon_layout.addWidget(new_user)
            self._employee_temp[self.id.text()] = [self.name.text(), float(self.salary.text()), int(self.age.text()),
                                                   self.email.text(), new_user, self._index_of_dict]
            self._index_of_dict += 1
        else:
            new_user = QPushButton(
                tennv + '                                                                             ' + manv)
            new_user.setToolTip(tennv)
            self._employee_temp[manv].append(new_user)
            self._employee_temp[manv].append(self._index_of_dict)
            self._index_of_dict += 1
            new_user.setFocusPolicy(Qt.NoFocus)
            new_user.setToolTip(tennv)
            new_user.clicked.connect(lambda: self.display_info(new_user))
            self.users_icon_layout.addWidget(new_user)

    def display_info(self, this):
        i = this.text().split(' ')[len(this.text().split(' ')) - 1]
        self.table.selectRow(self._employee_temp[i][5])
        for j in self._employee_temp:
            if j == i:
                self._employee_temp[j][4].setStyleSheet(
                    'border-left: 3px solid cyan; background-color: rgb(54, 56, 58);}')
            else:
                self._employee_temp[j][4].setStyleSheet(
                    'border: 0px; color: white; height: 50px; background-color: rgb(88, 101, 242); text-align: left; padding-left: 55px; border-radius: 20px; margin-bottom: 6px; background-image: url("./images/employee2.png"); background-repeat: none; background-position: left; font-weight: bold;}')
                self._employee_temp[j][4].setStyleSheet(
                    u'QPushButton:hover{border-radius: 20px; background-color: rgb(54, 56, 58);}')
        self.id.setText(i)
        self.name.setText(self._employee_temp[i][0])
        self.salary.setText(str(self._employee_temp[i][1]))
        self.age.setText(str(self._employee_temp[i][2]))
        self.email.setText(self._employee_temp[i][3])

    def header_mouse_press(self, event):
        self.window_header.setCursor(Qt.ClosedHandCursor)
        self.old_pos = event.globalPos()

    def header_mouse_move(self, event):
        delta = self.old_pos - self.pos()
        self.move(event.globalPos() - delta)
        self.old_pos = event.globalPos()

    def header_mouse_release(self, event):
        self.window_header.setCursor(Qt.ArrowCursor)

    def error_label(self):
        ef = QGraphicsOpacityEffect(self.error)
        self.ani4 = QPropertyAnimation(ef, b'opacity')
        self.error.setGraphicsEffect(ef)
        self.ani4.setStartValue(0)
        self.ani4.setKeyValueAt(0.111, 1)
        self.ani4.setKeyValueAt(0.9, 0.5)
        self.ani4.setKeyValueAt(1, 0)
        self.ani4.setDuration(5000)
        self.ani4.start()

    def change_color_error(self, color):
        self.error.setStyleSheet(
            f'''
                QLabel#error{{
                    color: {color};
                    font-family: Roboto;
                    font-size: 15px;
                }}''')

    def insert_data(self):
        worker = QThread(self)
        worker.run = self.insert_event
        worker.start()
        time1 = time.time()
        while self.result is None:
            if time.time() - time1 > 5:
                self.change_color_error('red')
                self.error_label()
                self.error.setText('Server Time out')
                worker.quit()
                break
        error = self.result
        if 'Inserted' in str(error):
            self.table.setRowCount(self.table.rowCount() + 1)
            self.change_color_error('cyan')
            self.error_label()
            self.error.setText(error)
            self.table.setItem(self.table.rowCount() - 1, 0, QTableWidgetItem(self.id.text()))
            self.table.setItem(self.table.rowCount() - 1, 1, QTableWidgetItem(self.name.text()))
            self.table.setItem(self.table.rowCount() - 1, 2, QTableWidgetItem(self.age.text()))
            self.table.setItem(self.table.rowCount() - 1, 3, QTableWidgetItem(self.salary.text()))
            self.table.setItem(self.table.rowCount() - 1, 4, QTableWidgetItem(self.email.text()))
            self.add_user()
            self.new_event()
        elif not error is None:
            self.change_color_error('red')
            self.error_label()
            self.error.setText(error)
        self.result = None

    def load_data(self):
        data = load_data(self._user_name)
        self.table.setRowCount(len(load_data(self._user_name)))
        for i in range(len(load_data(self._user_name))):
            self.table.setItem(i, 0, QTableWidgetItem(data[i][0]))
            self.table.setItem(i, 1, QTableWidgetItem(
                binascii.unhexlify(data[i][1].encode('latin1', 'backslashreplace')).decode('unicode-escape',
                                                                                           errors='backslashreplace')))
            self.table.setItem(i, 2, QTableWidgetItem(str(data[i][3])))
            self.table.setItem(i, 3, QTableWidgetItem(str(data[i][2])))
            self.table.setItem(i, 4, QTableWidgetItem(data[i][4]))
            self._employee_temp[data[i][0]] = [
                binascii.unhexlify(data[i][1].encode('latin1', 'backslashreplace')).decode('unicode-escape',
                                                                                           errors='backslashreplace')]
            self._employee_temp[data[i][0]].append(data[i][2])
            self._employee_temp[data[i][0]].append(data[i][3])
            self._employee_temp[data[i][0]].append(data[i][4])
            self.add_user(data[i][0],
                          binascii.unhexlify(data[i][1].encode('latin1', 'backslashreplace')).decode('unicode-escape',
                                                                                                     errors='backslashreplace'))

    def table_click_event(self):
        row_index = self.table.currentRow()
        self.display_info(self._employee_temp[self.table.item(row_index, 0).text()][4])

    def window_state(self):
        if self.size() != self.s.size():
            if self.s:
                self.setGeometry(self.s)
            else:
                self.showMaximized()
                self.s = self.frameGeometry()
                self.center = self.s.center()
        else:
            self.s2 = QRect(0, 0, 800, 500)
            self.s2.moveCenter(self.center)
            self.setGeometry(self.s2)

    def modify_event(self):
        if self._employee_temp.get(self.id.text().strip()):
            worker = QThread(self)
            worker.run = self.modify_data
            worker.start()
            time1 = time.time()
            while self.result is None:
                if time.time() - time1 > 5:
                    self.change_color_error('red')
                    self.error_label()
                    self.error.setText('Server Time out')
                    worker.quit()
                    break
            error = self.result
            if error == 'Modified':
                self._employee_temp[self.id.text().strip()][0] = self.name.text()
                self._employee_temp[self.id.text().strip()][1] = float(self.salary.text())
                self._employee_temp[self.id.text().strip()][2] = int(self.age.text())
                self._employee_temp[self.id.text().strip()][3] = self.email.text()
                self._employee_temp[self.id.text().strip()][4].setText(
                    self.name.text() + '                                                                             ' + self.id.text())
                self._employee_temp[self.id.text().strip()][4].setToolTip(self.name.text())
                self.table.setItem(self._employee_temp[self.id.text().strip()][5], 0, QTableWidgetItem(self.id.text()))
                self.table.setItem(self._employee_temp[self.id.text().strip()][5], 1,
                                   QTableWidgetItem(self.name.text()))
                self.table.setItem(self._employee_temp[self.id.text().strip()][5], 2, QTableWidgetItem(self.age.text()))
                self.table.setItem(self._employee_temp[self.id.text().strip()][5], 3,
                                   QTableWidgetItem(self.salary.text()))
                self.table.setItem(self._employee_temp[self.id.text().strip()][5], 4,
                                   QTableWidgetItem(self.email.text()))
                self.change_color_error('cyan')
                self.error_label()
                self.error.setText(error)
            elif not error is None:
                self.change_color_error('red')
                self.error_label()
                self.error.setText(error)
            self.result = None
        else:
            self.change_color_error('red')
            self.error.setText('Not found ID')
            self.error_label()

    def delete_event(self):
        if self._employee_temp.get(self.id.text().strip()):
            worker = QThread(self)
            worker.run = self.delete_data
            worker.start()
            time1 = time.time()
            while self.result is None:
                if time.time() - time1 > 5:
                    self.change_color_error('red')
                    self.error_label()
                    self.error.setText('Server Time out')
                    worker.quit()
                    break
            error = self.result
            if error == 'Deleted':
                self._employee_temp[self.id.text()][4].close()
                self.table.setRowHidden(self._employee_temp[self.id.text()][5], True)
                self._employee_temp.pop(self.id.text())
                self.new_event()
                self.change_color_error('cyan')
                self.error_label()
                self.error.setText(error)
            elif not error is None:
                self.change_color_error('red')
                self.error_label()
                self.error.setText(error)
            self.result = None
        else:
            self.change_color_error('red')
            self.error_label()
            self.error.setText('ID not found')

    def search_event(self):
        if self._employee_temp.get(self.search.text()):
            self.display_info(self._employee_temp[self.search.text().strip()][4])
        else:
            self.change_color_error('red')
            self.error_label()
            self.error.setText('ID not found')

    def delete_data(self):
        self.result = delete_data(self.id.text(), self._user_name)

    def modify_data(self):
        self.result = modify_database(self.id.text(),
                                      binascii.hexlify(self.name.text().encode('latin1', errors='backslashreplace')),
                                      self.salary.text(), self.age.text(), self.email.text(), self._user_name)

    def insert_event(self):
        self.result = insert_into_data_base(self.id.text(),
                                            binascii.hexlify(self.name.text().encode('latin1', 'backslashreplace')),
                                            self.salary.text(), self.age.text(), self.email.text(), self._user_name)

    def change_avatar(self):
        menu = QMenu()
        menu.setStyleSheet('''QMenu{background-color: rgb(32, 34, 37);
        color: white;
        border: 1px solid white;
        font-weight: bold;}''')
        action = QAction('Change Avatar')
        action.triggered.connect(self.change_avatar_event)
        menu.addAction(action)
        menu.exec(QCursor().pos())

    def change_avatar_event(self):
        file = QFileDialog.getOpenFileName(self, 'Select image file', dir='C:', filter='Images (*jpg)')
        if file[0]:
            self.avatar_label.setPixmap(self.mask_image(open(file[0], 'rb').read()))
            insert_image(self._user_name)
            with open(file[0], 'rb') as file:
                with open(f'images/anhdaidien{self._user_name}.jpg', 'wb') as file_copy:
                    file_copy.write(file.read())

    @staticmethod
    def mask_image(imgdata, imgtype='jpg', size=45):
        try:
            image = QImage.fromData(imgdata, imgtype)

            image.convertToFormat(QImage.Format_ARGB32)

            imgsize = min(image.width(), image.height())
            rect = QRect(
                (image.width() - imgsize) / 2,
                (image.height() - imgsize) / 2,
                imgsize,
                imgsize,
            )

            image = image.copy(rect)

            out_img = QImage(imgsize, imgsize, QImage.Format_ARGB32)
            out_img.fill(Qt.transparent)

            brush = QBrush(image)

            painter = QPainter(out_img)
            painter.setBrush(brush)

            painter.setPen(Qt.NoPen)

            painter.drawEllipse(0, 0, imgsize, imgsize)

            painter.end()

            pr = QWindow().devicePixelRatio()
            pm = QPixmap.fromImage(out_img)
            pm.setDevicePixelRatio(pr)
            size *= pr
            pm = pm.scaled(size, size, Qt.KeepAspectRatio,
                           Qt.SmoothTransformation)

            return pm
        except:
            return QIcon('images/defautl.png').pixmap(48, QIcon.Active, QIcon.On)
