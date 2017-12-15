__author__ = 'Sergey.Farin'
from PyQt5 import QtGui, QtCore, QtWidgets
import mainwindow_ui


class Ribbon(QtWidgets.QTabWidget):
    def __init__(self, parent):
        if not isinstance(parent, mainwindow_ui.MainWindow):
            raise TypeError('parent must be a MainWindow')
        super(Ribbon, self).__init__()

        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)

        self.cascade_button = QtWidgets.QToolButton()
        self.cascade_button.setDisabled(True)
        self.cascade_button.setText("Cascade")
        self.cascade_button.setStatusTip("Cascade all windows")
        self.cascade_button.setToolTip("Cascade all windows")
        self.cascade_button.setIcon(QtGui.QIcon("images/icons/application_cascade.png"))
        self.cascade_button.setIconSize(QtCore.QSize(32, 32))
        self.cascade_button.setAutoRaise(True)
        self.cascade_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        # noinspection PyUnresolvedReferences
        self.cascade_button.clicked.connect(parent.mdi_area.cascadeSubWindows)

        self.expand_button = QtWidgets.QToolButton()
        self.expand_button.setDisabled(True)
        self.expand_button.setText("Maximize")
        self.expand_button.setStatusTip("Maximize active window")
        self.expand_button.setToolTip("Maximize active window")
        self.expand_button.setIcon(QtGui.QIcon("images/icons/arrow_out.png"))
        self.expand_button.setIconSize(QtCore.QSize(32, 32))
        self.expand_button.setAutoRaise(True)
        self.expand_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.arrange_button = QtWidgets.QToolButton()
        self.arrange_button.setDisabled(True)
        self.arrange_button.setText("Tile")
        self.arrange_button.setStatusTip("Tile all windows")
        self.arrange_button.setToolTip("Tile all windows")
        self.arrange_button.setIcon(QtGui.QIcon("images/icons/application_view_tile.png"))
        self.arrange_button.setIconSize(QtCore.QSize(32, 32))
        self.arrange_button.setAutoRaise(True)
        self.arrange_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        # noinspection PyUnresolvedReferences
        self.arrange_button.clicked.connect(parent.mdi_area.tileSubWindows)

        self.prev_window_button = QtWidgets.QToolButton()
        self.prev_window_button.setDisabled(True)
        self.prev_window_button.setText("Previous")
        self.prev_window_button.setStatusTip("Activate previous window (Ctrl+Shift+Tab)")
        self.prev_window_button.setToolTip("Activate previous window (Ctrl+Shift+Tab)")
        self.prev_window_button.setShortcut("Ctrl+Shift+Tab")
        self.prev_window_button.setIcon(QtGui.QIcon("images/icons/previous_window.png"))
        self.prev_window_button.setIconSize(QtCore.QSize(32, 32))
        self.prev_window_button.setAutoRaise(True)
        self.prev_window_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        # noinspection PyUnresolvedReferences
        self.prev_window_button.clicked.connect(parent.mdi_area.activatePreviousSubWindow)

        self.next_window_button = QtWidgets.QToolButton()
        self.next_window_button.setDisabled(True)
        self.next_window_button.setText("Next")
        self.next_window_button.setStatusTip("Activate next window (Ctrl+Tab)")
        self.next_window_button.setToolTip("Activate next window (Ctrl+Tab)")
        self.next_window_button.setShortcut(QtGui.QKeySequence.NextChild)
        self.next_window_button.setIcon(QtGui.QIcon("images/icons/application_go.png"))
        self.next_window_button.setIconSize(QtCore.QSize(32, 32))
        self.next_window_button.setAutoRaise(True)
        self.next_window_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        # noinspection PyUnresolvedReferences
        self.next_window_button.clicked.connect(parent.mdi_area.activateNextSubWindow)

        self.select_window_button = QtWidgets.QToolButton()
        self.select_window_button.setDisabled(True)
        self.select_window_button.setText("Switch to")
        self.select_window_button.setStatusTip("Switch to a window")
        self.select_window_button.setToolTip("Switch to a window")
        self.select_window_button.setIcon(QtGui.QIcon("images/icons/application_xp.png"))
        self.select_window_button.setIconSize(QtCore.QSize(32, 32))
        self.select_window_button.setAutoRaise(True)
        self.select_window_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        # self.select_window_button.clicked.connect(parent.mdi_area.activateNextSubWindow)

        quit_button = QtWidgets.QToolButton()
        quit_button.setText("Quit")
        quit_button.setStatusTip("Quit Application (Ctrl+Q)")
        quit_button.setToolTip("Quit Application (Ctrl+Q)")
        quit_button.setShortcut("Ctrl+Q")
        quit_button.setIcon(QtGui.QIcon("images/icons/door_in.png"))
        quit_button.setIconSize(QtCore.QSize(32, 32))
        quit_button.setAutoRaise(True)
        quit_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        # noinspection PyUnresolvedReferences
        quit_button.clicked.connect(parent.close)

        about_button = QtWidgets.QToolButton()
        about_button.setText("About")
        about_button.setStatusTip("About the Application (F1)")
        about_button.setToolTip("About the Application (F1)")
        about_button.setShortcut("F1")
        about_button.setIcon(QtGui.QIcon("images/icons/help.png"))
        about_button.setIconSize(QtCore.QSize(32, 32))
        about_button.setAutoRaise(True)
        about_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        # noinspection PyUnresolvedReferences
        about_button.clicked.connect(parent.about)

        self.setStyleSheet("""
                    QWidget {
                        background: qlineargradient(
                            x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FFFFFF, stop: 0.5 #FFFFFF, stop: 1.0 #EAEDF1);
                        }
                    QTabWidget::tab-bar {
                        left: 30px;
                        }
                    QTabBar::tab {
                        padding: 5px 15px 3px 15px;
                        border: 1px solid #a4a063;
                        border-top-left-radius: 4px;
                        border-top-right-radius: 4px;
                        }
                    QTabBar::tab:!selected {
                        border-top: 0px;
                        border-left: 0px;
                        border-right: 0px;
                        background-color:#F0F0F0;
                        }
                    QTabBar::tab:hover {
                        border-top: 1px solid #a4a063;
                        border-left: 1px solid #a4a063;
                        border-right: 1px solid #a4a063;
                        }
                    QTabBar::tab:selected {
                        border: 1px solid #808090;
                        border-bottom: solid 0px;
                        background-color:#FFFFFF;
                        }""")

        ribbon_home = QtWidgets.QWidget()
        ribbon_window = QtWidgets.QWidget()
        ribbon_extra = QtWidgets.QWidget()

        self.addTab(ribbon_home, " Home ")
        self.addTab(ribbon_window, " Window ")
        # self.addTab(ribbon_extra, " Extra ")

        ribbon_home_layout = QtWidgets.QHBoxLayout()
        ribbon_home_layout.setContentsMargins(0, 0, 0, 0)
        ribbon_home.setLayout(ribbon_home_layout)
        # ribbon_home.setStyleSheet("""background-color:transparent;""")

        ribbon_home_plot_area = QtWidgets.QVBoxLayout()
        ribbon_home_plot_area.setContentsMargins(10, 0, 10, 0)
        self.ribbon_home_plot_area_layout = QtWidgets.QHBoxLayout()
        ribbon_home_plot_area.addLayout(self.ribbon_home_plot_area_layout)
        ribbon_home_plot_area.addStretch()
        # label = QtWidgets.QLabel('<font color="#666666">Main</font>')
        # label.setAlignment(QtCore.Qt.AlignCenter)
        # ribbon_home_plot_area.addWidget(label)
        ribbon_home_layout.addLayout(ribbon_home_plot_area)
        ribbon_separator1 = QtWidgets.QFrame()
        ribbon_separator1.setFrameShape(QtWidgets.QFrame.VLine)
        ribbon_separator1.setFrameShadow(QtWidgets.QFrame.Sunken)
        ribbon_separator1.setStyleSheet("""background-color:#FFFFFF;""")
        ribbon_home_layout.addWidget(ribbon_separator1)

        ribbon_home_window_area = QtWidgets.QVBoxLayout()
        ribbon_home_window_area.setContentsMargins(0, 0, 0, 0)
        ribbon_home_window_area_layout = QtWidgets.QHBoxLayout()
        ribbon_home_window_area_layout.setContentsMargins(0, 0, 0, 0)
        ribbon_home_window_area.addLayout(ribbon_home_window_area_layout)
        ribbon_home_window_area.addStretch()
        # label = QtWidgets.QLabel('<font color="#666666">Window</font>')
        # label.setAlignment(QtCore.Qt.AlignCenter)
        # ribbon_home_window_area.addWidget(label)
        ribbon_home_window_area_layout.addWidget(self.cascade_button)
        # ribbon_home_window_area_layout.addWidget(self.expand_button)
        ribbon_home_window_area_layout.addWidget(self.arrange_button)
        ribbon_home_window_area_layout.addWidget(self.prev_window_button)
        ribbon_home_window_area_layout.addWidget(self.next_window_button)
        # ribbon_home_window_area_layout.addWidget(self.select_window_button)
        ribbon_home_layout.addLayout(ribbon_home_window_area)
        ribbon_separator2 = QtWidgets.QFrame()
        ribbon_separator2.setFrameShape(QtWidgets.QFrame.VLine)
        ribbon_separator2.setFrameShadow(QtWidgets.QFrame.Sunken)
        ribbon_separator2.setStyleSheet("""background-color:#FFFFFF;""")
        ribbon_home_layout.addWidget(ribbon_separator2)

        ribbon_home_quit_area = QtWidgets.QVBoxLayout()
        ribbon_home_quit_area.setContentsMargins(0, 0, 0, 0)
        ribbon_home_quit_area_layout = QtWidgets.QHBoxLayout()
        ribbon_home_quit_area_layout.setContentsMargins(0, 0, 0, 0)
        ribbon_home_quit_area.addLayout(ribbon_home_quit_area_layout)
        ribbon_home_quit_area.addStretch()
        # label = QtWidgets.QLabel('<font color="#666666"></font>')
        # label.setAlignment(QtCore.Qt.AlignCenter)
        # ribbon_home_quit_area.addWidget(label)
        ribbon_home_quit_area_layout.addWidget(quit_button)
        ribbon_home_layout.addLayout(ribbon_home_quit_area)

        ribbon_home_layout.addStretch()

        ribbon_home_help_area = QtWidgets.QVBoxLayout()
        ribbon_home_help_area.setContentsMargins(0, 0, 0, 0)
        ribbon_home_help_area_layout = QtWidgets.QHBoxLayout()
        ribbon_home_help_area_layout.setContentsMargins(0, 0, 0, 0)
        ribbon_home_help_area.addLayout(ribbon_home_help_area_layout)
        ribbon_home_help_area.addStretch()
        # label = QtWidgets.QLabel('<font color="#666666"></font>')
        # label.setAlignment(QtCore.Qt.AlignCenter)
        # ribbon_home_help_area.addWidget(label)
        ribbon_home_help_area_layout.addWidget(about_button)
        ribbon_home_layout.addLayout(ribbon_home_help_area)

        ribbon_home_layout.addSpacing(5)

        # ribbon_home_layout_extra = QtGui.QVBoxLayout()
        #
        # ribbon_home_layout_extra.addLayout(ribbon_home_layout)
        # ribbon_home_layout_extra.addStretch()
        # ribbon_home_
        # ribbon_home_layout_extra.addWidget(QtGui.QLabel("Some Text"))
        # ribbon_home_layout_extra.setContentsMargins(10, 0, 10, 0)
        # ribbon.addTab(ribbon_home, "Home")
        #
        # ribbon_home_layout.addWidget(self.cascade_button)

        # ribbon.insetWidget(cascade)
