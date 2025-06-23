#Guess The Number Correctly

import random
n=random.randint(1,100)
a=-1
guesses=1
while(a!=n):
    a=int(input("Guess the number plz : "))
    if(a<n):
        print("Higher number plz!!")
        guesses+=1
    elif(a>n):
        print("lower no. plz!!")
        guesses+=1
print(f"You guessed the number {n} correctly in {guesses} attempts.")