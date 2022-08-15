def say_hello(age, name="anonymous" ):
    return f'Hello {name}. you are {age} years old'

hello = say_hello(33, "NICO")
print(hello)

def minus(a,b=0):
    return a - b

def r_plus(a,b):
    return a + b

def p_plus(a,b):
    print(a + b)

p_result = p_plus(2,3)
r_result = r_plus(2,3)
r_position_argu_result = r_plus(b=11, a=123)

print(r_position_argu_result)