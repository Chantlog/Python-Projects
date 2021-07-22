import threading, time
print("Start of program")

def sleep5():
    time.sleep(1)
    print("Slept 1------------------------")

def count100():
    for x in range(1,1000000):
        if(x % 127 == 0):
            print(x)

thread1 = threading.Thread(target=sleep5)
thread2 = threading.Thread(target=count100)

thread1.start()
thread2.start()

print("End of Program")