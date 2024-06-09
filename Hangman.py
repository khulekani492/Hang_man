# Project Hangman 
# Aim: tkinter basics
# Author: Khulekani Zondo email: khulekaniszondo6@gmail.com 
# DATE: 06/06/2024

import random
from tkinter import *
from tkinter import ttk


# ASCII art for the stages of the hangman
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = '''  _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                         '''

lives = 6
end_of_game = False

# Create a dict for words to guess attaching values that will serve as clues to the player 
word_list = {
    "Retriever": "otter-like tail",
    "GermanShepherd": "highly trainable",
    "Siberian husky": "wolf-like", 
    "Bulldog": "wrinkled face",
    "Rottweiler": "dense coat that is black",
    "GreatDane": "giant dog"
}

chosen_word = random.choice(list(word_list.keys()))  # Get a random key
value = word_list[chosen_word]
word_length = len(chosen_word) 

display = ["_" for _ in range(word_length)]




root = Tk()        

mainframe = ttk.Frame(root, padding="3 3 12 12",style='Main.TFrame' )
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
style = ttk.Style()
style.configure('Main.TFrame', background='black')
        
user = StringVar()
user_entry = ttk.Entry(mainframe, width=5, textvariable=user)
user_entry.grid(column=1, row=3)

cho_wrd = StringVar()
ttk.Label(mainframe, textvariable=cho_wrd,background='black', foreground='white' ).grid(column=3, row=5)

dis = StringVar()
ttk.Label(mainframe, textvariable=dis,background='black', foreground='white' ).grid(column=1, row=2)

asci_Art = StringVar()
ttk.Label(mainframe, textvariable=asci_Art,background='black', foreground='white').grid(column=3, row=2)

logo_Art = StringVar()
ttk.Label(mainframe, textvariable=logo_Art,background='black', foreground='white' ).grid(column=1, row=1)

intro = StringVar(value="Guess the breed\n Good luck (*_*)")
ttk.Label(mainframe, textvariable=intro,background='black', foreground='white',font=("Helvetica", 16, "bold")  ).grid(column=3, row=1)

loss = StringVar()
ttk.Label(mainframe, textvariable=loss,background='black', foreground='white',font=("Helvetica", 16, "bold")  ).grid(column=2, row=2)

clue = StringVar()
ttk.Label(mainframe, textvariable=clue,background='black', foreground='white',font=("Helvetica", 16, "bold")  ).grid(column=3, row=4)

solution = StringVar()
ttk.Label(mainframe, textvariable=solution, background='black', foreground='white' ).grid(column=2, row=3)



logo_Art.set(logo)
dis.set(display)
clue.set(f"Clue: {value}")
asci_Art.set(stages[6])

#restart the game
def resetgame():
    global chosen_word, value, word_length, display, lives, end_of_game
    chosen_word = random.choice(list(word_list.keys()))  # Get a random key
    value = word_list[chosen_word]
    word_length = len(chosen_word)
    display = ["_" for _ in range(word_length)]
    lives = 6
    end_of_game = False
    logo_Art.set(logo)
    dis.set(' '.join(display))
    clue.set(f"Clue:{value}")
    asci_Art.set(stages[6])
    loss.set("")
    solution.set("")
    user_entry.focus()
    
    
    

def check_guess():
    global lives , end_of_game 
    
    guess = user.get().lower()


    if guess in chosen_word.lower():
        for position in range(word_length):
            if chosen_word[position].lower() == guess:
                display[position] = chosen_word[position]
    else:
        lives -= 1

    # Update display
    dis.set(' '.join(display))
    asci_Art.set(stages[lives])    
    if lives == 2:
           loss.set("2 lives..")

    elif lives == 0:
       loss.set("You lose.")
       solution.set(f"Solution: {chosen_word}")
       
       end_of_game = True
    asci_Art.set(stages[lives])        
    
    if "_" not in display:
        loss.set("You win.")

    user_entry.focus()
    user_entry.delete(0, END)
    return dis.set(' '.join(display))                

  
ttk.Button(mainframe, text="Check", command=check_guess).grid(column=1, row=3, sticky=W)                           
ttk.Button(mainframe, text="Play again", command=resetgame) .grid(column=1, row=4, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

#play_again_button = ttk.Button(mainframe, text="Play Again", command=reset_game)        

user_entry.focus()



root.mainloop()