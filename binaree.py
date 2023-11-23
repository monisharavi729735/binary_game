from tkinter import *
import random

click = 0
sum = 0
score = 0


def random_number():
    global number
    global click
    click += 1

    if click in range(0,3):
        number = random.randint(0, 10)

    elif click in range(3,10):
        number = random.randint(0, 100)

    elif click > 9:
        number = random.randint(0, 256)
    
    submit_button.config(text="Submit")
    equality()
    window.after(1000, lambda: main_label.config(text=number))

    for one_button in all_buttons:
        one_button.reset_to_red()

    return number

def equality():

    global score
    
    try:
        display_number = int(main_label.cget("text"))

        #image1 = PhotoImage(file="right.png")

        #image2 = PhotoImage(file="wrong.png")

        if total_sum == display_number:
            main_label.config(bg='green')
            window.after(1000, lambda: main_label.config(bg='#9500FF'))
            score+=1

        else:
            main_label.config(bg='red')
            window.after(1000, lambda: main_label.config(bg='#9500FF'))
            reset_fn()
            score = 0

        score_label.configure(text=f"Score: {score}")
    
    except ValueError:
        pass



def reset_fn():
    global click
    click = 0
    score = 0
    main_label.config(text="click start")
    submit_button.config(text="Start")
    score_label.config(text="Score: 0")

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


img = PhotoImage(file="gamebg.png")
bg = Label(window, image=img)
bg.pack()


main_label = Label(window, text="click start",
                   font=('Arial', 40),
                   bg='#9500FF',
                   padx=20,
                   pady=10) #set master to window
main_label.place(relx=0.5, rely=0.4, anchor=CENTER) #add label to window

display_label = Label(window, text="",
                      font=('Arial', 28),
                      bg = '#9a4eae',
                      padx=20,
                      pady=10)
display_label.place(relx=0.89, rely=0.66, anchor=CENTER)
window.after(100, summation)


score_label = Label(window, text="Score: 0",
                    font=('Arial', 16),
                    bg="#008080",
                    fg="white",
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
        self.button = Button(window, text=powx, bg='red', fg='white', activebackground="#ff6700", padx=10, pady=5, command=self.click)
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