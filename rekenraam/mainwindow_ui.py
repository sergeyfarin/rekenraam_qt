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

        main_window_layout = QtWidgets.QVBoxLayout()
        main_window_layout.setSpacing(0)
        main_window_layout.setContentsMargins(0, 0, 0, 0)

        self.ribbon = ribbon_ui.Ribbon(self)

        self.home_tab = self.ribbon.add_tab("Home")
        self.extras_tab = self.ribbon.add_tab("Extras")
        self.home_tab.home_button = self.home_tab.add_button("Home", "Overview", "images/icons/color/icons8-home.png")
        self.extras_tab.home_button2 = self.extras_tab.add_button("Home2", "Overview", "images/icons/color/icons8-home.png")
        self.home_button3 = self.home_tab.add_button("Home3", "Overview", "images/icons/color/icons8-home.png")
        self.investments_tab = self.ribbon.add_tab("Investments")

        main_window_layout.addWidget(self.ribbon)

        main_layout = QtWidgets.QHBoxLayout()
        self.left_pane = QtWidgets.QWidget()

        self.left_pane.setFixedWidth(300)
        self.left_pane.setMinimumHeight(200)
        # self.left_pane.setStyleSheet("""background: #EBEDEF;""")
        self.left_pane.setObjectName("LeftPane")
        # left_pane.setStyleSheet(

        self.right_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(self.left_pane)
        main_layout.addLayout(self.right_layout)

        main_window_layout.addLayout(main_layout)

        self.main_area = QtWidgets.QWidget()
        self.main_area.setStyleSheet("background: #FFFFFF")

        self.windowMapper = QtCore.QSignalMapper(self)
        # noinspection PyUnresolvedReferences
        self.windowMapper.mapped.connect(self.set_active_sub_window)


        main_layout.addWidget(self.main_area)

        central = QtWidgets.QWidget()
        central.setLayout(main_window_layout)
        self.setCentralWidget(central)

        self.read_and_apply_window_settings()
        self.setUnifiedTitleAndToolBarOnMac(True)
        self.setWindowIcon(QtGui.QIcon('images/fireweed_ico.png'))

        # self.setStyleSheet("file-icon: url(images/icons/chart_line_reversed.png);")
        self.statusBar().showMessage("Ready")
        self.statusBar().setObjectName("StatusBar")
        self.show()

    def about(self):
        about_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.NoIcon, "About Fireweed",
                            """<h2>Fireweed """ + self.version + """</h2>
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

    def update_menus(self):
        pass

    def update_view_menu(self, add):
        windows = self.main_area.subWindowList()
        if len(windows)+add > 0:
            self.ribbon.cascade_button.setDisabled(False)
            self.ribbon.expand_button.setDisabled(False)
            self.ribbon.arrange_button.setDisabled(False)
            self.ribbon.prev_window_button.setDisabled(False)
            self.ribbon.next_window_button.setDisabled(False)
        else:
            self.ribbon.cascade_button.setDisabled(True)
            self.ribbon.expand_button.setDisabled(True)
            self.ribbon.arrange_button.setDisabled(True)
            self.ribbon.prev_window_button.setDisabled(True)
            self.ribbon.next_window_button.setDisabled(True)

    def read_and_apply_window_settings(self):
        """
        Read window attributes from settings,
        using current attributes as defaults (if settings not exist.)

        Called at QMainWindow initialization, before show().
        """
        qt_settings = QtCore.QSettings('Sergey.Farin', 'Fireweed')
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
        qt_settings = QtCore.QSettings('Sergey.Farin', 'Fireweed')
        qt_settings.setValue("geometry", self.saveGeometry())
        # qt_settings.setValue("saveState", self.saveState())
        qt_settings.setValue("maximized", (self.isMaximized()))
        if not self.isMaximized():
            qt_settings.setValue("pos", self.pos())
            qt_settings.setValue("size", self.size())

    def make_chart(self):
        self.statusBar().showMessage("Not working")
        # self.dialogue = org_chart_from_exchange.old.profor_well_create.Dialogue(self)
        # self.dialogue.setModal(True)
        # self.dialogue.show()

    def active_mdi_child(self):
        active_sub_window = self.main_area.activeSubWindow()
        if active_sub_window:
            return active_sub_window.widget()
        return None

    def set_active_sub_window(self, i):
        if i:
            self.main_area.setActiveSubWindow(self.main_area.subWindowList()[i - 1])

    def close(self):
        # self.main_area.closeAllSubWindows()
        self.write_window_settings()
        import sys
        sys.exit()

    def closeEvent(self, *args, **kwargs):
        # self.main_area.closeAllSubWindows()
        self.write_window_settings()
        import sys
        sys.exit()

    def moveEvent(self, *args, **kwargs):
        self.write_window_settings()

    def resizeEvent(self, *args, **kwargs):
        self.write_window_settings()

    def test(self):
        # self.make_chart_dialog.show()
        # g = self.make_chart_dialog.edit.text()
        # print(g)
        # self.active_mdi_child().chart_name = g
        # self.active_mdi_child().setWindowTitle(g)
        self.active_mdi_child().chart.update_figure()
