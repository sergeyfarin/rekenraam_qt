"""Main application file - creates application window"""

from PyQt5 import QtCore, QtWidgets, Qt
# noinspection PyUnresolvedReferences
import mainwindow_ui

if __name__ == '__main__':

    import sys

    # QtWidgets.QApplication.setAttribute(Qt.Qt.AA_EnableHighDpiScaling, True)
    # QtWidgets.QApplication.setAttribute(Qt.Qt.AA_UseHighDpiPixmaps, True)
    # QtWidgets.QApplication.setAttribute(Qt.Qt.)

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
    QtCore.QCoreApplication.setApplicationName("Rekenraam")
    mainWin = mainwindow_ui.MainWindow()
    sys.exit(app.exec_())
