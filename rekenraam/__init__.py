"""Main application file - creates application window"""

import os
os.environ["PATH"] += ("C:\\Apps\\Programs\\miniconda3\\envs\\jupyter;" +
                       "C:\\Apps\\Programs\\miniconda3\\envs\\jupyter\\Library\\mingw - w64\\bin;" +
                       "C:\\Apps\\Programs\\miniconda3\\envs\\jupyter\\Library\\usr\\bin;" +
                       "C:\\Apps\\Programs\\miniconda3\\envs\\jupyter\\Library\\bin;" +
                       "C:\\Apps\\Programs\\miniconda3\\envs\\jupyter\\Scripts;" +
                       "C:\\Apps\\Programs\\miniconda3\\envs\\jupyter\\bin;") + os.environ["PATH"]
from PyQt5 import QtCore, QtWidgets
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
