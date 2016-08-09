import tkinter

cont1 = {'name':'Marcus Polo', 'phone':'663-123-427','mail':'marcus.polo@gmail.com'}
cont2 = {'name':'Michelle Cargo', 'phone':'700-880-142','mail':'michelle86@yahoo.com'}
cont3 = {'name':'Jan Kowalski', 'phone':'123-456-789','mail':'janek.dzbanek@poczta.onet.pl'}

window = tkinter.Tk()
window.title('Phone Book')
window.geometry('300x300')

info = tkinter.Label(window, text='\nHere I will display contact details.')

def display(cont):
    info.configure(text='\nDetails for '+cont['name']+'\nPhone Number:\n'+cont['phone']+'\nE-mail:\n'+cont['mail'])

start = tkinter.Label(window, text='Click contact to display details.\n')
start.pack()

but1 = tkinter.Button(window, text='Marcus Polo',command=lambda: display(cont1))
but1.pack()

but2 = tkinter.Button(window, text='Michelle Cargo',command=lambda: display(cont2))
but2.pack()

but3 = tkinter.Button(window, text='Jan Kowalski',command=lambda: display(cont3))
but3.pack()

info.pack()

window.mainloop()
