import string

fruits = {"apple", "banana", "orange", "cherry", "kiwi", "melon", "strawberry"}
alphabet = list(string.ascii_lowercase)

print("Welcome to Hangman!")
print("Type \"start\" to start the game.")
answer = input(":")

if answer == "start":
    lives = 5
    print("Category: Fruits")
    print("You have ",lives," lives left.")
    wordToGuess = list(fruits.pop())
    lenOfWord = len(wordToGuess)

    # print the guessing line
    i = 0 
    guessingLine = []
    while i < lenOfWord:
        guessingLine.append("_")
        i = i + 1

    print(guessingLine)
    print(alphabet)
    
    # guess
    while lenOfWord != 0:
        print("")
        if lives == 0:
            print("YOU LOSE")
            break
    
        letterGuess = input("Guess: ")
        letterGuess = letterGuess
        
        if letterGuess in alphabet:
            #if the letter is in the string
            if letterGuess in wordToGuess:
                letterIndex = []

                #getting the index/es of the char in the string
                x = 0
                while x < len(wordToGuess):
                    if wordToGuess[x] == letterGuess:
                        letterIndex.append(x)
                    x = x + 1

                #changing the guessing line
                j = 0
                numOfRepititions = len(letterIndex)
                while j < numOfRepititions:
                    guessingLine[letterIndex[j]] = letterGuess
                    j = j +1
                
                lenOfWord = lenOfWord - numOfRepititions
            #if the letter is not in the string
            else:
                lives = lives - 1
                print("WRONG.")
            
            alphabet.remove(letterGuess)
            print("You have ",lives," lives left.")
            print(guessingLine)
            print(alphabet)

        else:
            print("Wrong input./You've already entered this before.")

    if lives !=0:
        print("Congratulations. You've guessed the word correctly.")
