#nested if/ else condition
height = int(input("what is the height"))
if height >= 120:
    print("you can ride the roller coaster")
    age = int(input("what is the age of a person"))
    if age <= 12:
        print("please pay 7$")
    elif age <= 18:
        print("please pay 10$")
    else:
        print("please pay 12$")
else:
    print("sorry you are not permitted to ride")