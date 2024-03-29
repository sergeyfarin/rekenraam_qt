__author__ = 'Sergey.Farin'
import os

os.environ["PATH"] += ("C:\\Apps\\Programs\\miniconda3\\envs\\jupyter;" +
                       "C:\\Apps\\Programs\\miniconda3\\envs\\jupyter\\Library\\mingw - w64\\bin;" +
                       "C:\\Apps\\Programs\\miniconda3\\envs\\jupyter\\Library\\usr\\bin;" +
                       "C:\\Apps\\Programs\\miniconda3\\envs\\jupyter\\Library\\bin;" +
                       "C:\\Apps\\Programs\\miniconda3\\envs\\jupyter\\Scripts;" +
                       "C:\\Apps\\Programs\\miniconda3\\envs\\jupyter\\bin;") + os.environ["PATH"]
from PyQt5 import QtGui, QtCore, QtWidgets
import mainwindow_ui

class Ribbon(QtWidgets.QFrame):
    def __init__(self, parent):
        if not isinstance(parent, mainwindow_ui.MainWindow):
            raise TypeError('parent must be a MainWindow')
        super(Ribbon, self).__init__()

        self.main_window = parent
        self.setObjectName("Ribbon")
        self.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Maximum)
        ribbon_layout = QtWidgets.QVBoxLayout()
        ribbon_layout.setSpacing(0)
        ribbon_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(ribbon_layout)
        ribbon_layout.addItem(QtWidgets.QSpacerItem(0, 10))
        self.ribbon_tabs = QtWidgets.QTabWidget()
        self.ribbon_tabs.setObjectName("RibbonTabs")
        self.ribbon_tabs.tabBar().setObjectName("RibbonTabBar")
        ribbon_layout.addWidget(self.ribbon_tabs)
        ribbon_layout.addItem(QtWidgets.QSpacerItem(0, 0))

        parent.info_button = QtWidgets.QToolButton()
        parent.info_button.setObjectName("InfoButton")
        parent.info_button.setStatusTip("About")
        parent.info_button.setIcon(QtGui.QIcon("images/icons/icons8-info-2.png"))
        parent.info_button.setIconSize(QtCore.QSize(24, 24))
        # info_button.setAutoRaise(True)
        # info_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        # self.layout.addWidget(info_button)
        parent.info_button.name = 'about'
        parent.info_button.resize(24, 24)
        parent.info_button.move(self.width() - 30, 6)
        parent.info_button.move(10, 10)
        # parent.info_button.raise()
        # print(self.home_tab.height())
        # self.info_button.setStyleSheet('background-color:red;')
        parent.info_button.setParent(parent)
        # parent.info_button.clicked.connect(self.about)
        parent.info_button.show()

        self.version = parent.version
        self.about()

    def add_tab(self, name):
        new_tab = RibbonTab(self, self.main_window)
        self.ribbon_tabs.addTab(new_tab, " "+name+" ")
        new_tab.layout0 = QtWidgets.QVBoxLayout()
        new_tab.layout0.setContentsMargins(0, 0, 0, 0)
        new_tab.layout = QtWidgets.QHBoxLayout()
        new_tab.layout.setContentsMargins(0, 0, 0, 0)
        new_tab.layout0.addItem(QtWidgets.QSpacerItem(0, 3))
        new_tab.layout0.addLayout(new_tab.layout)
        new_tab.layout0.addItem(QtWidgets.QSpacerItem(0, 0))
        new_tab.layout.setAlignment(QtCore.Qt.AlignLeft)
        new_tab.layout.addItem(QtWidgets.QSpacerItem(10, 0))
        new_tab.setLayout(new_tab.layout0)
        return new_tab

    def about(self):
        # self.w = AboutPopup()
        # self.w.setGeometry(QtCore.QRect(100, 100, 400, 200))
        # self.w.show()

        about_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.NoIcon, "About Fireweed", # "" + self.version + """
                            """<h2>Fireweed</h2>
                            Field, Reservoir and Well Electronic Dashboard<br><br>
                            Created by <a href="mailto:Sergey.Farin@gmail.com?Subject=Fireweed">
                            Sergey Farin</a><br><br>
                            Powered by:
                            <a href="https://www.python.org/">Python</a>,
                            <a href="http://qt-project.org/wiki/PySide">PySide</a>, """ +
                            # """<a href="http://www.riverbankcomputing.com/software/pyqt/download">PyQt</a>,"""+
                            """<a href="http://matplotlib.org">matplotlib</a>,
                            <a href="http://www.numpy.org">NumPy</a>,
                            <a href="http://pandas.pydata.org">Pandas</a>,
                            <a href="https://code.google.com/p/pyodbc">PyODBC</a>,
                            <a href="http://www.fatcow.com">FatCow</a> Fram-fresh icons</a>
                            <br>""")


        about_box.exec()


