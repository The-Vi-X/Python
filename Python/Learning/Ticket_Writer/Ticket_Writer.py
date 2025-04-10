from tkinter import *



#----------<MAIN>----------
if __name__ == "__main__":
    #Itin window
    root = Tk()
    root.title("Ticket Writer")
    lbl1 = Label(root, text="Hello World!", font=("Times New Roman",21,"bold"))
    lbl1.grid(column=0,row=0)
    btn1 = Button(root, text="DONT PRESS THE BUTTON", command=clicked)
    btn1.grid(column=0,row=0)

    root.mainloop()
#----------<MAIN>----------
