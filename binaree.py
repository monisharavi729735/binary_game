from tkinter import *
import random

click = 0
sum = 0

def random_number():
    global number
    global click
    click += 1

    if click > 0:
        submit_button.config(text="Submit")
        number = random.randint(1, 255)
        main_label.config(text=number)
        
        for one_button in all_buttons:
            one_button.reset_to_red()

        return number

def equality(number):
    try:
        global total_sum

        if total_sum == number:
            main_label.config(bg='green')
            window.after(3000, lambda: main_label.config(bg='#6A85A9'))
        else:
            main_label.config(bg='red')
            window.after(3000, lambda: main_label.config(bg='#6A85A9'))
    
    except:
        isinstance(number,str)



def reset_fn():
    global click
    click = 0
    main_label.config(text="click start")
    submit_button.config(text="Start")

    for one_button in all_buttons:
        one_button.reset_to_red()

def summation(): #amazinggggg function
    global total_sum
    total_sum = 0
    for one_button in all_buttons:
        total_sum += one_button.get_value()
    display_label.config(text=str(total_sum))
    window.after(100, summation) #something new
    

window = Tk() #instantiate the instance of a window
window.geometry("800x500") #dimension of the window
window.minsize(800, 500)
window.maxsize(800, 500)
window.title("binary game")
window.config(background="#212121")
'''img = PhotoImage(file="bgimg.png")
bg = Label(window, image=img)
bg.pack()'''


main_label = Label(window, text="click start",
                   font=('Arial', 40),
                   bg='#6A85A9',
                   padx=20,
                   pady=10) #set master to window
main_label.place(relx=0.5, rely=0.4, anchor=CENTER) #add label to window

display_label = Label(window, text="",
                      font=('Arial', 28),
                      bg = '#7F89C1',
                      padx=20,
                      pady=10)
display_label.place(relx=0.89, rely=0.66, anchor=CENTER)
window.after(100, summation)


score_label = Label(window, text="Score: 0",
                    font=('Arial', 16),
                    bg="#889986",
                    padx=20,
                    pady=10)
score_label.place(x=30, y=25)

submit_button = Button(window, text="Start",
                     font=('Arial', 16),
                     bg = '#01814D',
                     fg = 'white',
                     activebackground='#02AB72',
                     padx=10,
                     pady=5,
                     command= random_number)
submit_button.place(relx=0.5, rely=0.82, anchor=CENTER)

reset_button = Button(window, text="Reset",
                      command=reset_fn,
                      font=('Arial', 16),
                      bg = '#C62828',
                      fg = 'white',
                      activebackground='#E53935',
                      padx=10,
                      pady=5)
reset_button.place(x=690, y=25)



class CreateButton:

    def __init__(self, window, powx, ro, col):
        self.count = 0
        self.powx = powx
        self.button = Button(window, text=powx, bg='red', fg='white', activebackground="orange", padx=10, pady=5, command=self.click)
        self.button.place(x=25 + col*80, y=ro * 45)

    def click(self):
        if self.count%2==0:
            self.button.configure(bg='green', fg='white')
        else:
            self.button.configure(bg='red', fg='white')
        self.count += 1

    def reset_to_red(self):
        self.count = 0
        self.button.configure(bg='red', fg='white')

    def get_value(self):
        if self.count%2==1:
            return int(self.powx)
        else:
            return 0


all_buttons = []

for i in range(7, -1, -1):
    one_button = CreateButton(window, powx=str(2**i), ro=i+(7-i), col=7-i)
    all_buttons.append(one_button)

# Center the buttons in the window
for i in range(10):
    window.grid_columnconfigure(i, weight=1)


window.mainloop() #displays the window