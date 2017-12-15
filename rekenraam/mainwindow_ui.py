from PyQt5 import QtGui, QtCore, QtWidgets
# import org_chart_from_exchange.old.profor_well_create
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
        self.setWindowTitle("Fireweed "+self.version)

        # self.setStyleSheet("""background-color:blue;""")

        self.mdi_area = QtWidgets.QMdiArea()
        self.mdi_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.mdi_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)

        # noinspection PyUnresolvedReferences
        self.mdi_area.subWindowActivated.connect(self.update_menus)
        self.mdi_area.setViewMode(QtWidgets.QMdiArea.TabbedView)

        self.mdi_area.setTabsClosable(True)
        self.mdi_area.setTabsMovable(True)
        self.mdi_area.setDocumentMode(True)
        self.mdi_area.setTabShape(QtWidgets.QTabWidget.Rounded)

        self.windowMapper = QtCore.QSignalMapper(self)
        # noinspection PyUnresolvedReferences
        self.windowMapper.mapped.connect(self.set_active_sub_window)

        main_window_layout = QtWidgets.QGridLayout()
        main_window_layout.setSpacing(0)
        main_window_layout.setContentsMargins(0, 0, 0, 0)
        self.ribbon = ribbon_ui.Ribbon(self)
        main_window_layout.addItem(QtWidgets.QSpacerItem(0, 5))
        main_window_layout.addWidget(self.ribbon)
        main_window_layout.addWidget(self.mdi_area)

        self.newWellProductionPlot = QtWidgets.QToolButton()
        self.newWellProductionPlot.setText("New well plot")
        self.newWellProductionPlot.setStatusTip("New well plot")
        self.newWellProductionPlot.setIcon(QtGui.QIcon("images/icons/chart_line_add.png"))
        self.newWellProductionPlot.setIconSize(QtCore.QSize(32, 32))
        self.newWellProductionPlot.setAutoRaise(True)
        self.newWellProductionPlot.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        # noinspection PyUnresolvedReferences
        self.newWellProductionPlot.clicked.connect(self.make_chart)
        self.ribbon.ribbon_home_plot_area_layout.addWidget(self.newWellProductionPlot)

        central = QtWidgets.QWidget()
        central.setLayout(main_window_layout)
        self.setCentralWidget(central)

        self.read_and_apply_window_settings()
        self.setUnifiedTitleAndToolBarOnMac(True)
        self.setWindowIcon(QtGui.QIcon('images/fireweed_ico.png'))

        # self.setStyleSheet("file-icon: url(images/icons/chart_line_reversed.png);")
        self.statusBar().showMessage("Ready")
        # QStatusBar
        # {
        #     background: qlineargradient(
        #         x1: 0, y1: 0, x2: 0, y2: 1, stop: 0  # E6EAEE, stop: 0.75 #C4C9CE, stop: 1.0 #B7BCC1);
        # }

        # self.setStyleSheet("""
        # QTabBar {
        #     background-color: #F0F0F0;
        #     }""")
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
        windows = self.mdi_area.subWindowList()
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
        active_sub_window = self.mdi_area.activeSubWindow()
        if active_sub_window:
            return active_sub_window.widget()
        return None

    def set_active_sub_window(self, i):
        if i:
            self.mdi_area.setActiveSubWindow(self.mdi_area.subWindowList()[i-1])

    def close(self):
        self.mdi_area.closeAllSubWindows()
        self.write_window_settings()
        import sys
        sys.exit()

    def closeEvent(self, *args, **kwargs):
        self.mdi_area.closeAllSubWindows()
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
