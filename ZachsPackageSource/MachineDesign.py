from tkinter import *

class Fatigue:
    def __init__(self, win):
        self.win = win
        self.lbl1=Label(win, text='Number of cycles? (If none, put 0)')

        self.t1=Entry(bd=3)
    
        # self.btn1 = Button(win, text='Add')
        # self.btn2=Button(win, text='Subtract')

        self.lbl1.place(x=100, y=50)
        self.t1.place(x=100, y=100)
        
        # self.lbl2.place(x=100, y=100)
        # self.t2.place(x=200, y=100)

        self.b1=Button(win, text='Enter', command=self.GivenNCycles)
        # self.b2=Button(win, text='Subtract')
        # self.b2.bind('<Button-1>', self.sub)

        self.b1.place(x=100, y=150)
        # self.b2.place(x=200, y=150)

        # self.lbl3.place(x=100, y=200)
        # self.t3.place(x=200, y=200)

    def GivenNCycles(self):
        if self.t1.get() == '0':
            self.lbl1.config(text='>1 loadings (y/n)?')
            self.t1.delete(0, 'end')
        else:
            window2 = Toplevel(root)
    # def add(self):
    #     self.t3.delete(0, 'end')
    #     num1=int(self.t1.get())
    #     num2=int(self.t2.get())
    #     result=num1+num2
    #     self.t3.insert(END, str(result))

    # def sub(self, event):
    #     self.t3.delete(0, 'end')
    #     num1=int(self.t1.get())
    #     num2=int(self.t2.get())
    #     result=num1-num2
    #     self.t3.insert(END, str(result))

    


root=Tk()
mywin=Fatigue(root)
root.title('Fatigue')
root.geometry("400x300+10+10")
root.mainloop()