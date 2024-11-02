import threading
import time
lock1 =threading.Lock()
lock2 =threading.Lock()

def task1():
    print("Task1 Trying to acquire lock1..")
    lock1.acquire()
    print("Task1:Acquired lock1")
    time.sleep(1)

    print("Task1: Trying to  acquire lock2..")
    lock2.acquire()
    print("Task1:Acquired lock2")

    lock2.release()
    lock1.release()
    print("Task1:Released lock1 and lock2")


def task2():
    print("Task2 Trying to acquire lock1..")
    lock1.acquire()
    print("Task2:Acquired lock1")
    time.sleep(1)

    print("Task2: Trying to  acquire lock2..")
    lock2.acquire()
    print("Task1:Acquired lock2")

    lock2.release()
    lock1.release()
    print("Task2:Released lock1 and lock2")

#Not the same order can cause deadlock
# def task2():
#     print("Task2: Trying to acquire lock2..")
#     lock2.acquire()
#     print("Task2:Acquired lock2")
#     time.sleep(1)

#     print("Task2: Trying to acquire lock1..")
#     lock1.acquire()
#     print("Task 2:Acquired lock1")

#     lock1.release()
#     lock2.release()
#     print("Task2:Released lock2 and lock1")

thread1=threading.Thread(target=task1)
thread2=threading.Thread(target=task2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()