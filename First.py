from tkinter import *   
class Tom:
    top = Tk()  
    top.geometry("500x500")  

#creating a simple canvas  
    c = Canvas(top,bg = "pink",height = "400",width = 400)  

    c.create_line(15, 25, 200, 25)
    c.create_line(300, 35, 300, 200, dash=(5, 3))
    c.create_line(55, 85, 155, 85, 105, 180, 55, 85)
    c.create_rectangle(10, 300, 180, 100,outline="#fb0", fill="#fb0")
    c.pack(fill=BOTH , expand=1)

mainloop()  