#Logical oprators

def logical_operator():
    name1 = input("what is your name")
    name2 = input("what is there name")
    name = name1 + name2

    lower_case = name.lower()

    t = lower_case.count('t')
    r = lower_case.count('r')
    u = lower_case.count('u')
    e = lower_case.count('e')

    true = t + r + u + e

    l = lower_case.count('l')
    o = lower_case.count('o')
    v = lower_case.count('v')
    e = lower_case.count('e')

    love = l + o + v + e

    calculator = str(true) + str(love)
    print(calculator)
    love_score = int(calculator)

    if (love_score >= 60) and (love_score <= 100):
        print(f"your love score {love_score}, {name1} and {name2} are like coke and mentos")
    elif (love_score >= 30) or (love_score <= 59):
        print(f"your love score {love_score}, you like each other")
    else:
        print(f"your love score {love_score}, are okay with each other")

    return