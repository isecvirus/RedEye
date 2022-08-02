import random
from tkinter.ttk import Label, Frame, Entry, Button, Style

def Securer(_in_, password, background:str='black', access_text:str='Access'):
    r = str(random.randint(10000000000000000000, 99999999999999999999)) # r=random (a random string 20 char length for style)
    style = Style()
    style.configure(r + '.TFrame', background=background)
    style.configure(r + '.TEntry', background=background)
    style.configure(r + '.TButton', background=background)

    Blocker = Label(_in_, background=background, width=_in_.winfo_screenwidth())
    Blocker.place(relx=0.5, rely=0.5, anchor='center', height=_in_.winfo_screenheight())

    PromptFrame = Frame(_in_, style=r + '.TFrame')
    PromptFrame.place(relx=0.5, rely=0.5, anchor='center')

    input = Entry(PromptFrame, style=r + '.TEntry', justify='center')
    input.pack(pady=10)

    def Access():
        if input.get() == password:
            Blocker.destroy()
            PromptFrame.destroy()
            input.destroy()
            access.destroy()
        else:
            input.delete(0, 'end')
    access = Button(PromptFrame, text=access_text, style=r + '.TButton', takefocus=False, cursor='hand2', command=lambda :Access())
    access.pack()