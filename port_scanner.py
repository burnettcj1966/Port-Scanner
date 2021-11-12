
import sys
import socket
from threading import Thread
from queue import Queue
import threading

q = Queue()
target = 0

def scan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        
        if (port % 10000 == 0): print("BENCHMARK: " + str(port))
        
        if result == 0:
            print("PORT {} IS OPEN".format(port))
        s.close

    except socket.gaierror:
        print("\n Cannot resolve host")
        sys.exit()
    except socket.error:
        print("Server is not responding")
        sys.exit()

def startThreading():
    while True:
        worker = q.get()

        scan(worker)

        q.task_done()
        
        
def startScanningTarget(target):
    globals()['target'] = socket.gethostbyname(target)
    
    for n in range (10000):
        t = threading.Thread(target=startThreading)
        t.daemon = True
        t.start()

    for worker in range (1,65535):
        q.put(worker)
    

    q.join()