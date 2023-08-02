from ipcheck_class import IpCheck
import sys , os , time
from PyQt5.QtWidgets import QApplication


name = ["device01"     ,"device02"     ,"device03"     ,"device04"     ,"device05"    ,"device06"    ,"device07"    ,"device018"    ,"device09"     ,"device10"]
ip =   ["192.168.2.50" ,"192.168.2.51" ,"192.168.2.52" ,"192.168.2.53" ,"192.168.2.54","192.168.2.55","192.168.2.56","192.168.2.251","192.168.2.252","157.237.20.40"]
app = QApplication(sys.argv)
ipcheck = IpCheck(ip = ip,name = name)
sys.exit(app.exec_())

while True :
    for i in range(len(ip)):
        result = os.system(f'ping -n 1 -w 1 {ip[i]}')
        led =  ipcheck.leds[i]
        if result == 0:
            led.turn_on()
        else:
            led.turn_off()
        app.processEvents()
    time.sleep(1)