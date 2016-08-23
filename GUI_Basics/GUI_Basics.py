import tkinter

def clear():
    login = ent_login.get()
    passwd = ent_pass.get()
    ent_login.delete(0, 'end')
    ent_pass.delete(0, 'end')
    lbl_info.pack()

window = tkinter.Tk()

window.title('My First GUI Interface')
window.geometry('400x300')
window.wm_iconbitmap('favicon.ico')
window.configure(background='medium sea green')

lbl = tkinter.Label(window, text= "Zwróć uwagę na ikonkę...\n",bg='medium sea green', font=('Helvetica', 16))
lbl_login = tkinter.Label(window, text = 'Login:', bg='medium sea green')
lbl_pass = tkinter.Label(window, text = 'Password:', bg='medium sea green')
lbl_info = tkinter.Label(window, text = '\nSuccessfully logged in!', bg='medium sea green')

ent_login = tkinter.Entry(window)
ent_pass = tkinter.Entry(window, show="*")

btn = tkinter.Button(window, text = "Log in.",fg='medium sea green',bg='dark slate gray', command = lambda: clear())

#in pack() function parameter fill=tkinter.X will make widget fills the axis in window)
#parameter side=tkinter.LEFT will whereas put the widgets next to each other starting from left side)

lbl.pack()
lbl_login.pack()
ent_login.pack()
lbl_pass.pack()
ent_pass.pack()
btn.pack()

window.mainloop()
    
 
