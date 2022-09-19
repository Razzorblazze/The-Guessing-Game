from random import randint
print("The Challenge: \n Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are: \n 1. If a player's guess is less than 1 or greater than 100, say 'OUT OF BOUNDS' \n 2. On a player's first turn, if their guess is \n\t * within 10 of the number, return 'WARM!' \n\t * further than 10 away from the number, return 'COLD!' \n 3. On all subsequent turns, if a guess is \n\t * closer to the number than the previous guess return 'WARMER!' \n\t * farther from the number than the previous guess, return 'COLDER!' \n 4. When the player's guess equals the number, tell them they've guessed correctly *and* how many guesses it took!4. When the player's guess equals the number, tell them they've guessed correctly *and* how many guesses it took!4. When the player's guess equals the number, tell them they've guessed correctly *and* how many guesses it took!4. When the player's guess equals the number, tell them they've guessed correctly *and* how many guesses it took!4. When the player's guess equals the number, tell them they've guessed correctly *and* how many guesses it took!4. When the player's guess equals the number, tell them they've guessed correctly *and* how many guesses it took! \n4. When the player's guess equals the number, tell them they've guessed correctly *and* how many guesses it took!")
a = randint(1,100)
print(a)
guesses=[]
x=0
guesses.append(int(input('Enter your first guess')));
dif = abs(guesses[x]-a)
if guesses[x]==a:
    print("Correct Guess")
elif dif <= 10:
    print("Warm")
else:
    print("Cold")
c=0
while guesses[x]!=a:
    guess=0
    x=x+1
    while guess >= 0:
        guess=int(input("Enter Your Guess"))
        c=c+1
        if guess<1 or guess > 100:
            print("Out of Bounds")
        else:
            guesses.append(guess)
            break
    dif=abs(guesses[x]-a)
    predif=abs(guesses[x-1]-a)
    if(guesses[x]==a):
        print("Correct Guess")
        break
    elif dif < predif:
        print("Warmer")
    elif dif > predif:
        print("Colder")

print("No of tries =",c)