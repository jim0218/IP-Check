from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QGridLayout
from pyqt_led import Led
from PyQt5.QtCore import Qt
import os, time, sys

class IpCheck(QWidget):
    def __init__(self, name, ip):
        super().__init__()
        self.name = name
        self.ip = ip
        self.leds = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Ip_Check')
        self.resize(250, 40 * len(self.ip))
        layout = QGridLayout(self)
        for i in range(len(self.ip)):
            led = Led(parent=None, on_color=Led.green, off_color=Led.red, shape=Led.circle)
            label = QLabel(f"{self.name[i]} ({self.ip[i]})")
            layout.addWidget(led, i, 0, alignment=Qt.AlignCenter)
            layout.addWidget(label, i, 1, alignment=Qt.AlignCenter)
            self.leds.append(led)
        self.show()

# if __name__ =='__main__':
    # name = ["device01"     ,"device02"     ,"device03"     ,"device04"     ,"device05"    ,"device06"    ,"device07"    ,"device018"    ,"device09"     ,"device10"]
    # ip =   ["192.168.2.50" ,"192.168.2.51" ,"192.168.2.52" ,"192.168.2.53" ,"192.168.2.54","192.168.2.55","192.168.2.56","192.168.2.251","192.168.2.252","157.237.20.40"] 
    # app = QApplication(sys.argv)
    # ipcheck = IpCheck(name, ip)
    # sys.exit(app.exec_())



