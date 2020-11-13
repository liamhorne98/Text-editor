from tkinter import *
from tkinter import filedialog
root = Tk()
root.title('read - write')
root.geometry("500x450")

my_text= Text(root, width=40, height=10)
my_text.pack(pady=20)

def open_txt():
    text_file = filedialog.askopenfile(initialdir="D:/user/Desktop", title="open text", filetypes=(("text Files", "*.txt"),))
    text_file = open(text_file , 'r')
    text_file.read()
    stuff = text_file.read()

    my_text.insert(END, stuff)
    text_file.close()

def delete():
    my_text.delete(1)

mybutton = Button(root, text = "Delete", command = delete)
mybutton.pack(pady = 5)

def save_txt():
    text_file = open('sample.txt', 'w')
    text_file.write(my_text.get(1.0, END))


open_button = Button(root, text="Open Text", command= open_txt)
open_button.pack(pady=20)

save_button= Button(root, text="Save File", command= save_txt)
save_button.pack(pady=20)



root.mainloop()