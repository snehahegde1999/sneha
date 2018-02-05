import random #import the random function to generate the numbers to play the game
cocount=0 #position of die starts from initial zero
r=r=0 #initialize random number to zero
while count<=100: #check the condition
    roll=input("press r to the roll dice")
    if roll=='r': #compare roll with r
        r =random.randint(1,6) #this can generate values from 1 to 6
        count=count+r #increment count value by r variable
        print ("your random number is ",r)
        print ("your count",count) 
        print(input("print any key to exit program")) 
    if  count==38:
        count=9
        print("you have biten by snake")
        print("your count is",count)
    elif count== 2:
        count=11
        print ("you have bitan by snake")
        print ("your count is ",count)
    elif count==13:
        count=34
        print("you have to climb ladder")
        print("your count is",count)
    elif count==4:
        count=25
        print("you have bitan by snake")
        print("your count is",count)
    elif count==8:
        count=37
        print ("you have to climb the ladder")
        print("your count is",count)
    elif count==40:
        count=68
        print("you have to climb the ladder")
        print("your count is",count)
    elif count==46:
         count=65
         print("you have biten by snake")
         print("your count is",count)
    elif count==52:
         count=81
         print("you have to climb the ladder")
         print("your count is",count)
    elif count==70:
         count=89
         print("you have biten by snake")
         print("your count is",count)
    elif count==76:
         count=97
         print("you have to climb the ladder")
         print("your count is ",count)
    elif count==64:
         count=93
         print("tou have biten by snake")
         print("your count is",count)
               
              
    

    
    
