import sys
import socket
from datetime import datetime
from threading import Thread
from queue import Queue
import threading
import time

q = Queue()
target = 0

def scan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        if port % 5000 == 0:
            print("BENCHMARK: " + str(port))
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

    if len(sys.argv) == 2:
        globals()['target'] = socket.gethostbyname(sys.argv[1])
    else:
        print("Argument Error")

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