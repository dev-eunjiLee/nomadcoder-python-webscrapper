"""
타입 및 길이 체크(소스 진행 전 체크 사항)
"""
# type check
def type_check(*numbers) -> bool:
    print(numbers)
    value = True
    for i in numbers:
        try:
            float(i) # number 변경 시도 => number로 변경 불가능한 경우 예외처리로 잡은 후 False 리턴                
        except Exception as e:
            print('예외: ', e)
            value = False
            break
    return value

# length check and return new list
def split_list(*list) -> list:
    split_length=2
    args = []
    if(len(list) > split_length):
        print(f"인자의 개수가 많아 앞의 {split_length}개의 인자로만 계산을 진행합니다")    
        args.append(list[0])
        print(list[1])
        args.append(list[1])
    else:
        args = list
    return args    

"""
실제 계산 로직
"""
# plus - 여러 인자를 list로 받은 후 해당 값을 다 더한 값을 리턴
def plus(*args) -> float:
    # type check
    type_check_result = type_check(*args)
   
    # type check 결과에 따라 결과값 리턴
    if(type_check_result == False):
        print('check your args')
    else:
        value = 0
        print(args)
        for i in args:
            value += float(i)
        return value

# minus - 러 인자를 list로 받은 후 해당 값을 다 뺀 값을 리턴
def minus(*args) -> float:
    # type check
    type_check_result = type_check(*args)
   
    # type check 결과에 따라 결과값 리턴
    if(type_check_result == False):
        print('check your args')
    else:
        value = 0
        print(args)
        for i in args:
            value -= float(i)
        return value



# times
def times(*args) -> float:
    # type check
    type_check_result = type_check(*args)

    #type check 결과에 따라 결과값 리턴
    if(type_check_result == False):
        print('check your args')
    else:
        value = 1
        for i in args:
            value *= float(i)
        return value

# devision
def devision(*args) -> float:
    # type check
    type_check_result = type_check(*args)

    #type check 결과에 따라 결과값 리턴
    if(type_check_result == False):
        print('check your args')
    else:
        value = 1
        for i in args:
            value /= float(i)
        return value

# negation(부정)
def devision(*args) -> list:
    # type check
    type_check_result = type_check(*args)

    #type check 결과에 따라 결과값 리턴
    if(type_check_result == False):
        print('check your args')
    else:
        value = []
        for i in args:
            value.append(-float(i))
        return value

# remainder(나머지)
def remainder(*args) -> float:
    
    # length check
    args =split_list(*args)
    print('remainder new args: ', args)
    # type check
    type_check_result = type_check(*args)

    #type check 결과에 따라 결과값 리턴
    if(type_check_result == False):
        print('check your args')
    else:
        value = []
        for i in args:
            value.append(-float(i))
        return value

# power(거듭제곱)
def power(*args) -> float: 
     # length check
    args =split_list(*args)

     # type check
    type_check_result = type_check(*args)

    #type check 결과에 따라 결과값 리턴
    if(type_check_result == False):
        print('check your args')
    else:
        return float(args[0]) ** float(args[1])

"""
함수 호출
"""
# 실제 처리
input = [2,3,4,"5.5", "-7"]

plus_result = plus(*input)
print('plus_result: ', plus_result)

minus_result = minus(*input)
print('minus_result: ', minus_result)

times_result = times(*input)
print('times_result: ', times_result)

devision_result = devision(*input)
print('devision_result: ', devision_result)

remainder_result = remainder(*input)
print('remainder_result: ', remainder_result)

power_result = power(*input)
print('power_result: ', power_result)