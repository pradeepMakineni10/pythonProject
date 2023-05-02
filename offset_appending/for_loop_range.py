import random
import string
import getpass
def range_list():

    total = 0
    for number in range(1, 101):
        total += number
    print(total)

#even number from 1 to 100

    total1 = 0
    for number in range(2, 101, 2):
        number += total1
        print(number)

# odd number from 1 to 100

    total2 = 0
    for number1 in range(1, 101,2):
        number1 += total2
        print(number1)

# even number modulo method

    total3 = 0
    for number in range(1, 101):
        if number % 2 == 0:
            total3 += number
            print(total3)

# fizzBuzz quiz test

    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("fizzBuzz")
        elif number % 3 == 0:
            print("fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

# final project on password generator:-

    lower_case = list(string.ascii_lowercase)

    numbers = list(string.digits)
    keystrokes = list(string.punctuation)

    nr_letters = int(input("how many letters do you want"))
    nr_symbols = int(input('how many symbols you want'))
    nr_numbers = int(input('how many numbers do you want to choose'))

    password = ""

    for char in range(1, nr_letters + 1):
        lower_case_vales = random.choice(lower_case)
        password += lower_case_vales

    print(password)

    for num in range(1, nr_numbers + 1):
        pas_numbers = random.choice(numbers)
        password += pas_numbers

    print(password)

    for sym in range(1, nr_symbols + 1):
        sym_numbers = random.choice(keystrokes)
        password += sym_numbers

    final_password = list(password)
    random.shuffle(final_password)
    print(final_password)




    return

