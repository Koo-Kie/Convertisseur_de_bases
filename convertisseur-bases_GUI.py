import tkinter as tk
import re

def init():        
    global base1, base2, nombre, result, window
    result = ''
    window = tk.Tk()
    width = 1000
    height = 600
    window.title('Convertisseur de bases - V1.0 by Kais')
    screenwidth = window.winfo_screenwidth()
    screenheight = window.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    window.geometry(alignstr)
    window.resizable(width=False, height=False)

    titre = tk.Label(
        text="Convertisseur de bases (décimal, binaire, octale et héxadécimal)",
        fg = '#f55142',
        justify= 'center',
        font = ('',20) 
    )
    base1_titre = tk.Label(
        text="Base 1",
        fg = '#f55142',
        justify = 'center', 
        font = ('',15) 
    )
    base1 = tk.Entry(
    fg="#f55142",
    bg="white",
    font= ('', 13),
    justify = 'center',
    borderwidth = '1px',
    )
    base2_titre = tk.Label(
        text="Base 2",
        fg= '#f55142',
        justify= 'center',
        font = ('',15) 
    )
    base2 = tk.Entry(
    fg="#f55142",
    bg="white",
    font= ('', 13),
    justify= 'center',
    borderwidth = '1px',
    )
    bouton_convertir = tk.Button(
    text="Convertir",
    width=10,
    borderwidth = '3px',
    justify= 'center',
    height=2,
    bg="#f55142",
    fg="white",
    font  = ('', 15),
    command = verif
    )
    nombre_titre = tk.Label(
        text="Nombre:",
        fg= '#f55142',
        font = ('',15) 
    )
    nombre = tk.Entry(
    fg="#f55142",
    bg="white",
    font= ('', 13),
    justify= 'center'
    )
    résultat = tk.Label(
        text=f"Résultat: \n{result}",
        height= 10,
        width = 200,
        justify= 'center',
        fg= '#f55142',
        font = ('',15) 
    )  
    
    titre.place(x=100,y=30,width=800,height=50)
    base1_titre.place(x=140,y=120,width=197,height=40)
    base1.place(x=160,y=190,width=155,height=50)
    base2_titre.place(x=630,y=120,width=159,height=41)
    base2.place(x=640,y=190,width=155,height=50)
    nombre_titre.place(x=440,y=280,width=80,height=25)
    nombre.place(x=420,y=320,width=109,height=44)
    résultat.place(x= -700, y=380)
    bouton_convertir.place(x=420,y=190,width=115,height=51)
    window.mainloop()

def verif():
    b1 = base1.get().strip()
    b2 = base2.get().strip()
    num = nombre.get().strip()
    signe = False
    if re.search('.*(bin|dec|hex|oct).*', b1) and re.search('.*(bin|dec|hex|oct).*', b2):
        pass
    else: result = 'Erreur, veuillez saisir dans le bon format (base1 base2)'

    if b1 == 'dec':
        if num.isnumeric():
            conversion(b1, b2, num, signe)
        elif re.search('^-\d+$', num):
            signe = True
            conversion(b1, b2, num, signe)
        else:
            result = 'Erreur, veuillez saisir un decimal!'
    elif b1 == 'bin':
        try:
            int(num, 2)
            conversion(b1, b2, num, signe)
        except:
            result = 'Veuillez entrer un nombre binaire!'
    elif b1 == 'hex':
        try:
            int(num, 16)
            conversion(b1, b2, num, signe)
        except:
            result = 'Veuillez entrer un nombre en hexadecimal!'
    elif b1 == 'oct':
        try:
            int(num, 8)
            conversion(b1, b2, num, signe)
        except:
            result = 'Veuillez entrer un nombre en octal!'
    else: result = 'Veuillez entrer une base valide!'
    try:
        résultat = tk.Label(
            text=f"Résultat: \n{result}",
            height= 10,
            width= 200,
            fg= '#f55142',
            font = ('',15),
            justify= 'center' 
        )
        résultat.place(x= -700, y=380)
    except:
        pass

def conversion(b1, b2, num, signe):
    if b2 == 'dec':
        if b1 == 'hex':
            result = (int(num, 16))
        elif b1 == 'oct':
            result = (int(num, 8))
        elif b1 == 'bin':
            if len(num)%8 == 0:
                résultat = ''
                for bit in (bin(int(str(num),2)-1)[2:]):
                    if bit == '0':
                        résultat += '1'
                    else:
                        résultat += '0'
                result = f'Décimal: {int(num, 2)} \nComplément à deux: -{int(résultat, 2)}'
            else:
                result = (int(num, 2))
        else:
            result = (num)
    elif b2 == 'hex':
        if b1 == 'dec':
            result =(hex(int(num))[2:])
        elif b1 == 'oct':
            result = (hex(int(num, 8))[2:])
        elif b1 == 'bin':
            result = (hex(int(num, 2))[2:])
        else:
            result = (num)
    elif b2 == 'oct':
        if b1 == 'dec':
            result = (oct(int(num))[2:])
        elif b1 == 'hex':
            result = (oct(int(num, 16))[2:])
        elif b1 == 'bin':
            result = (oct(int(num, 2))[2:])
        else:
            result = (num)
    elif b2 == 'bin':
        if b1 == 'dec':
            if signe == True:
                nb_byte = (int(num).bit_length() + 7) // 8
                if nb_byte >=2:
                    lettre = 's'
                else: lettre = ''
                result = f'Complément à deux ({nb_byte} octet{lettre}): {bin(int(num) & (2**(nb_byte*8) - 1))[2:]}'   
            else:
                result = (bin(int(num))[2:])
        elif b1 == 'oct':
            result = (bin(int(num, 8))[2:])
        elif b1 == 'hex':
            result = (bin(int(num, 16))[2:])
        else:
            result = (num)
    else: result = 'Veuillez entrer une base valide!'
    résultat = tk.Label(
        text=f"Résultat: \n{result}",
        height= 10,
        width= 200,
        fg= '#f55142',
        font = ('',15),
        justify= 'center' 
    )
    résultat.place(x= -700, y=380)    
if __name__ == '__main__':
    init()