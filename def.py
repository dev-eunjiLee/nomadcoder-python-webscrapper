def say_hello(who="anonymous"):
    print("Hello", who)

say_hello("NICO")
say_hello()

def plus(a,b):
    return a + b


def minus(a,b=0):
    return a - b

print(plus(3,5))
print(minus(3,5))
print(minus(3))