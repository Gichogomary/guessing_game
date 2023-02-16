#this program demonstrates a guessing 
#game
#get user input
#generate a random number
#using a while loop
#check if user input is equal to generated number
from random import randint
username = input("what's your name")
print("Hello there"+username+"!")


#generate a random number
random_number = randint(10,50)
counter = 0
while counter < 5:
    user_number = eval(input("enter a number:"))
    counter += 1

    if user_number<random_number:
        print("your guess is too low.")
    elif user_number > random_number:
        print("your guess is too high")
    elif user_number == random_number:
        print("you win!")
        break
print("Game over.")

if  user_number == random_number:
    print("you win!")
else:
    print("game over!the correct number is")
    print(random_number)    
    
  
            
