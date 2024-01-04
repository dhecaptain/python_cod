import random

num=[1,2,3,4,5,6,7,8,9,0]
cpu=random.choice(num)
guess_limit=3
guess_count=0

while guess_count < guess_limit:
    player=int(input('guess a number: '))
    guess_count +=1
    if player==cpu:
        print("you win!!! You guessed correctly")
        break
    else:
        print('you lose! Try again')
else:
    print('you lost')