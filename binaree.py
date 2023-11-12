from tkinter import *

window = Tk() #instantiate the instance of a window
window.geometry("800x500") #dimension of the window
window.minsize(800, 500)
window.maxsize(800, 500)
window.title("binary game")
window.config(background="#212121")

main_label = Label(window, text="hello",
                   font=('Arial', 40),
                   bg='#A9A9A9',
                   padx=20,
                   pady=10) #set master to window
main_label.place(x=325, y=30) #add label to window


class CreateButton:

    def __init__(self, window, powx, ro, col):
        self.count = 0
        self.button = Button(window, text=powx, bg='red', fg='yellow', padx=10, pady=5, command=self.click)
        self.button.grid(row=ro, column=col)

    def click(self):
        if self.count%2==0:
            self.button.configure(bg='yellow', fg='red')
        else:
            self.button.configure(bg='red', fg='yellow')
        self.count += 1


for i in range(7, -1, -1):
    CreateButton(window, powx=str(2**i), ro=0, col=7-i)


# Center the buttons in the window
for i in range(10):
    window.grid_columnconfigure(i, weight=1)



'''def click(button):
    global x
    if (x%2==0):
        button.configure(bg="red", fg="yellow")
    else:
        button.configure(bg='yellow', fg='red')
    x += 1

def create_button(powx, col, row):
    button = Button(window, text=powx, bg='red', fg='yellow', padx=10, pady=5)
    button.configure(command= lambda: click(button))  # passing the button reference using lambda
    button.grid(row=row, column=col)
    return button'''

'''buttons = []
for i in range(8):
    button = create_button(str(2 ** i), i + 1, 1)
    buttons.append(button)'''

window.mainloop() #displays the window