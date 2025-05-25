print('You will get three chances to guess the number.')
i=1
number=7
while i<=3:
    guess=input("Enter your guess:")
    if int(guess)==number:
        print('You won. You guessed it correct.')
        break
    else:
        print('Try again.')
        i+=1
else:
    print('Your three chances are over.')
