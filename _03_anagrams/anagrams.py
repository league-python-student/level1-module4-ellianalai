"""
Create an anagram game!
"""
import random
import tkinter as tk
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
        self.text = tk.Entry(self)
        self.text.place(relx = 0.1, rely=0.3, relheight = 0.1, relwidth = 0.7)

        self.b=tk.Button(self, text = 'Get New Word', font =('Courier New', 10, 'bold'))
        self.b.place(relx = 0.7, rely=0.1, relheight = 0.2, relwidth = 0.2)
        self.b.bind('<ButtonPress>', self.word)
        self.label = tk.Label(self, text = 'Label is here', font = ('Courier New', 13, 'bold'))
        self.label.place(relx = 0.1, rely=0.5, relheight = 0.15, relwidth = 0.8)

        self.label_1 = tk.Label(self, text='Guess the anagram for the word: ', font=('Courier New', 10, 'bold'))
        self.label_1.place(relx=0.07, rely=0.16, relheight=0.1, relwidth=0.45)

        self.label_2 = tk.Label(self, text='', font=('Courier New', 10, 'bold'))
        self.label_2.place(relx=0.47, rely=0.16, relheight=0.1, relwidth=0.2)
    #How do I make the word reset after I click Get New Word?
    #Right now it only does it once.
    def word(self, event):
        for key in self.word_anagrams:
            self.label_2.configure(text = key)



if __name__ == '__main__':
    a = anagram()
    a.title('hi')
    a.geometry('700x200')
    a.mainloop()






















