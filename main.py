from os import name


f = open("info.txt", "r+")
string1 = "Books:"
borrowed = 0
name = str(input("Please enter your name:"))

for x in f:
    if name in x:
        borrowed = x.split(string1,1)[1]
        print(borrowed.strip())
        if (borrowed.strip() <= '3'):
            print("Allowed to borrow")
            break
        else:
            print("Borrowed number of books exceeded")
            break
    else:
        print("New user found!")
        f.write("\nName: " + name + " Books: 0")

f.close()