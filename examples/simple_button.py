from tkinter import *

root = Tk()

def pritisk():
    myLabel = Label(root, text="pritisnil sem gumb!")
    myLabel.pack()

#moj_gumb = Button(root, text = "moj_gumb",state = DISABLED,padx =50)     #deklaracija 
moj_gumb = Button(root, text="Click Me!", command = pritisk, fg = "blue", bg = "red") #ko kličemo funkcijo pritisk je brez oklepajev -> drugače jo avtomatsko kliče!!!!
moj_gumb.pack()#klic

root.mainloop()
