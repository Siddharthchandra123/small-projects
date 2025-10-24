import random
import default
from default import *
class Hangman:
    def __init__(self):
        self.logo=logo
        print(logo)
        print("Welcome to Hangman game")
        self.gamestart()
    
    def rules(self):
       
       print("""Rules of game are as follow:
        🕹️ Hangman Game Rules
        - Guess the Word
            A secret word is hidden. Your goal is to guess it one letter at a time.
        - One Letter at a Time
            Type a single letter to make a guess. Only alphabet letters are allowed.
        - Correct Guesses
            If the letter is in the word, all its positions will be revealed.
        - Incorrect Guesses
            If the letter is not in the word, you lose a life.
        - Limited Lives
             You have a limited number of incorrect guesses. Use them wisely!
        - No Repeats
            Letters you’ve already guessed won’t count again. Try something new!
        - Win or Lose
        - You win if you guess all the letters before running out of lives.
        - You lose if your lives reach zero before the word is complete.
        - Optional: Full Word Guess
        Some versions allow you to guess the full word at any time—but be careful, a wrong guess might cost you a life!
""")
    def gamestart(self):
        
        print("Lets start the game","\n")
        self.rules()
        word=random.choice(word_list)

        k=["_"]*len(word)
        print(k)
        a=""
        tries=4
        errors=0
       
        
        while tries>0 and "_" in k:
            x=str(input())

            for x in word:
                for i in range(len(word)):
                    if word[i]==x:
                        k[i]==x
            else:
                tries-=1
                errors+=1
                print("lost 1 life")
                print(error[errors-1])
            print(f"*********************************{tries}/4 lives left********************************")

        if errors==4:
            print(""" 
██       ██████  ███████ ████████ 
██      ██    ██ ██         ██    
██      ██    ██ ███████    ██    
██      ██    ██      ██    ██    
███████  ██████  ███████    ██    
                                  
                                   """)
        
        if tries>0 and a==word:
            print(WON)

Hangman()
        
