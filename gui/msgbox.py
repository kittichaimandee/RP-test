from tkinter import*
from tkinter import messagebox
root = Tk()
root.geometry('500x500')

#function messagebox .show messagebox
def show_message():
    messagebox.showinfo("Message","Warning!!")
    
btn_show = Button(root,text="Show message",command=show_message)
btn_show.pack(side=LEFT)
root.mainloop()