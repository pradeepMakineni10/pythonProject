# Excercise:-
def pizza_order():
    pizza_size = input("what size pizza would you like to order 'S','M' or 'L'? ")
    add_pepperoni = str(input("would u like to add pepperoni Y or N? "))
    extra_cheese = str(input("would like to add extra cheese Y or N? "))

    if pizza_size == 'S':
        bill = 15
        print(f"small pizza & {bill}")
    elif pizza_size == 'M':
        bill = 20
        print(f"medium pizza & {bill}")
    else:
        bill = 25
        print(f"large pizza & {bill}")

    if add_pepperoni == 'Y':
        if pizza_size == 'S':
            pepperoni = bill + 2
            print(f'total price with pepronin {pepperoni}')
        elif pizza_size == 'M':
            pepperoni = bill + 3
            print(f'total price with pepronin {pepperoni}')
        elif pizza_size == 'L':
            pepperoni = bill + 3
            print(f'total price with pepronin {pepperoni}')
    else:
        print("pepperoni nt required")
        pepperoni = bill

    if extra_cheese == 'Y':
        total_cheese = pepperoni + 1
        print(total_cheese)
    else:
        total_bill = pepperoni
        print(total_bill)

    return #pizza_order()
