from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
                            QHBoxLayout, QSpacerItem,QSizePolicy,QListWidget, QListWidgetItem,QMenu,QAction)

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QFont

from PyQt5.QtGui import QCursor
from PyQt5.QtCore import QPoint

class MyLable(QWidget):
    def __init__(self, title, subtitle, icon_path):
        super(MyLable, self).__init__()
        self.lb_title = QLabel(title)
        self.lb_title.setFont(QFont("Arial", 10, QFont.Bold))
        self.lb_subtitle = QLabel(subtitle)
        self.lb_subtitle.setFont(QFont("Arial", 8, QFont.StyleItalic))
        self.lb_icon = QLabel()
        self.lb_icon.setFixedSize(40, 40)
        pixMap = QPixmap(icon_path).scaled(self.lb_icon.width(), self.lb_icon.height())
        self.lb_icon.setPixmap(pixMap)
        self.double_click_fun = None
        self.init_ui()


    def init_ui(self):
        """handle layout"""
        ly_main = QHBoxLayout()
        ly_right = QVBoxLayout()
        ly_right.addWidget(self.lb_title)
        ly_right.addWidget(self.lb_subtitle)
        ly_right.setAlignment(Qt.AlignVCenter)
        ly_main.addWidget(self.lb_icon)
        ly_main.addLayout(ly_right)
        self.setLayout(ly_main)
        self.resize(90, 60)

    def get_lb_title(self):
        return self.lb_title.text()

    def get_lb_subtitle(self):
        return self.lb_subtitle.text()

class ListWindow(QWidget):
    def __init__(self, parent=None):
        super(ListWindow, self).__init__(parent)
        self.doubleclick_fun = None
        self.list_widget = QListWidget()


    def _set_items(self, list_text):
        self.list_widget.clear()
        ly_vbox = QVBoxLayout()
        print("set_items>",list_text)
        for item in list_text:
            self._setItem(item[0], str(item[1]), item[2])
        ly_vbox.addWidget(self.list_widget)
        self.list_widget.itemClicked.connect(self.item_doubleclick_slot)
        self.list_widget.customContextMenuRequested[QPoint].connect(self.myListWidgetContext)
        self.list_widget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.setLayout(ly_vbox)

    def getListitems(self):
        return self.selectedItems()

    def myListWidgetContext(self, point):
        popMenu = QMenu()
        popMenu.addAction(QAction(u'添加', self, triggered=self.close))
        popMenu.addAction(QAction(u'删除', self, triggered=self.addItem))
        popMenu.addAction(QAction(u'修改', self, triggered=self.close))

        popMenu.exec_(QCursor.pos())

    def addItem(self):
        print("执行了删除")
        L = [["1","1","avatar.jpg"],["1","1","avatar.jpg"]]
        self._set_items(L)


    def _setItem(self, title, subtitle, pic_path):
        item_widget = QListWidgetItem()
        item_widget.setSizeHint(QSize(90, 60))
        self.list_widget.addItem(item_widget)

        label = MyLable(title, subtitle, pic_path)
        self.list_widget.setItemWidget(item_widget, label)


    def item_doubleclick_slot(self):
        if self.doubleclick_fun:
            widget = self.list_widget.itemWidget(self.list_widget.currentItem()) # get MyLabel widget
            self.doubleclick_fun(widget.get_lb_title(), widget.get_lb_subtitle())

    def set_doubleclick_slot(self, fun):
        """set item double click slot"""
        self.doubleclick_fun = fun



class LoginLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super(LoginLineEdit, self).__init__()
        self.setObjectName("LoginLine")
        self.parent = parent
        self.setMinimumSize(218, 20)
        with open('qss/loginLine.qss', 'r') as f:
            self.setStyleSheet(f.read())

        self.button = QPushButton(self)
        self.button.setMaximumSize(13, 13)
        self.button.setCursor(QCursor(Qt.PointingHandCursor))

        self.setTextMargins(3, 0, 19, 0)

        self.spaceItem = QSpacerItem(150, 10, QSizePolicy.Expanding)

        self.mainLayout = QHBoxLayout()
        self.mainLayout.addSpacerItem(self.spaceItem)
        # self.mainLayout.addStretch(1)
        self.mainLayout.addWidget(self.button)
        self.mainLayout.addSpacing(10)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.mainLayout)