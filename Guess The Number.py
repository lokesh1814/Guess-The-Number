# Guess The Number Game
"""You have to make a program which will hide a variable with value integer and then allow the user to find that integer
value by giving him only 5 chances to find it. If he finds the number print "Congratulations! You have guessed properly"
with the numbers of turn he takes to find that number"""
a = 10 # number to find
number_of_guess = 0

while (True):
    print("Number of guesses >", number_of_guess)
    guess_number = int(input("Guess a number: "))

    if(guess_number==a):
        print("Congrats! You Won")
        number_of_guess = number_of_guess + 1
        break
    if(number_of_guess==5 ):
        print("You have reached your guess limit \n You Loose")
        exit()

    elif(guess_number<10 and guess_number<20):
        print("You are almost near to it \n\t Try Again")
        number_of_guess = number_of_guess + 1
        continue

    elif(guess_number>20 and guess_number<50):
        print("You are near but still so far \n\t Try Again")
        number_of_guess = number_of_guess + 1
        continue

    else:
        print("You are so far....")
        number_of_guess = number_of_guess + 1
        continue
