from tkinter import *

root = Tk()

root.title("Blas DB")
root.call('wm', 'iconphoto', root._w, PhotoImage(file='favicon.ico'))

#CALCULADORA
#pantalla.delete = #Para que elimine lo que hay en la pantalla asi no se acumulan los numeros
# el 0 = indica la posicion 0 en el widget
#END = limpia la pantalla 
def enviarNumero(valor): #Funcion que envia la pulsacion de cada uno de los botones y los muestra en pantalla
    anterior = pantalla.get() #Almacena el numero anterior al nuevo pulsado, para poner numeros de mas de un digito
    pantalla.delete(0, END)
    pantalla.insert(0, str(anterior) + str(valor)) #Y añade el valor
def igual():
    global num2
    num2 = pantalla.get()
    pantalla.delete(0, END)
    if operacion == '+':
        pantalla.insert(0, num1 + float(num2))
    if operacion == '-':
        pantalla.insert(0, num1 - float(num2))
    if operacion == '*':
        pantalla.insert(0, num1 * float(num2))
    if operacion == '/':
        pantalla.insert(0, num1 / float(num2)) 

def resta():
    global num1
    global operacion
    num1 = pantalla.get()
    num1 = float(num1)
    pantalla.delete(0, END)
    operacion = '-'


def suma():
    global num1 #Creamos variable global para poder usarla fuera de la funcion
    global operacion
    num1 = pantalla.get()
    num1 = float(num1)
    pantalla.delete(0, END) #Para borrar lo que hay en pantalla
    operacion = '+'

def multiplicar():
    global num1
    global operacion
    num1 = pantalla.get()
    num1 = float(num1)
    pantalla.delete(0, END)
    operacion = '*'

def dividir():
    global num1
    global operacion
    num1 = pantalla.get()
    num1 = float(num1)
    pantalla.delete(0, END)
    operacion = '/'

def despejar():
    pantalla.delete(0, END)


root.resizable(0, 0) #Para que no se pueda cambiar el tamaño de la ventana
#root.resizable(1, 0) #Para mover en X horizontalmente la ventana
#root.resizable(0, 1) #Para mover en Y verticalmente

root.geometry('292x304') #Para asignarle el tamaño directamente

#CALCULADORA parte logica

#CALCULADORA parte grafica
pantalla = Entry(root, width=22, bg="black", fg="lawn green", borderwidth=0, font=('ms serif', 18, 'bold'))#18 = tamaño, bold=Negrita

pantalla.grid(row=0, padx=2, pady=2, columnspan=4) #columnspan= para que ocupe 4 columnas

boton_1 = Button(root, text='1', width=9, height=3, bg='white', fg='black', borderwidth=0, cursor='hand2', command=lambda:enviarNumero(1)).grid(row=1, column=0, padx=1, pady=1)
#cursor = lo que hace el cursor cuando pasamos por encima de el elemento.
boton_2 = Button(root, text='2', width=9, height=3, bg='white', fg='black', borderwidth=0, cursor='hand2', command=lambda:enviarNumero(2)).grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text='3', width=9, height=3, bg='white', fg='black', borderwidth=0, cursor='hand2', command=lambda:enviarNumero(3)).grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text='4', width=9, height=3, bg='white', fg='black', borderwidth=0, cursor='hand2', command=lambda:enviarNumero(4)).grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text='5', width=9, height=3, bg='white', fg='black', borderwidth=0, cursor='hand2', command=lambda:enviarNumero(5)).grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text='6', width=9, height=3, bg='white', fg='black', borderwidth=0, cursor='hand2', command=lambda:enviarNumero(6)).grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text='7', width=9, height=3, bg='white', fg='black', borderwidth=0, cursor='hand2', command=lambda:enviarNumero(7)).grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text='8', width=9, height=3, bg='white', fg='black', borderwidth=0, cursor='hand2', command=lambda:enviarNumero(8)).grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text='9', width=9, height=3, bg='white', fg='black', borderwidth=0, cursor='hand2', command=lambda:enviarNumero(9)).grid(row=3, column=2, padx=1, pady=1)
boton_0 = Button(root, text='0', width=9, height=3, bg='white', fg='black', borderwidth=0, cursor='hand2', command=lambda:enviarNumero(0)).grid(row=4, column=1, padx=1, pady=1)

boton_igual = Button(root, text='=', width=9, height=3, bg='black', fg='lawn green', borderwidth=0, cursor='hand2', command=igual).grid(row=4, column=0, padx=1, pady=1)
boton_coma = Button(root, text=',', width=9, height=3, bg='black', fg='lawn green', borderwidth=0, cursor='hand2', command=lambda : enviarNumero(".")).grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text='+', width=9, height=3, bg='black', fg='lawn green', borderwidth=0, cursor='hand2', command=suma).grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text='-', width=9, height=3, bg='black', fg='lawn green', borderwidth=0, cursor='hand2', command=resta).grid(row=2, column=3, padx=1, pady=1)
boton_multiplicar = Button(root, text='x', width=9, height=3, bg='black', fg='lawn green', borderwidth=0, cursor='hand2', command=multiplicar).grid(row=3, column=3, padx=1, pady=1)
boton_dividir = Button(root, text='/', width=9, height=3, bg='black', fg='lawn green', borderwidth=0, cursor='hand2', command=dividir).grid(row=4, column=3, padx=1, pady=1)
boton_despejar = Button(root, text='>>>', width=40, height=3, bg='black', fg='lawn green', borderwidth=0, cursor='hand2', command=despejar).grid(row=5, column=0, columnspan=4, padx=1, pady=1)

root.mainloop()