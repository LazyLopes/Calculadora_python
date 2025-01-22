from tkinter import *

# definição de cores
black_color = "#3b3b3b"
white_color = "#feffff"
blue_color = "#38576b"
grey_color = "#ECEFF1"
orange_color = "#FFAB40"

#configiração da janela
window = Tk()
window.title("Calculadora")
window.geometry("300x340")
window.config(bg=black_color)
font = ("Verdana", "8")

# Container da tela
container_screen = Frame(window, width=300, height=60, bg=blue_color)
container_screen.grid(row=0, column=0)

# Container das teclas
container_body = Frame(window, width=300, height=320)
container_body.grid(row=1, column=0)

all_values = ''

#criando função de calculo
def entry_values(input):
    global all_values
    all_values = all_values + str(input)
    
    # passando o valor para a tela
    text_value.set(all_values)
    
def calculate():
    global all_values
    result = eval(all_values)
    text_value.set(str(result))
    all_values = str(result)
    
def clean_screen():
    global all_values
    all_values = ""
    text_value.set("")
    
# Criando a tela
text_value = StringVar()

screen = Label(container_screen, textvariable=text_value, width=18, height=2, padx=7, anchor="e", font=(font, 20))
screen.place(x=0, y=0)

# Criando os botões
b_c = Button(container_body, command = lambda: clean_screen(), text="C", width=20, height=3, bg=grey_color)
b_c.place(x=-4, y=0)
b_prc = Button(container_body, command = lambda: entry_values("%"), text="%", width=9, height=3, bg=grey_color)
b_prc.place(x=146, y=0)
b_div = Button(container_body, command = lambda: entry_values("/"), text="/", width=11, height=3, bg=orange_color)
b_div.place(x=219, y=0)

b_9 = Button(container_body, command = lambda: entry_values("9"), text="9", width=9, height=3, bg=grey_color)
b_9.place(x=0, y=56)
b_8 = Button(container_body, command = lambda: entry_values("8"), text="8", width=9, height=3, bg=grey_color)
b_8.place(x=73, y=56)
b_7 = Button(container_body, command = lambda: entry_values("7"), text="7", width=9, height=3, bg=grey_color)
b_7.place(x=146, y=56)
b_x = Button(container_body, command = lambda: entry_values("*"), text="x", width=11, height=3, bg=orange_color)
b_x.place(x=219, y=56)

b_6 = Button(container_body, command = lambda: entry_values("6"), text="6", width=9, height=3, bg=grey_color)
b_6.place(x=0, y=112)
b_5 = Button(container_body, command = lambda: entry_values("5"), text="5", width=9, height=3, bg=grey_color)
b_5.place(x=73, y=112)
b_4 = Button(container_body, command = lambda: entry_values("4"), text="4", width=9, height=3, bg=grey_color)
b_4.place(x=146, y=112)
b_x = Button(container_body, command = lambda: entry_values("-"), text="-", width=11, height=3, bg=orange_color)
b_x.place(x=219, y=112)

b_3 = Button(container_body, command = lambda: entry_values("3"), text="3", width=9, height=3, bg=grey_color)
b_3.place(x=0, y=168)
b_2= Button(container_body, command = lambda: entry_values("2"), text="2", width=9, height=3, bg=grey_color)
b_2.place(x=73, y=168)
b_1 = Button(container_body, command = lambda: entry_values("1"), text="1", width=9, height=3, bg=grey_color)
b_1.place(x=146, y=168)
b_x = Button(container_body, command = lambda: entry_values("+"), text="+", width=11, height=3, bg=orange_color)
b_x.place(x=219, y=168)

b_0 = Button(container_body, command = lambda: entry_values("0"), text="0", width=20, height=3, bg=grey_color)
b_0.place(x=-4, y=224)
b_dot = Button(container_body, command = lambda: entry_values("."), text=".", width=9, height=3, bg=grey_color)
b_dot.place(x=146, y=224)
b_eq = Button(container_body, command = lambda: calculate(), text="=", width=11, height=3, bg=orange_color)
b_eq.place(x=219, y=224)

# Entradas do teclado
window.bind("1", lambda event: entry_values("1"))
window.bind("2", lambda event: entry_values("2"))
window.bind("3", lambda event: entry_values("3"))
window.bind("4", lambda event: entry_values("4"))
window.bind("5", lambda event: entry_values("5"))
window.bind("6", lambda event: entry_values("6"))
window.bind("7", lambda event: entry_values("7"))
window.bind("8", lambda event: entry_values("8"))
window.bind("9", lambda event: entry_values("9"))
window.bind("0", lambda event: entry_values("0"))
window.bind(".", lambda event: entry_values("."))
window.bind("+", lambda event: entry_values("+"))
window.bind("-", lambda event: entry_values("-"))
window.bind("*", lambda event: entry_values("*"))
window.bind("/", lambda event: entry_values("/"))
window.bind("%", lambda event: entry_values("%"))
window.bind("=", lambda event: calculate())
window.bind("<Return>", lambda event: calculate())
window.bind("c", lambda event: clean_screen())

window.mainloop()