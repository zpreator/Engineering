
def ShowInfo(message, title="Information"):
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.iconbitmap(default='C:\\Program Files (x86)\\Raylock\\Sandbox\\py-components\\main_logo.ico')
    root.withdraw()
    messagebox.showinfo(title, message)

def ShowError(message, title="Error"):
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.iconbitmap(default='C:\\Program Files (x86)\\Raylock\\Sandbox\\py-components\\main_logo.ico')
    root.withdraw()
    messagebox.showerror(title, message)

def ShowWarning(message, title="Warning"):
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.iconbitmap(default='C:\\Program Files (x86)\\Raylock\\Sandbox\\py-components\\main_logo.ico')
    root.withdraw()
    messagebox.showwarning(title, message)

def AskOkCancel(message, title="Question"):
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.iconbitmap(default='C:\\Program Files (x86)\\Raylock\\Sandbox\\py-components\\main_logo.ico')
    root.withdraw()
    return messagebox.askokcancel(title, message)

def AskRetryCancel(message, title="Question"):
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.iconbitmap(default='C:\\Program Files (x86)\\Raylock\\Sandbox\\py-components\\main_logo.ico')
    root.withdraw()
    return messagebox.askretrycancel(title, message)

def AskYesNo(message, title="Question"):
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.iconbitmap(default='C:\\Program Files (x86)\\Raylock\\Sandbox\\py-components\\main_logo.ico')
    root.withdraw()
    return messagebox.askyesno(title, message)

def AskYesNoCancel(message, title="Question"):
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.iconbitmap(default='C:\\Program Files (x86)\\Raylock\\Sandbox\\py-components\\main_logo.ico')
    root.withdraw()
    return messagebox.askyesnocancel(title, message)

def AskString(message, title="Question"):
    import tkinter as tk
    from tkinter import simpledialog
    root = tk.Tk()
    root.iconbitmap(default='C:\\Program Files (x86)\\Raylock\\Sandbox\\py-components\\main_logo.ico')
    root.withdraw()
    return simpledialog.askstring(title, message, parent=root)

def AskInteger(message, title="Question", minvalue=0, maxvalue=100):
    import tkinter as tk
    from tkinter import simpledialog
    root = tk.Tk()
    root.iconbitmap(default='C:\\Program Files (x86)\\Raylock\\Sandbox\\py-components\\main_logo.ico')
    root.withdraw()
    return simpledialog.askinteger(title, message, parent=root, minvalue=minvalue, maxvalue=maxvalue)

def AskFloat(message, title="Question", minvalue=0.0, maxvalue=100000.0):
    import tkinter as tk
    from tkinter import simpledialog
    root = tk.Tk()
    root.iconbitmap(default='C:\\Program Files (x86)\\Raylock\\Sandbox\\py-components\\main_logo.ico')
    root.withdraw()
    return simpledialog.askfloat(title, message, parent=root, minvalue=minvalue, maxvalue=maxvalue)