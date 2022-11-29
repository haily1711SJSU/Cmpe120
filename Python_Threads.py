import logging
import threading
import time

def count_up_to_10(name):
    logging.info("Thread %s: starting", name)
    for i in range(11):
        print("Thread %s, count: %s" % (name,i))
        time.sleep(1)
    logging.info("Thread %s: exiting", name)

def count_down_from_10(name):
    logging.info("Thread %s: starting", name)
    for i in range(10,-1,-1):
        print("Thread %s, count: %s" % (name,i))
        time.sleep(1)
    logging.info("Thread %s: exiting", name)

def main():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    thread1 = threading.Thread(target=count_up_to_10, args=(1,))
    thread2 = threading.Thread(target=count_down_from_10, args=(2,))
    thread1.start()
    thread2.start()
    thread2.join() # ends thread2 before thread1
    thread1.join()

main()