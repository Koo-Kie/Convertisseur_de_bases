import tkinter as tk
import re

def init():        
    global base1, base2, nombre, result, window
    result = ''
    window = tk.Tk()
    width = 1000
    height = 600
    window.title('Convertisseur de bases - V1.0')
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
    command = conversion
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
        text=f"Résultat: {result}",
        height= 150,
        width = 950,
        justify= 'left',
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
    résultat.place(x= 40, y=400)
    bouton_convertir.place(x=420,y=190,width=115,height=51)
    window.mainloop()
    # while True: 
    #     inp = input('\nConversion base1 base2 (hex, dec, oct, bin): ').lower()
    #     try:
    #         bases = re.search('(bin|dec|hex|oct).*(bin|dec|hex|oct)', inp).groups()
    #         break
    #     except:
    #         print('Erreur, veuillez saisir dans le bon format (base1 base2)\n')
    #         continue
    # while True:
    #     try:
    #         signe = False
    #         num = input('\n(ctrl+c pour modifier les bases) Nombre à convertir: ')
    #         if bases[0] == 'dec':
    #             if num.isnumeric():
    #                 pass
    #             elif re.search('^-\d+$', num):
    #                 signe = True
    #                 pass
    #             else:
    #                 print('Erreur, veuillez saisir un decimal!\n')
    #                 continue
    #         elif bases[0] == 'bin':
    #             try:
    #                 int(num, 2)
    #             except:
    #                 print('Veuillez entrer un nombre bianire!\n')
    #                 continue
    #         elif bases[0] == 'hex':
    #             try:
    #                 int(num, 16)
    #                 pass
    #             except:
    #                 print('Veuillez entrer un nombre en hexadecimal!\n')
    #                 continue
    #         elif bases[0] == 'oct':
    #             try:
    #                 int(num, 8)
    #                 pass
    #             except:
    #                 print('Veuillez entrer un nombre en octal!\n')
    #                 continue
    #         print(conversion(bases[0], bases[1], num, signe))
    #     except KeyboardInterrupt:
    #         init() 

def conversion():
    b1 = base1.get()
    b2 = base2.get()
    num = nombre.get()
    if num[0] == '-':
        signe = True
    else: signe = False 
    if b2 == 'dec':
        if b1 == 'hex':
            result = (int(num, 16))
        elif b1 == 'oct':
            result = (int(num, 8))
        elif b1 == 'bin':
            if len(num) == 8 or len(num) == 16:
                résultat = ''
                for bit in (bin(int(str(num),2)-1)[2:]):
                    if bit == '0':
                        résultat += '1'
                    else:
                        résultat += '0'
                result = (f'Décimal: {int(num, 2)} \nComplément à deux: -{int(résultat, 2)}')
            else:
                result = (int(num, 2))
        else:
            result = (num)
    elif b2 == 'hex':
        if b1 == 'dec':
            return(hex(int(num))[2:])
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
                result = (f'Complément à deux (1 octet): {bin(int(num) & 0xff)[2:]} \nComplément à deux (2 octets): {bin(int(num) & 0xfff)[2:]}')
            else:
                result = (bin(int(num))[2:])
        elif b1 == 'oct':
            result = (bin(int(num, 8))[2:])
        elif b1 == 'hex':
            result = (bin(int(num, 16))[2:])
        else:
            result = (num)
    résultat = tk.Label(
        text=f"Résultat: {result}",
        height= 150,
        width= 950,
        fg= '#f55142',
        font = ('',15),
        justify= 'left' 
    )
    résultat.place(x= 40, y=400)    
if __name__ == '__main__':
    init()