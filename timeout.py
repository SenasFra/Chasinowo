import time

def wait(second):
    temp = time.time()
        
    while time.time() - temp < second:
        print(time.time() - temp)
        
    return True

