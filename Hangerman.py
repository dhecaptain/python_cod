import random
from collections import Counter 

someWords=""" apple banana strawberry mango orange grape pineapple apricot lemon coconut watermelon cherry papaya berry"""
someWords=someWords.split(' ')

word=random.choice(someWords)

if __name__=="__main__":
    print('Guess a word ! Hint word is a name of a fruit ')
    
    for i in word:
        
        #for printing the empty space for letters in word
        print('_',end=' ')
    print()
    playing=True
    #list for storing these guessed by the player
    letterGuessed=' '
    chance=len(word)+2