from threading import Thread, Event
from time import sleep

event = Event()

def NetworkServerServe(var):
    while True:
        for i in range(len(var)):
            var[i] += 1
        if event.is_set():
            break
        sleep(.5)
    print('Stop printing')


my_var = [1, 2, 3]
t = Thread(target=NetworkServerServe, args=(my_var, ))
t.start()
while True:
    try:
        print(my_var)
        sleep(1)
    except KeyboardInterrupt:
        event.set()
        break
t.join()
print(my_var)