class RibbonTab(QtWidgets.QWidget):
    def __init__(self, parent, main_window):
        if not isinstance(parent, Ribbon) and not isinstance(main_window, mainwindow_ui.MainWindow):
            raise TypeError('grandparent must be a MainWindow')
        super(RibbonTab, self).__init__()

    def add_button(self, name, status_tip, icon_link):
        new_button = QtWidgets.QToolButton()
        new_button.setText(name)
        new_button.setStatusTip(status_tip)
        new_button.setIcon(QtGui.QIcon(icon_link))
        new_button.setIconSize(QtCore.QSize(32, 32))
        new_button.setAutoRaise(True)
        new_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.layout.addWidget(new_button)
        return new_button

        # self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)

class AboutPopup(QtWidgets.QWidget):
    def __init__(self):
        super(AboutPopup, self).__init__()
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(QtWidgets.QLabel("rebrerbreb"))



        # ribbon_home_window_area = QtWidgets.QVBoxLayout()
        # ribbon_home_window_area.setContentsMargins(0, 0, 0, 0)
        # ribbon_home_window_area_layout = QtWidgets.QHBoxLayout()
        # ribbon_home_window_area_layout.setContentsMargins(0, 0, 0, 0)
        # ribbon_home_window_area.addLayout(ribbon_home_window_area_layout)
        # ribbon_home_window_area.addStretch()
        # label = QtWidgets.QLabel('<font color="#666666">Window</font>')
        # label.setAlignment(QtCore.Qt.AlignCenter)
        # ribbon_home_window_area.addWidget(label)
        # ribbon_home_window_area_layout.addWidget(self.cascade_button)
        # # ribbon_home_window_area_layout.addWidget(self.expand_button)
        # ribbon_home_window_area_layout.addWidget(self.arrange_button)
        # ribbon_home_window_area_layout.addWidget(self.prev_window_button)
        # ribbon_home_window_area_layout.addWidget(self.next_window_button)
        #
        # self.home_button = QtWidgets.QToolButton()
        # self.home_button.setText("New well plot")
        # self.home_button.setStatusTip("New well plot")
        # self.home_button.setIcon(QtGui.QIcon("images/icons/color/icons8-home.png"))
        # self.home_button.setIconSize(QtCore.QSize(32, 32))
        # self.home_button.setAutoRaise(True)
        # self.home_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        # # noinspection PyUnresolvedReferences
        # # self.home_button.clicked.connect(self.make_chart)
        # # self.ribbon.ribbon_home_plot_area_layout.addWidget(self.newWellProductionPlot)
        #
        # self.cascade_button = QtWidgets.QToolButton()
        # # self.cascade_button.setDisabled(True)
        # self.cascade_button.setText("Cascade")
        # self.cascade_button.setStatusTip("Cascade all windows")
        # self.cascade_button.setToolTip("Cascade all windows")
        # self.cascade_button.setIcon(QtGui.QIcon("images/icons/color/icons8-cashbook.png"))
        # self.cascade_button.setIconSize(QtCore.QSize(32, 32))
        # self.cascade_button.setAutoRaise(True)
        # self.cascade_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        # # noinspection PyUnresolvedReferences
        # # self.cascade_button.clicked.connect(parent.main_area.cascadeSubWindows)
        #
        # self.expand_button = QtWidgets.QToolButton()
        # # self.expand_button.setDisabled(True)
        # self.expand_button.setText("Maximize")
        # self.expand_button.setStatusTip("Maximize active window")
        # self.expand_button.setToolTip("Maximize active window")
        # self.expand_button.setIcon(QtGui.QIcon("images/icons/color/icons8-tasks.png"))
        # self.expand_button.setIconSize(QtCore.QSize(32, 32))
        # self.expand_button.setAutoRaise(True)
        # # self.expand_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        #
        # self.arrange_button = QtWidgets.QToolButton()
        # # self.arrange_button.setDisabled(True)
        # self.arrange_button.setText("Tile")
        # self.arrange_button.setStatusTip("Tile all windows")
        # self.arrange_button.setToolTip("Tile all windows")
        # self.arrange_button.setIcon(QtGui.QIcon("images/icons/color/icons8-stocks.png"))
        # self.arrange_button.setIconSize(QtCore.QSize(32, 32))
        # self.arrange_button.setAutoRaise(True)
        # self.arrange_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        # # noinspection PyUnresolvedReferences
        # # self.arrange_button.clicked.connect(parent.main_area.tileSubWindows)
        #
        # self.prev_window_button = QtWidgets.QToolButton()
        # self.prev_window_button.setDisabled(True)
        # self.prev_window_button.setText("Previous")
        # self.prev_window_button.setStatusTip("Activate previous window (Ctrl+Shift+Tab)")
        # self.prev_window_button.setToolTip("Activate previous window (Ctrl+Shift+Tab)")
        # self.prev_window_button.setShortcut("Ctrl+Shift+Tab")
        # self.prev_window_button.setIcon(QtGui.QIcon("images/icons/previous_window.png"))
        # self.prev_window_button.setIconSize(QtCore.QSize(32, 32))
        # self.prev_window_button.setAutoRaise(True)
        # self.prev_window_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        # # noinspection PyUnresolvedReferences
        # # self.prev_window_button.clicked.connect(parent.main_area.activatePreviousSubWindow)
        #
        # self.next_window_button = QtWidgets.QToolButton()
        # self.next_window_button.setDisabled(True)
        # self.next_window_button.setText("Next")
        # self.next_window_button.setStatusTip("Activate next window (Ctrl+Tab)")
        # self.next_window_button.setToolTip("Activate next window (Ctrl+Tab)")
        # self.next_window_button.setShortcut(QtGui.QKeySequence.NextChild)
        # self.next_window_button.setIcon(QtGui.QIcon("images/icons/application_go.png"))
        # self.next_window_button.setIconSize(QtCore.QSize(32, 32))
        # self.next_window_button.setAutoRaise(True)
        # self.next_window_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        # # noinspection PyUnresolvedReferences
        # # self.next_window_button.clicked.connect(parent.main_area.activateNextSubWindow)
        #
        # self.select_window_button = QtWidgets.QToolButton()
        # self.select_window_button.setDisabled(True)
        # self.select_window_button.setText("Switch to")
        # self.select_window_button.setStatusTip("Switch to a window")
        # self.select_window_button.setToolTip("Switch to a window")
        # self.select_window_button.setIcon(QtGui.QIcon("images/icons/application_xp.png"))
        # self.select_window_button.setIconSize(QtCore.QSize(32, 32))
        # self.select_window_button.setAutoRaise(True)
        # self.select_window_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        # # self.select_window_button.clicked.connect(parent.main_area.activateNextSubWindow)
        #
        # ribbon_home = QtWidgets.QWidget()
        # ribbon_window = QtWidgets.QWidget()
        # ribbon_extra = QtWidgets.QWidget()
        #
        # self.addTab(ribbon_home, " Home ")
        # self.addTab(ribbon_window, " Window ")
        # self.addTab(ribbon_extra, " Extra ")
        # # self.setStyleSheet("QWidget#Ribbon {background-image: url(images/bg.jpg);}")
        # ribbon_layout = QtWidgets.QHBoxLayout()
        # ribbon_layout.setContentsMargins(0, 0, 0, 0)
        # ribbon_home.setLayout(ribbon_layout)
        # # ribbon_home.setStyleSheet("""background-color:transparent;""")
        #
        # ribbon_home_area = QtWidgets.QVBoxLayout()
        # ribbon_home_area.setContentsMargins(10, 0, 10, 0)
        # ribbon_home_area_layout = QtWidgets.QHBoxLayout()
        # ribbon_home_area.addLayout(ribbon_home_area_layout)
        # ribbon_home_area.addStretch()
        # # label = QtWidgets.QLabel('<font color="#666666">Main</font>')
        # # label.setAlignment(QtCore.Qt.AlignCenter)
        # # ribbon_home_area.addWidget(label)
        # ribbon_layout.addLayout(ribbon_home_area)
        # ribbon_separator1 = QtWidgets.QFrame()
        # ribbon_separator1.setFrameShape(QtWidgets.QFrame.VLine)
        # ribbon_separator1.setFrameShadow(QtWidgets.QFrame.Sunken)
        # # ribbon_separator1.setStyleSheet("""background-color:#FFFFFF;""")
        # ribbon_layout.addWidget(ribbon_separator1)
        #
        # ribbon_home_window_area = QtWidgets.QVBoxLayout()
        # ribbon_home_window_area.setContentsMargins(0, 0, 0, 0)
        # ribbon_home_window_area_layout = QtWidgets.QHBoxLayout()
        # ribbon_home_window_area_layout.setContentsMargins(0, 0, 0, 0)
        # ribbon_home_window_area.addLayout(ribbon_home_window_area_layout)
        # ribbon_home_window_area.addStretch()
        # label = QtWidgets.QLabel('<font color="#666666">Window</font>')
        # label.setAlignment(QtCore.Qt.AlignCenter)
        # ribbon_home_window_area.addWidget(label)
        # ribbon_home_window_area_layout.addWidget(self.cascade_button)
        # # ribbon_home_window_area_layout.addWidget(self.expand_button)
        # ribbon_home_window_area_layout.addWidget(self.arrange_button)
        # ribbon_home_window_area_layout.addWidget(self.prev_window_button)
        # ribbon_home_window_area_layout.addWidget(self.next_window_button)
        # # ribbon_home_window_area_layout.addWidget(self.select_window_button)
        # ribbon_layout.addLayout(ribbon_home_window_area)
        # ribbon_separator2 = QtWidgets.QFrame()
        # ribbon_separator2.setFrameShape(QtWidgets.QFrame.VLine)
        # # ribbon_separator2.setFrameShadow(QtWidgets.QFrame.Sunken)
        # ribbon_separator2.setStyleSheet("""color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgba(150,150,150,255), stop: 0.5 rgba(150,255,150,0), stop: 1.0 rgba(150,150,150,255));""")
        #
        #
        #
        # ribbon_layout.addWidget(ribbon_separator2)
        #
        # ribbon_layout.addStretch()
        #
        # ribbon_home_help_area = QtWidgets.QVBoxLayout()
        # ribbon_home_help_area.setContentsMargins(0, 0, 0, 0)
        # ribbon_home_help_area_layout = QtWidgets.QHBoxLayout()
        # ribbon_home_help_area_layout.setContentsMargins(0, 0, 0, 0)
        # ribbon_home_help_area.addLayout(ribbon_home_help_area_layout)
        # ribbon_home_help_area.addStretch()
        # # label = QtWidgets.QLabel('<font color="#666666"></font>')
        # # label.setAlignment(QtCore.Qt.AlignCenter)
        # # ribbon_home_help_area.addWidget(label)
        #
        # about_button = QtWidgets.QToolButton()
        # about_button.setText("About")
        # about_button.setStatusTip("About the Application (F1)")
        # about_button.setToolTip("About the Application (F1)")
        # about_button.setShortcut("F1")
        # about_button.setIcon(QtGui.QIcon("images/icons/color/icons8-info.png"))
        # about_button.setIconSize(QtCore.QSize(32, 32))
        # about_button.setAutoRaise(True)
        # about_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        # # noinspection PyUnresolvedReferences
        # about_button.clicked.connect(main_window.about)
        #
        # ribbon_home_help_area_layout.addWidget(about_button)
        # ribbon_layout.addLayout(ribbon_home_help_area)
        #
        # ribbon_home_quit_area = QtWidgets.QVBoxLayout()
        # ribbon_home_quit_area.setContentsMargins(0, 0, 0, 0)
        # ribbon_home_quit_area_layout = QtWidgets.QHBoxLayout()
        # ribbon_home_quit_area_layout.setContentsMargins(0, 0, 0, 0)
        # ribbon_home_quit_area.addLayout(ribbon_home_quit_area_layout)
        # ribbon_home_quit_area.addStretch()
        # # label = QtWidgets.QLabel('<font color="#666666"></font>')
        # # label.setAlignment(QtCore.Qt.AlignCenter)
        # # ribbon_home_quit_area.addWidget(label)
        # quit_button = QtWidgets.QToolButton()
        # quit_button.setText("Quit")
        # quit_button.setStatusTip("Quit Application (Ctrl+Q)")
        # quit_button.setToolTip("Quit Application (Ctrl+Q)")
        # quit_button.setShortcut("Ctrl+Q")
        # quit_button.setIcon(QtGui.QIcon("images/icons/color/icons8-close-existing-tab.png"))
        # quit_button.setIconSize(QtCore.QSize(32, 32))
        # quit_button.setAutoRaise(True)
        # quit_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        # # noinspection PyUnresolvedReferences
        # quit_button.clicked.connect(main_window.close)
        #
        # ribbon_home_quit_area_layout.addWidget(quit_button)
        # ribbon_layout.addLayout(ribbon_home_quit_area)
        #
        # ribbon_layout.addSpacing(5)
        #
        # # ribbon_home_layout_extra = QtGui.QVBoxLayout()
        # #
        # # ribbon_home_layout_extra.addLayout(ribbon_layout)
        # # ribbon_home_layout_extra.addStretch()
        # # ribbon_home_
        # # ribbon_home_layout_extra.addWidget(QtGui.QLabel("Some Text"))
        # # ribbon_home_layout_extra.setContentsMargins(10, 0, 10, 0)
        # # ribbon.addTab(ribbon_home, "Home")
        # #
        # # ribbon_layout.addWidget(self.cascade_button)
        #
        # # ribbon.insetWidget(cascade)





