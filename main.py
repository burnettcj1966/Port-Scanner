from datetime import datetime
import time
import gui

def main():

    start_time = time.time()
      
    gui.startGui()

    print("Scanning Started at:" + str(datetime.now()))


if __name__ == "__main__":
    main()