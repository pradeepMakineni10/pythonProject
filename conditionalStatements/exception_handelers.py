

def exceptions():
    x = 5
    y = 2

    try:
        print(x/y)
        k = int(input('type number'))
        print(k)

    except ZeroDivisionError as e:
        print("hey , you cannot divide with zero", e)

    except ValueError as e:
        print("invalid input", e)

    finally:
        print("resource closed")

    print("bye")

exceptions()

def break_statement(x, av):

    i = 1

    while i <= x:
        if i>av:
            print(f"the are limited candies {av}")
            break
        print("candy")
        i+=1

break_statement(10, 5)





