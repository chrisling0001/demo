def work():
    print("I'm working, it's a low-paid job, I hate it")

def wrapper(func):
    def inner(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return inner

#下面三行等价于 work = wrapper（work）
@wrapper   
def work():
    print("I'm working")

