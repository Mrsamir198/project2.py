#we are going to write a program that generates a random numbers and asks the user to guess it.

#if the player's guess is higher than the actual number ,the program displays "lower number please".similarly,if the user's guess is too low ,the program prints"higher number please"
#when the user guessesthe correct number, the program displays the number of guesses the player used to arrive at the number.
#hint the random module.
import random
n = random.randint(1,100)
a= -1
guesses = 1
while(a !=n):
    
    a= int(input("guess the number:"))
    if(a>n):
        print("lower number please")
        guesses +=1
    elif(a<n):
        print("higher number please")
        guesses +=1


print(f"you have guessed the number {n} correctly in {guesses} attempts")            