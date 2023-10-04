print("Handling file exceptions")
try:
    with open('sample.txt','r') as f:
        text = f.read()
except FileNotFoundError:
    text = "file not found"
print(text)

try:
    f = open(r"C:\Users\Admin\Desktop\Goa\IMG_3563.jpeg",'rb')
    f2 = open(r"C:\Users\Admin\Desktop\cpyimg.jpeg","wb")
    f2.write(f.read())
    f.close()
    f2.close()
    print(f.closed)
    print(f2.closed)
    print("copy successful")
except FileNotFoundError:
    print("The specified file is not found")
finally:
    print("closed successfully")
