import time



def decorator(func):
    def say():
        time_start = time.time()
        func()
        end = time.time() - time_start
        print(end)
    return say
