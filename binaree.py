from tkinter import *

window = Tk() #instantiate the instance of a window
window.geometry("800x500") #dimension of the window
window.minsize(800, 500)
window.maxsize(800, 500)
window.title("binary game")
window.config(background="#212121")

main_label = Label(window, text="number",
                   font=('Arial', 40),
                   bg='#A9A9A9',
                   padx=20,
                   pady=10) #set master to window
main_label.place(x=325, y=70) #add label to window

display_label = Label(window, text="hehe",
                      font=('Arial', 28),
                      bg = '#7F89C1',
                      padx=20,
                      pady=10)
display_label.place(x=635, y=300)



class CreateButton:

    def __init__(self, window, powx, ro, col):
        self.count = 0
        self.button = Button(window, text=powx, bg='red', fg='white', padx=10, pady=5, command=self.click)
        self.button.place(x=col * 80, y=ro * 45)

    def click(self):
        if self.count%2==0:
            self.button.configure(bg='green', fg='white')
        else:
            self.button.configure(bg='red', fg='white')
        self.count += 1


for i in range(7, -1, -1):
    CreateButton(window, powx=str(2**i), ro=i+(7-i), col=7-i)


# Center the buttons in the window
for i in range(10):
    window.grid_columnconfigure(i, weight=1)


window.mainloop() #displays the window