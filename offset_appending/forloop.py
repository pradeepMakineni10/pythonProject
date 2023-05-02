
def concept_loop():
    # fruits = ['Apple', 'Peach', 'Pears']
    # for fruit in fruits:
    #     print(fruit)

    list_numbers = [180, 124, 165, 173, 189, 169, 146]

    total_height = 0
    for heights  in list_numbers:
        total_height += heights
    print(total_height)

    length = 0
    for average in list_numbers:
        print(average)
        length += 1
    print(length)

    total  = (total_height/length)
    print(round(total))
    return
