import threading
import time

class CPUPainter:
    def paintwall(self):
        time.sleep(2)
        print('Wall painted')

    def __init__(self):
        t = threading.Thread(target=self.paintwall)
        t.start()

CPUPainter()
CPUPainter()
CPUPainter()
CPUPainter()