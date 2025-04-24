from tkinter import *

root = Tk()

e = Entry(root, width = 50, bg = "blue", fg = "red") ##deklaracija vpisnega polja
e.pack() ##klic polja

def pritisk():
    myLabel = Label(root, text=e.get())
    myLabel.pack()

#moj_gumb = Button(root, text = "moj_gumb",state = DISABLED,padx =50)     #deklaracija 
moj_gumb = Button(root, text="Click Me!", command = pritisk, fg = "blue", bg = "red") #ko kličemo funkcijo pritisk je brez oklepajev -> drugače jo avtomatsko kliče!!!!
moj_gumb.pack()#klic

root.mainloop()
