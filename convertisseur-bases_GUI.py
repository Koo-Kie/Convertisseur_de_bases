def init():
    import re
    import tkinter as tk

    window = tk.Tk()
    window.geometry('1000x1000')
    window.title('Convertisseur de bases - V1.0')

    titre = tk.Label(
        text="Convertisseur de bases (décimal, binaire, octale et héxadécimal)",
        height= 3,
        fg = '#f55142',
        width= 100,
        font = ('',20) 
    )
    bouton_convertir = tk.Button(
    text="Convertir",
    width=10,
    height=2,
    bg="#f55142",
    fg="white",
    font  = ('', 15),
    border = 0
    )
    base1_titre = tk.Label(
        text="Base 1",
        fg = '#f55142',
        height= 3,
        width= 100,
        font = ('',15) 
    )
    base1 = tk.Entry(
    fg="#f55142",
    bg="white",
    width=50
    )
    base2_titre = tk.Label(
        text="Base 2",
        height= 3,
        fg= '#f55142',
        width= 100,
        font = ('',15) 
    )
    base2 = tk.Entry(
    fg="#f55142",
    bg="white",
    width=50
    )
  
    titre.pack()
    base1_titre.pack()
    base1.pack()
    base2_titre.pack()
    base2.pack()
    bouton_convertir.place(x = 450,y = 900)
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

def conversion(b1, b2, num, signe): 
    if b2 == 'dec':
        if b1 == 'hex':
            return (int(num, 16))
        elif b1 == 'oct':
            return (int(num, 8))
        elif b1 == 'bin':
            if len(num) == 8 or 16:
                résultat = ''
                for bit in (bin(int(str(num),2)-1)[2:]):
                    if bit == '0':
                        résultat += '1'
                    else:
                        résultat += '0'
                return f'Décimal: {int(num, 2)} \nComplément à deux: -{int(résultat, 2)}'
            else:
                return (int(num, 2))
        else:
            return (num)
    elif b2 == 'hex':
        if b1 == 'dec':
            return(hex(int(num))[2:])
        elif b1 == 'oct':
            return (hex(int(num, 8))[2:])
        elif b1 == 'bin':
            return (hex(int(num, 2))[2:])
        else:
            return (num)
    elif b2 == 'oct':
        if b1 == 'dec':
            return (oct(int(num))[2:])
        elif b1 == 'hex':
            return (oct(int(num, 16))[2:])
        elif b1 == 'bin':
            return (oct(int(num, 2))[2:])
        else:
            return (num)
    elif b2 == 'bin':
        if b1 == 'dec':
            if signe == True:
                return f'Complément à deux (1 octet): {bin(int(num) & 0xff)[2:]} \nComplément à deux (2 octets): {bin(int(num) & 0xfff)[2:]}'
            else:
                return (bin(int(num))[2:])
        elif b1 == 'oct':
            return (bin(int(num, 8))[2:])
        elif b1 == 'hex':
            return (bin(int(num, 16))[2:])
        else:
            return (num)    
if __name__ == '__main__':
    init()