from PyQt5 import QtGui, QtCore, QtWidgets
# noinspection PyUnresolvedReferences
import ribbon_ui
import os


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        if os.path.isfile('VERSION'):
            version_file = open('VERSION')
            self.version = version_file.read()
            version_file.close()
        else:
            self.version = ""
        self.setWindowTitle("Rekenraam "+self.version)

        for f in os.listdir('fonts'):
            if os.path.isfile(os.path.join('fonts', f)) and f.split(sep='.')[1] == 'ttf':
                QtGui.QFontDatabase.addApplicationFont(os.path.join('fonts', f))

        if os.path.isfile('main_window.qss'):
            with open('main_window.qss') as qss:
                self.setStyleSheet(qss.read())

        self.setMinimumSize(500, 400)

        layout_for_ribbon = QtWidgets.QVBoxLayout()
        layout_for_ribbon.setSpacing(0)
        layout_for_ribbon.setContentsMargins(0, 0, 0, 0)
        layout_for_left_pane = QtWidgets.QHBoxLayout()
        layout_for_left_pane.setSpacing(0)
        layout_for_left_pane.setContentsMargins(0, 0, 0, 0)
        self.layout_main_pane = QtWidgets.QVBoxLayout()
        self.layout_main_pane.setSpacing(0)
        self.layout_main_pane.setContentsMargins(0, 0, 0, 0)

        self.ribbon = ribbon_ui.Ribbon(self)
        self.left_pane = QtWidgets.QWidget()
        self.main_area = QtWidgets.QWidget()

        central = QtWidgets.QWidget()
        central.setLayout(layout_for_ribbon)
        self.setCentralWidget(central)
        layout_for_ribbon.addWidget(self.ribbon)
        layout_for_ribbon.addLayout(layout_for_left_pane)
        layout_for_left_pane.addWidget(self.left_pane)
        layout_for_left_pane.addLayout(self.layout_main_pane)
        self.layout_main_pane.addWidget(self.main_area)

        self.home_tab = self.ribbon.add_tab("Home")
        self.extras_tab = self.ribbon.add_tab("Extras")
        self.home_tab.home_button = self.home_tab.add_button("Data\n download", "Overview", "images/icons/dusk/icons8-home-64.png")
        self.home_tab.home_button2 = self.home_tab.add_button("Home2\n", "Overview", "images/icons/dusk/icons8-Budget.png")
        self.home_button3 = self.home_tab.add_button("Home3\n", "Overview", "images/icons/dusk/icons8-business-64.png")
        self.investments_tab = self.ribbon.add_tab("Investments")
        self.investments_tab2 = self.ribbon.add_tab("Investments2")
        self.investments_tab3 = self.ribbon.add_tab("Investments3")


        self.left_pane.setFixedWidth(350)
        self.left_pane.setMinimumHeight(200)
        self.left_pane.setObjectName("LeftPane")

        self.main_area.setObjectName("MainArea")

        self.windowMapper = QtCore.QSignalMapper(self)
        # noinspection PyUnresolvedReferences
        # self.windowMapper.mapped.connect(self.set_active_sub_window)

        self.read_and_apply_window_settings()
        self.setUnifiedTitleAndToolBarOnMac(True)
        self.setWindowIcon(QtGui.QIcon('images/icons/abacus.png'))

        self.statusBar().showMessage("Ready")
        self.statusBar().setObjectName("StatusBar")

        self.info_button.raise_()

        self.show()

    def read_and_apply_window_settings(self):
        """
        Read window attributes from settings,
        using current attributes as defaults (if settings not exist.)

        Called at QMainWindow initialization, before show().
        """
        qt_settings = QtCore.QSettings('Sergey.Farin', 'Rekenraam')
        # No need for toPoint, etc. : PySide converts types
        self.restoreGeometry(qt_settings.value("geometry", self.saveGeometry()))
        # self.restoreState(qt_settings.value("saveState", self.saveState()))
        position = qt_settings.value("pos", self.pos())
        if position.x() > (QtWidgets.QDesktopWidget().availableGeometry().width()*0.85):
            position.setX(max(0,
                              QtWidgets.QDesktopWidget().availableGeometry().width()/2
                              - qt_settings.value("size", self.size()).width()/2))
        if position.y() > (QtWidgets.QDesktopWidget().availableGeometry().height()*0.85):
            position.setY(max(0,
                              QtWidgets.QDesktopWidget().availableGeometry().height()/2
                              - qt_settings.value("size", self.size()).height()/2))
        self.move(position)
        size = qt_settings.value("size", self.size())
        self.resize(size)
        if qt_settings.value("maximized", self.isMaximized()) == "true":
            self.showMaximized()

    def write_window_settings(self):
        """
        Save window attributes as settings.
        Called when window moved, resized, or closed.
        """
        qt_settings = QtCore.QSettings('Sergey.Farin', 'Rekenraam')
        qt_settings.setValue("geometry", self.saveGeometry())
        qt_settings.setValue("maximized", (self.isMaximized()))
        if not self.isMaximized():
            qt_settings.setValue("pos", self.pos())
            qt_settings.setValue("size", self.size())

    def close(self):
        self.write_window_settings()
        import sys
        sys.exit()

    def closeEvent(self, *args, **kwargs):
        self.write_window_settings()
        import sys
        sys.exit()

    def moveEvent(self, *args, **kwargs):
        self.write_window_settings()

    def resizeEvent(self, *args, **kwargs):
        self.write_window_settings()
        self.info_button.move(self.width()-32, 4)
