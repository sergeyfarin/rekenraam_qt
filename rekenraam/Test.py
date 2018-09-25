import sys
from PyQt5.QtWidgets import QApplication, QLabel, QStyleFactory

app = QApplication(sys.argv)
print(QStyleFactory.keys())
f = QStyleFactory.create('Fusion')
app.setStyle(f)
#label = QLabel("Hello World!")
label = QLabel("<font color=red size=40>Hello World!</font>")
label.show()
app.exec_()