import tkinter

number = input('How many contacts you want to add ? >>> ')
contacts = []

for i in range(int(number)):
    contact = input(str(i+1)+'. contact\'s name: ')
    contacts += [contact]

window = tkinter.Tk()
window.title('Skype')
window.geometry('300x400')
window.configure(background='sky blue')
window.wm_iconbitmap('skype.ico')

job = tkinter.Label(window, text='\nStaying lazy...',fg='white',bg='sky blue',font=('Helvetica',14))

def call(name):
    job.configure(text='\nCalling '+name+'...')

intro = tkinter.Label(window, text='Click a button to call someone.',fg='white',bg='sky blue', font=('Helvetica',15))
intro.pack()

for con in contacts:
    con_lab = tkinter.Label(window, text='\nClick to phone '+con,fg='white',bg='sky blue')
    con_lab.pack()
    con_but = tkinter.Button(window,text='Call '+con, command=lambda cur_contact = con: call(cur_contact),fg='sky blue',bg='white')
    con_but.pack()

job.pack()
window.mainloop()


