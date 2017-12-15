"""Main application file - creates application window"""

from PyQt5 import QtCore, QtWidgets

if __name__ == '__main__':

    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
    QtCore.QCoreApplication.setApplicationName("Fireweed")
    mainWin = mainwindow_ui.MainWindow()
    sys.exit(app.exec_())
