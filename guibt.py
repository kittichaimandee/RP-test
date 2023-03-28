from tkinter import*
#import tkinter
top = Tk() #create application main window
top.title("โปรแกรมของฉัน") #title of main window
top.geometry("480x640") #create size of main window
lbl_name=Label(top,text="name:")
lbl_name.pack(side=LEFT)

txt_name=Text(top,width=20,height=1)
txt_name.pack(side=LEFT)

btn_cancel=Button(top,text="cancel")
btn_cancel.pack(side=LEFT)

btn_ok=Button(top,text="OK")
btn_ok.pack(side=LEFT)

top.mainloop() #calling event main loop