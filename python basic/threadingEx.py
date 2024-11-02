import threading 
import time 
shared_counter = 0
def increment_counter(): 
    global shared_counter
# Critical section: access and modify the shared counter
    for i in range(1000000):
        shared_counter += 1
    print(f" Thread {threading.current_thread().name} incremented counter to {shared_counter}")
# Create multiple threads
threads = []
for i in range(3):
    thread = threading. Thread(target=increment_counter, name=f" Thread-{i}")
    threads.append(thread)
# Start the threads
for thread in threads:
    thread.start()
# Wait for all threads to finish
for thread in threads:
    thread.join()
print("Final value of shared counter:", shared_counter)