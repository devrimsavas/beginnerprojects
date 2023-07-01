
#an easy hangman game. word list is huge and found in internet.Without word list program returns error. however
#you can prepare your word list as words=[........] and save as words.py and call it.
#main program and word.py should be in same directory
import random #import random module 
from words import words #import a huge word list found in internet
import os #clear screen in case user use cmd


game=True #set the loop true

while game: #game will go on until player exits
    word=random.choice(words) #word list found internet quite huge. pick a random word from list
    while '-' in word or ' ' in word: # we eliminate words with white space or minus sign
        word=random.choice(words) #keep while until random word has no space nor minus sign
    #secret_word=[] #create a list for secret words letter
    player_guess=[] #create a list for player's guess
    used=[] #list for used letters
    secret_word=list(word) #we convert secret_word to a list to make it easier.
    player_guess=['_']*len(word) #we create a list of _ char for player's input.

    print(' '.join(player_guess)) #print out the string made of _ char
    word_len=len(word) #we take the lenght of the secret
    turn=0 #set or reset the turn
    limit_turn=10 #change tour number as you wish
    print()
    print(f'Secret word has {word_len} letters\n')

    while turn<limit_turn: #start turn
        
        user=input('Enter a letter : ') #get players guess
        if user in used: #check if this letter is already entered by player
            print(f'The letter {user} already used')

        else : #if letter was not used before , we put it in used list 
            used.append(user)

        print(f"Used letters: {', '.join(used)}\n") #print out used word list

        if user in word: #check if letter in secret word
            print(f'the letter {user} exists in the secret word')
            for index,letter  in enumerate(secret_word): #search for where this letter in secret word
                if letter==user:
                    player_guess[index]=user

        else:
            turn+=1 #increase turn
            print(f'the letter {user} does not exist in secret word\n')

        print(' '.join(player_guess))
        print(f'\nYou have {limit_turn-turn} turns left')

        if secret_word==player_guess:
            print(f'You found the secret word: {word}')
            break
    if secret_word !=player_guess:
        print(f'\nYou Lost. The secret word was: {word} \n')

    play_again=input('Play Again (y/n): ').strip().lower()
    if play_again !='y':
        break
    else:
        os.system('cls')
