import random


def random_values():

# pull random integer
    random_integer = random.randint(1, 10)
    print(random_integer)

# pull random float values
    random_float = random.random()
    print(random_float)

    random_side = random.randint(1, 100)
    if random_side % 2 == 0:
        print(f'even number {random_side}')
        print('Heads')
    else:
        print('Tails')
        print(f'odd number {random_side}')