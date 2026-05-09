import random

"Define game title and print the game title for welcoming the game"
game_title = "Word Raider"
print("Welcome to " + game_title +"!!")

"Open txt file for loading in the list of word bank"
wordBank = []

f = open("fiveWordsBank.txt")
for x in f:
    y = x.rstrip()
    wordBank.append(y)

"Select the word to guess"
#option 1
word_to_guess = (random.choice(wordBank))

#option2
"""
randomnum = random.randint(0,(len(wordBank)-1))
word_to_guess = wordBank[randomnum]
print(word_to_guess)
"""
correctLetters = []
misplacedGuess = []
incorrectGuess = []
max_turns = 5
theNumOfTurnsMade = 0


"Print the current game state"

while  max_turns > theNumOfTurnsMade:
    print("The words has " +str(len(word_to_guess))+" letters.")
    print("You have "+ str(max_turns-theNumOfTurnsMade)+" turns left.")
    print("Please guess a word with "+ str(len(word_to_guess))+" letters")
    
    user_guess = input().lower()
    
    if len(user_guess)!=len(word_to_guess) or user_guess.isalpha()!=True:
        print("The length is incorrect or the entered word contains a symbol or non-letter character.")
        print("Please guess again")
        continue
    
    index = 0
    for c in user_guess:
        if c == word_to_guess[index]:
            if c in correctLetters:
                index+=1
                continue
            correctLetters.append(c)

        elif c in word_to_guess:
            if c in misplacedGuess:
                index+=1
                continue
            elif c != word_to_guess[index] and c not in misplacedGuess:
                misplacedGuess.append(c)

        else:
            if c not in incorrectGuess:
                incorrectGuess.append(c)

        index+=1
    if user_guess!= word_to_guess:
        
        print("Correct letters are ",correctLetters)
        print("Misplaced letters are ",misplacedGuess)
        print("Incorrect letters are ",incorrectGuess)
        print()

        theNumOfTurnsMade+=1

    elif user_guess == word_to_guess:
        print("Congratulations! You guessed correctly!")
        break
    
"After using all tursns, print out 'Game over'"
if theNumOfTurnsMade == max_turns:
    print("Game Over! See you again!")
    

        
        
            
        
        
    
        
    
    



