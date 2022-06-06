import time
import threading

def myfunc(name):
    print(f"MYFUNC STARTED WITH {name}")
    time.sleep(3)
    print("MYFUNC ENDED")

if __name__ == "__main__":
    print("main sarted")
    t = threading.Thread(target=myfunc, args=["MULTITHREADING"])
    t.start()
    print("main ended")
