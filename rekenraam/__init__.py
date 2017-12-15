"""Main application file - creates application window"""

from PyQt5 import QtCore, QtWidgets
# noinspection PyUnresolvedReferences
import mainwindow_ui

if __name__ == '__main__':

    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
    QtCore.QCoreApplication.setApplicationName("Rekenraam")
    mainWin = mainwindow_ui.MainWindow()
    sys.exit(app.exec_())
