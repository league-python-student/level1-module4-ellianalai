"""
Create an anagram game!
"""
import random
import tkinter as tk
from tkinter import messagebox
class anagram(tk.Tk):
    def __init__(self):
        super().__init__()

# TODO Use this dictionary of anagrams to create an anagrams GUI word game.
#  Look at 'anagrams_game_example.png' in this folder for an example.
        self.word_anagrams = {
            "action": ["cation"],
            "agree": ["eager"],
            "calm": ["clam"],
            "charming": ["marching"],
            "clean": ["lance"],
            "cool": ["loco"],
            "creative": ["reactive"],
            "delight": ["lighted"],
            "earnest": ["eastern", "nearest"],
            "easy": ["ayes", "yeas"],
            "free": ["reef"],
            "great": ["grate"],
            "green": ["genre"],
            "grin": ["ring"],
            "hearty": ["earthy"],
            "idea": ["aide"],
            "ideal": ["ailed"],
            "keen": ["knee"],
            "lively": ["evilly", "vilely"],
            "lovely": ["volley"],
            "merit": ["miter", "remit", "timer"],
            "open": ["nope", "peon", "pone"],
            "prepared": ["dapperer"],
            "quiet": ["quite"],
            "refined": ["definer"],
            "restored": ["resorted", "rostered"],
            "reward": ["drawer", "redraw", "warder", "warred"],
            "rewarding": ["redrawing", "wardering"],
            "right": ["girth"],
            "secure": ["rescue"],
            "simple": ["impels"],
            "smile": ["limes", "miles", "slime"],
            "super": ["puers", "purse"],
            "tops": ["opts", "post", "pots", "spot", "stop"],
            "unreal": ["neural"],
            "wonderful": ["underflow"],
            "zeal": ["laze"]}

#The text field to put your guess in
        self.text = tk.Entry(self)
        self.text.place(relx = 0.5, rely=0.32, relheight = 0.1, relwidth = 0.5)

#The button for getting a new word
        self.b=tk.Button(self, text = 'Get New Word', font =('Courier New', 10, 'bold'))
        self.b.place(relx = 0.7, rely=0.1, relheight = 0.2, relwidth = 0.2)
        self.b.bind('<ButtonPress>', self.word)

#The button to Insert the guess from tbe text field
        self.b_1 = tk.Button(self, text='Insert Guess', font=('Courier New', 10, 'bold'))
        self.b_1.place(relx=0.001, rely=0.3, relheight=0.2, relwidth=0.15)
        self.b_1.bind('<ButtonPress>', self.guess)

#The label where your guesses show up
        self.label = tk.Label(self, text = '', font = ('Courier New', 13, 'bold'))
        self.label.place(relx = 0.1, rely=0.6, relheight = 0.1, relwidth = 0.3)

#A label that just shows text
        self.label_1 = tk.Label(self, text='Guess the anagram for the word: ', font=('Courier New', 10, 'bold'))
        self.label_1.place(relx=0.07, rely=0.16, relheight=0.1, relwidth=0.45)


#The label that shows the word that you have to do an anagram
        self.label_2 = tk.Label(self, text='', font=('Courier New', 10, 'bold'))
        self.label_2.place(relx=0.47, rely=0.16, relheight=0.1, relwidth=0.2)

#A label that just shows text and the number of guesses you have
        self.number_guess = 5
        self.label_3 = tk.Label(self, text='Guesses Remaining: ' + str(self.number_guess), font=('Courier New', 10, 'bold'))
        self.label_3.place(relx=0.2, rely=0.35, relheight=0.1, relwidth=0.25)




    #How do I make the word reset after I click Get New Word?
    #Right now it only does it once.
    def word(self, event):
        self.label.configure(text='')
        list_of_keys = list(self.word_anagrams.keys())
        self.random_word = random.choice(list_of_keys)
        self.a = self.word_anagrams[self.random_word]
        self.label_2.configure(text = self.random_word)
        self.correct = 0


    def guess(self,event):
        t = self.text.get()
        if t in self.a:
            self.correct+= 1
            anagram_guessed = self.label['text'] + t + ','
            self.label.configure(text=anagram_guessed)
        #How am I supposed to say you guessed all anagrams in that word??
        if self.correct == self.a:
            messagebox.showinfo(title = '', message = 'You have guessed all the anagrams!')

        self.number_guess -=1
        self.label_3.configure(text = 'Guesses Remaining: ' + str(self.number_guess))
    #Also, make sure to say if you do not guess all the anagrams in the word in 5 guesses, you lose

if __name__ == '__main__':
    a = anagram()
    a.title('hi')
    a.geometry('700x200')
    a.mainloop()






















