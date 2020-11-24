
import os
import time
from threading import Thread

# def timing():
#     t = [30, 1/25]
#     return t

# class worker(Thread):
#     def run(self):
#         t = timing()
#         for x in range(0, t[0]):
#             print(x)
#             time.sleep(t[1])


# class waiter(Thread):
#     def run(self):
#         t = timing()
#         for x in range(0, t[0]):
#             # print(x)
#             time.sleep(t[1])
#             os.system("clear")

# def run():
#     worker().start()
#     waiter().start()

# run()

for x in range(0, 200):
    
    print(x)
    print(x+1)
    time.sleep(1/3)
    os.system("clear")

    