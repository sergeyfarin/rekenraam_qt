# customize Title bar
# dotpy.ir
# iraj.jelo@gmail.com
import sys
from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import Qt
import qtawesome as qta
# from PySide2 import QtWinExtras


class TitleBar(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        css = """
        QWidget{
            Background: #AA00AA;
            color:white;
            font:12px bold;
            font-weight:bold;
            border-radius: 1px;
            height: 11px;
        }
        QDialog{
            Background-image:url('img/titlebar bg.png');
            font-size:12px;
            color: black;

        }
        QToolButton{
            Background:#AA00AA;
            font-size:11px;
        }
        QToolButton:hover{
            Background: #FF00FF;
            font-size:11px;
        }
        """
        self.setAutoFillBackground(True)
        self.setBackgroundRole(QtGui.QPalette.Highlight)
        self.setStyleSheet(css)
        self.minimize = QtWidgets.QToolButton(self)
        self.minimize.setIcon(QtGui.QIcon(qta.icon('fa.window-minimize', color='white')))
        self.maximize = QtWidgets.QToolButton(self)
        self.maximize.setIcon(QtGui.QIcon(qta.icon('fa.window-maximize', color='white')))
        close = QtWidgets.QToolButton(self)
        close.setIcon(QtGui.QIcon(qta.icon('fa.window-close', color='white')))
        self.minimize.setMinimumHeight(10)
        close.setMinimumHeight(10)
        self.maximize.setMinimumHeight(10)
        label = QtWidgets.QLabel(self)
        label.setText("Window Title")
        self.setWindowTitle("Window Title")
        hbox = QtWidgets.QHBoxLayout(self)
        hbox.addWidget(label)
        hbox.addWidget(self.minimize)
        hbox.addWidget(self.maximize)
        hbox.addWidget(close)
        hbox.insertStretch(1, 500)
        hbox.setSpacing(0)
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.maxNormal = False
        # noinspection PyUnresolvedReferences
        close.clicked.connect(self.close)
        # noinspection PyUnresolvedReferences
        self.minimize.clicked.connect(self.showSmall)
        # noinspection PyUnresolvedReferences
        self.maximize.clicked.connect(self.showMaxRestore)

    def showSmall(self):
        box.showMinimized()

    def showMaxRestore(self):
        if self.maxNormal:
            box.showNormal()
            self.maxNormal = False
            self.maximize.setIcon(QtGui.QIcon(qta.icon('fa.window-maximize', color='white')))
            print('1')
        else:
            box.showMaximized()
            self.maxNormal = True
            print('2')
            self.maximize.setIcon(QtGui.QIcon(qta.icon('fa.window-restore', color='white')))

    def close(self):
        box.close()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            box.moving = True
            box.offset = event.pos()

    def mouseMoveEvent(self, event):
        if box.moving:
            box.move(event.globalPos()-box.offset)


class Frame(QtWidgets.QFrame):
    def stylizeOnWindows(self, window):
        """
        On Windows, extends the window frame behind the tab bar.
        On other platforms, does nothing.
        Requires the window this ribbon is located in.
        """
        return  # glitches the window out, currently
        # if sys.platform != 'win32': return
        try:

            # return

            from PyQt5 import QtWinExtras
            QtWin = QtWinExtras.QtWin

            window.setAttribute(Qt.WA_TranslucentBackground, True)
            QtWin.extendFrameIntoClientArea(window, 110, 24, 110, 0)

            self._tabBar.setAutoFillBackground(False)
            self._tabLayerWidget.setAutoFillBackground(False)
            self.setAutoFillBackground(False)
        except:
            pass  # fail silently

    def __init__(self, parent=None):
        QtWidgets.QFrame.__init__(self, parent)
        self.m_mouse_down = False
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        css = """
        QFrame{
            Background:  #D700D7;
            color:white;
            font:13px ;
            font-weight:bold;
            }
        """
        self.setStyleSheet(css)
        self.setAttribute(Qt.WA_NoSystemBackground)
        # f = QtWinExtras.QtWin()
        # QtWinExtras.QtWin.extendFrameIntoClientArea(f, self, 100, 100, 100, 100)
        self.stylizeOnWindows(self)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowCloseButtonHint)
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowCloseButtonHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        # self.setAttribute(Qt.WA)
        self.setMouseTracking(True)
        self.m_titleBar = TitleBar(self)
        self.m_content = QtWidgets.QWidget(self)
        vbox = QtWidgets.QVBoxLayout(self)
        vbox.addWidget(self.m_titleBar)
        vbox.setContentsMargins(0, 0, 0, 0)
        vbox.setSpacing(0)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.m_content)
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(0)
        vbox.addLayout(layout)
        # Allows you to access the content area of the frame
        # where widgets and layouts can be added

    def contentWidget(self):
        return self.m_content

    def titleBar(self):
        return self.m_titleBar

    def mousePressEvent(self, event):
        self.m_old_pos = event.pos()
        self.m_mouse_down = event.button() == Qt.LeftButton

    def mouseMoveEvent(self, event):
        x = event.x()
        y = event.y()

    def mouseReleaseEvent(self, event):
        m_mouse_down = False



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    box = Frame()
    box.move(60, 60)
    l = QtWidgets.QVBoxLayout(box.contentWidget())
    l.setContentsMargins(0, 0, 0, 0)
    edit = QtWidgets.QLabel("""I would've did anything for you to show you how much I adored you
But it's over now, it's too late to save our loveJust promise me you'll think of me
Every time you look up in the sky and see a star 'cuz I'm  your star.""")
    l.addWidget(edit)
    box.show()
    app.exec_()
