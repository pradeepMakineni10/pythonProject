

def fruit():
    # total_fruits = ['strawberries', 'pears', 'peaches', 'blueberries', 'cherries' ]
    # total_vegetables = ['green beans', 'spinach', 'kale', 'tomatoes', 'celery']
    #
    # dirty_dozen = [total_fruits, total_vegetables]
    # print(dirty_dozen)
    # print(dirty_dozen[0][1])
    #
    # print(total_fruits[-2])

    row1 = ['1', '2', '3']
    row2 = ['4', '5', '6']
    row3 = ['7', '8', '9']

    map = [row1, row2, row3]
    print(f"{row1}\n{row2}\n{row3}")
    position = input("what do you to provide")
    horizontal = int(position[0])
    vertical = int(position[1])
    selected_row = map[vertical -1]
    selected_row[horizontal -1] = 'x'

    print(map)
    print(f"{row1}\n{row2}\n{row3}")

    return