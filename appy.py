User_input = int(input("number"))
for i in range (1, 11):
          if  User_input > 0:
           for i in range(1, 11):
               x = User_input*i
               print (x)
if User_input == 0:
        print ("error, pick another number")
if User_input == ("exit"):
     print("Game finished!")
