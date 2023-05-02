


new_height = int(input("Height of the wall"))
new_width = int(input("width of the wall"))
coverage = 5

def paint(height = new_height, width = new_width, cov = coverage):
    number_of_cans = (height * width)/cov
    print(number_of_cans)


    return