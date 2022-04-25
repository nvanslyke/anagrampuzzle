import random
import sys

words = []

with open("words.txt") as file:
    for line in file:
        words.append(line)

    
print(str(len(words)) + " words uploaded")

def jumble(word):
    indexes = [100]
    for char in range(0, len(word)):
        i = 100
        while i in indexes:
            i = random.randint(0, len(word) -1)
        indexes.append(i)
    indexes.pop(0)
    jumbled = ""

    for c in range(0,len(indexes)):
        jumbled += word[indexes[c]] 

    return jumbled
    
def idk(randword):  
    print()
    print("The word was " + randword + ", do better next time")


def correct():
 print("  _____                         _     _ ")
 print(" / ____|                       | |   | |")
 print("| |     ___  _ __ _ __ ___  ___| |_  | |")
 print("| |    / _ \| '__| '__/ _ \/ __| __| | |")
 print("| |___| (_) | |  | | |  __/ (__| |_  |_|")
 print(" \_____\___/|_|  |_|  \___|\___|\__| (_)")
 print()
 print()                                       
 play()


def solve():
    
    narrowed = []

    print("  ______       _                _______           _       ")
    print(" / _____)     | |              (_______)         | |      ")
    print("( (____   ___ | |_   _ _____    _  _  _  ___   __| |_____ ")
    print(" \____ \ / _ \| | | | | ___ |  | ||_|| |/ _ \ / _  | ___ |")
    print(" _____) ) |_| | |\ V /| ____|  | |   | | |_| ( (_| | ____|")
    print("(______/ \___/ \_)\_/ |_____)  |_|   |_|\___/ \____|_____)")
    print()
    print()                                                      
    anag = input("Enter Anagram: ")

    for i in words:
        if len(i) - 1 == len(anag):
            narrowed.append(i)
    for c in narrowed:
        for char in anag:
            if char not in c:
                narrowed.remove(c)
                break

    print(narrowed)

         


def play():
    
    randword = words[random.randint(0, len(words))]
    randword = randword[0:len(randword)-1].lower()

    wordlen = len(randword)
    anagram = jumble(randword)
    print(anagram)
    guess = input("Guess the word: ")

    if guess == "q":
        sys.exit()

    elif guess.lower() == "idk":
        idk(randword)
    
    elif guess.lower() == randword:
        correct()
    
    elif guess.lower() == "solve":
        solve()

    elif guess.lower() != randword:
        while True:
            if guess.lower() != randword:
                print("Incorrect")
                print()
                print(anagram)
                guess = input("Guess the word: ")
            if guess.lower() == "idk":
                idk(randword)
                break
            if guess.lower() == "q":
                sys.exit()
            if guess.lower() == randword:
                correct()
            if guess.lower() == "solve":
                solve()

            


play()



