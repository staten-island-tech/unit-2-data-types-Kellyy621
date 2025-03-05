

while True:
        User_input = int(input("number"))
        for i in range (1, 11):
                x = User_input*i
                print (x)
        if (int(User_input)) == 0:
                print ("error, pick another number")
        c = input("number")
        if c == ("exit"):
                break 
