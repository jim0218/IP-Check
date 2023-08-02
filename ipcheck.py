from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel,QGridLayout
from pyqt_led import Led
from PyQt5.QtCore import Qt
import os ,time,sys

name = ["device01"     ,"device02"     ,"device03"     ,"device04"     ,"device05"    ,"device06"    ,"device07"    ,"device018"    ,"device09"     ,"device10"]
ip =   ["192.168.2.50" ,"192.168.2.51" ,"192.168.2.52" ,"192.168.2.53" ,"192.168.2.54","192.168.2.55","192.168.2.56","192.168.2.251","192.168.2.252","157.237.20.40"]

app = QApplication(sys.argv)
widget = QWidget()
layout = QGridLayout()
widget.setLayout(layout)
widget.resize(250,40*len(ip))
widget.setWindowTitle("Ip_Check")
leds = []

for i in range(len(ip)):
    led = Led(parent=None, on_color=Led.green, off_color=Led.red,shape=Led.circle)
    label = QLabel(f"{name[i]} ({ip[i]})")
    layout.addWidget(led, i, 0, alignment=Qt.AlignCenter)
    layout.addWidget(label, i, 1, alignment=Qt.AlignCenter)
    leds.append(led)
widget.show()

while True:
    for i in range(len(ip)):
        result = os.system(f'ping -n 1 -w 1 {ip[i]}')
        # print(f"ip{i}:{result}")
        led =  leds[i]
        if result == 0:
            led.turn_on()
        else:
            led.turn_off()
        app.processEvents() #畫面更新
        if widget.isVisible() is False:  #畫面關閉，結束程式
            break    
    if widget.isVisible() is False:
        break
        sys.exit(app.exec_())
    time.sleep(1)

