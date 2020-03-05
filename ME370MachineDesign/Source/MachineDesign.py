import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Harrison, you are homeless"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
root.title("Wassup")
lbl = tk.Label(root, text="John Sucks", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)
# photo = tk.
# root.geometry('350x200')
# btn = tk.Button(root, text="Click Me")
# btn.grid(column=1, row=0)
root.mainloop()


# app = Application(master=root)
# app.master.maxsize(1000, 400)
# app.mainloop()