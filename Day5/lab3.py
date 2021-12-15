#write a program to guress a number between 1 to 9.
import random
targetNum, guessNum = random.randint(1,10),0
while targetNum != guessNum:
    guessNum = int(input("Guess the number: "))
print("Well guessed")
