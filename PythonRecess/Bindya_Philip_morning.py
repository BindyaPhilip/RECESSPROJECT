#ContextManager with file management
class FootballManager():
    def __init__(self,filename,mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    def __enter__(self):
        self.file = open(self.filename,self.mode)
        return self.file
    def __exit__(self,exc_type,exc_value,exc_traceback):
        self.file.close()
with FootballManager("file.txt","w") as manager:
    content = manager.write("We manage all football stats")
    print('Writing is done')
#Database connection management using context manager
import sqlite3
from contextlib import contextmanager

@contextmanager
def database_connection(database):
    conn = sqlite3.connect(database)
    try:
        yield conn
    finally:
        conn.close()

# Usage example
database_path = 'employees.db'

with database_connection(database_path) as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees')
    results = cursor.fetchall()
    for row in results:
        print(row)


#multithreading 
import threading
def print_numbers(start,end):
    for num in range(start, end+1):
        print(num)
t1 = threading.Thread(target=print_numbers,args=(2,4))
t2 = threading.Thread(target=print_numbers,args=(3,9))
t1.start()
t2.start()
t1.join()
t2.join()
print("threads are now done executing")


#multithreading with multiprocessing combined
import time
import threading
import multiprocessing

def function_a():
    print("Function A started")
    time.sleep(3)
    print("Function A completed")

def function_b():
    print("Function B started")
    time.sleep(6)
    print("Function B completed")

def run_multithreading():
    t1 = threading.Thread(target=function_a)
    t2 = threading.Thread(target=function_b)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

def run_multiprocessing():
    p1 = multiprocessing.Process(target=function_a)
    p2 = multiprocessing.Process(target=function_b)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

# Run functions concurrently using multithreading
print("Multithreading:")
run_multithreading()

print("-----------------------")

# Run functions concurrently using multiprocessing
print("Multiprocessing:")
run_multiprocessing()

    