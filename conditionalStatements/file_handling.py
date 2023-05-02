

def file_handle():
    f = open('myData.txt','r')
    print(f.read())

file_handle()

def create_file():
    f1 = open('abc','w')
    f1.write("something")

create_file()

def copy_data_fromfile1():
    f = open('myData.txt', 'r')
    f1 = open('abc', 'w')
    for data in f:
        f1.write(data)

copy_data_fromfile1()

def copy_image():
    f2 = open('image.jpeg', 'rb') #orginal pick
    f3 = open('mypick.jpeg','wb') #copying pick to new file
    for i in f2:
        f3.write(i)
copy_image()



