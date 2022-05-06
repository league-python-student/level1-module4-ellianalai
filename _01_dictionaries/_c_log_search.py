"""
Log Search using a Id-Name Dictionary
"""

# TODO: Create a dictionary of integers for the keys and strings for the values.
#  Create a GUI app with three buttons. Look at 'log_search_example.png' in this
#  folder for an example of what your program should look like.
#
#  Button 1: Add Entry
#      When this button is clicked, use an input dialog to ask the user
#      to enter an ID number.
#      After an ID is entered, use another input dialog to ask the user
#      to enter a name. Add this information as a new entry to your
#      dictionary.


#  Button 2: Search by ID
#      When this button is clicked, use an input dialog to ask the user
#      to enter an ID number.
#      If that ID exists, display that name to the user.
#      Otherwise, tell the user that that entry does not exist.
#
# Button 3: View List
#      When this button is clicked, display the entire list in a message
#      dialog in the following format:
#      ID: 123  Name: Harry Howard
#      ID: 245  Name: Polly Powers
#      ID: 433  Name: Oliver Ortega
#      etc...
#
# When this is complete, add a fourth button to your window.
# Button 4: Remove Entry
#      When this button is clicked, prompt the user to enter an ID using
#      an input dialog.
#      If this ID exists in the dictionary, remove it. Otherwise, notify the
#      user that the ID is not in the list.
#
import tkinter as tk
from tkinter import simpledialog, messagebox
class dictionary(tk.Tk):
    def __init__(self):
        super().__init__()
        self.dictionary = {}
        self.button= tk.Button(self, text = 'Add', font = ('Courier New', 10, 'bold'))
        self.button.place(relx = 0.1, rely=0.3, relwidth = 0.2, relheight = 0.1)
        self.button.bind('<ButtonPress>', self.add)

        self.button1 = tk.Button(self, text='Search', font=('Courier New', 10, 'bold'))
        self.button1.place(relx=0.3, rely=0.3, relwidth=0.2, relheight=0.1)
        self.button1.bind('<ButtonPress>', self.search)

        self.button2 = tk.Button(self, text='View All', font=('Courier New', 10, 'bold'))
        self.button2.place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.1)
        self.button2.bind('<ButtonPress>', self.view)

        self.button3 = tk.Button(self, text='Remove', font=('Courier New', 10, 'bold'))
        self.button3.place(relx=0.7, rely=0.3, relwidth=0.2, relheight=0.1)
        self.button3.bind('<ButtonPress>', self.remove)

    def add(self, event):
       id = simpledialog.askstring(title ='ID?', prompt = 'Please enter an ID number')
       name = simpledialog.askstring(title = 'Name?', prompt = 'Please enter your name')
       key = id
       value = name
       self.dictionary.update({key:value})
    def search (self,event):
        s = simpledialog.askstring(title = 'Search', prompt = 'Enter an ID number')
        if s in self.dictionary:
            messagebox.showinfo(title= 'Search', message = 'Your Name is ' + self.dictionary[s])
        else:
            messagebox.showerror(title = 'Error', message = 'The ID number does not exist. Sorry (~_~;)')
    def view(self, event):
        m = ''

        for key in self.dictionary:
            m += 'ID: ' + str(key) + ' Name: ' + self.dictionary[key] + '\n'
        messagebox.showinfo(title = 'View', message = m)
    def remove(self,event):
        r = simpledialog.askstring(title = 'Remove?', prompt = 'Enter an ID number')
        if r in self.dictionary:
            del self.dictionary[r]
            messagebox.showinfo(title = 'Remove?', message = 'The ID and name have been removed')
        else:
            messagebox.showerror(title = 'Error', message = 'The ID number does not exist. Sorry (~_~;)')
if __name__ == '__main__':
    d = dictionary()
    d.title('Log Search')
    d.geometry('400x200')
    d.mainloop()
















