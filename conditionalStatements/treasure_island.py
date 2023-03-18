# Treasure Island

def treasure_island():
    print("welcome to Treasure island ")
    navigation = input("what way would u like to travel left or right? ")
    if navigation == 'left':
        print("wait for the next step")
        decision = input("do you want to swim or wait? ")
        if decision == 'wait':
            door_color = input("which color door do you want to exit Red, Blue or Yellow? ")
            if door_color == 'yellow':
                print("you are the winner")
            else:
                print("your game over")
        else:
            print("your game over")
    else:
        print("your game over")
