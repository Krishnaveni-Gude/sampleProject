import random
input_char='y'
while(input_char=='y'):
    input_num=random.randint(1,1000)
    guess=int(input("enter your number in the range from 1 to 1000: "))
    counter=1
    while(input_num!=guess):
        diff=abs(guess-input_num)
        if(diff==1):
            print("you are almost closure to the number")
        elif(guess>input_num):
            print("The number you entered is too large..")
        elif(guess<input_num):
            print("The number you entered is too small")
        guess = int(input("enter your number in the range from 1 to 1000: "))
        counter+=1
    print("You got it! you have tried for "+str(counter)+" times")
    input_char=input("Do you want to continue?(y): ")
