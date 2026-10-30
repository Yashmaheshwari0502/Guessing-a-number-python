import random

count=0
condidtion=True
num=random.randint(1,100)

while(condidtion):
    value=int(input("Enter the Number\n"))
    if(value<num):
        print("Guess Bigger")
    elif(value>num):
        print("Guess Smaller")
    else:
        print("You have guessed the number in ",count," times")
        print("the number was",num)
        condidtion=False
    count+=1
            
    