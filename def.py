def say_hello(who="anonymous"):
    print("Hello", who)

say_hello("NICO")
say_hello()

def minus(a,b=0):
    return a - b

def r_plus(a,b):
    return a + b

def p_plus(a,b):
    print(a + b)

p_result = p_plus(2,3)
r_result = r_plus(2,3)

print(p_result, r_result)