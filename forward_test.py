from picarx import Picarx
import time

def forward_test():
    px = Picarx()
    
    px.forward(100)
    time.sleep(1)
    
    px.backward(100)
    time.sleep(1)
    px.stop()
    
forward_test()