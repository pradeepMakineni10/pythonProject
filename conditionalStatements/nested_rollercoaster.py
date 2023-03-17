# Excercise:-

def roller_coaster():
    height = int(input("what is the height"))

    if height >= 120:
        print("you can ride the roller coaster")
        age = int(input("what is the age of a person"))
        if age <= 12:
            print("please pay child 7$")
            bill = 7
        elif age <= 18:
            print("please pay teen  10$")
            bill = 10
        elif age <= 55 & age >= 45:
            print("please pay adult 0$")
            bill = 0
            print(f"for {age} bill is free")
        else:
            bill = 12
            print("please pay adult 12$")

    photo = input("would you like to have a photo copy Y or NO?:- ")
    if photo == "Y":
        bill += 3
        print(f"your toal bill {bill}")
    else:
        print("sorry you are not permitted")

    return
