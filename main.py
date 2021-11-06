import sys
import socket
from datetime import datetime


if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Argument Error")

print("Scanning Target: " + target)
print("Scanning Started at:" + str(datetime.now))


try:
    for port in range (1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)


        result = s.connect_ex((target,port))
        if result == 0:
            print("PORT {} IS OPEN".format(port))
        s.close

except KeyboardInterrupt:
    print("Keyboard interrupt")
    sys.exit()
except socket.gaierror:
    print("\n Cannot resolve host")
    sys.exit()
except socket.error:
    print("Server is not responding")
    sys.exit()

    