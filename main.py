import sys
import socket
from datetime import datetime
from threading import Thread
from queue import Queue
import threading
import time
import IP_Scanner

q = Queue()
target = 0

def scan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
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


def main():

    start_time = time.time()

    IP_Scanner.printNetworkIPs()

    targetIP = input("What IP do you want to target?\n")
    globals()['target'] = socket.gethostbyname(targetIP)

    print("Scanning Target: " + target)
    print("Scanning Started at:" + str(datetime.now()))

    for n in range (10000):
        t = threading.Thread(target=startThreading)
        t.daemon = True
        t.start()

    for worker in range (1,65535):
        q.put(worker)
    

    q.join()

    print ("RUN TIME: ", time.time() - start_time,)



if __name__ == "__main__":
    main()