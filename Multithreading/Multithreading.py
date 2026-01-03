import threading
import time

def print_number():
    for i in range(10):
        time.sleep(2)
        print(f"Number {i}")
        
def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter {letter}")
        
#create 2 threads
t1 = threading.Thread(target=print_number)
t2 = threading.Thread(target=print_letter)

t=time.time()
#start the threads
t1.start()
t2.start()

## wait for thread complete 
t1.join()
t2.join()

finished_time=time.time()-t
print(finished_time)