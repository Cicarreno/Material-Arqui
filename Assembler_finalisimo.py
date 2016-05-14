__author__ = 'pedromangiola'

import tkinter as tk

master = tk.Tk()
master.title("Assembly")
label = tk.Label(master, fg="blue")
label.config(text="ingresa el nombre del archivo de input:")
label.pack()


e = tk.Entry(master)
e.pack()

def ensambla():

    global path
    path = e.get()

button = tk.Button(master, text='Ensamblar', command=ensambla)
button.pack()
master.mainloop()

archi = open(path,'r')
texto = archi.readlines()
nuevo_arreglo = []
for k in texto:
    if "//" in k:
        l = k[:k.index("//")]
        l = l[:-1]
        nuevo_arreglo.append(l)
    elif "//" not in k and k != "\n":
        nuevo_arreglo.append(k)
#nuevo_arreglo = []
# for k in arreglo:
#     if "\t" in k:
#         l = k[:-1]
#         nuevo_arreglo.append(l)
#     else:
#         nuevo_arreglo.append(k)
data = []
code = []
d = False


if nuevo_arreglo[-1] == ' ':
    nuevo_arreglo = nuevo_arreglo[:-1]

for k in nuevo_arreglo:


    if not(any(c.isalpha() for c in k)) or len(k) < 3:


        nuevo_arreglo.remove(k)


    # if k == '':
    #     print(k,'k')
    #     print('nuevo_array',nuevo_arreglo)
    #     nuevo_arreglo.remove(k)     DEBERIA IR DEBERIA IR

for i in nuevo_arreglo:
    i = i.lower()
    i = i.replace('\n',"")
    i = i.replace('\t', "")
    while i[0] == " ":
        i = i[1:]
    while i[-1] == " ":
        i = i[:-1]

    if d == 1 and ("data:" and 'code:') not in i:

        data.append(i)

    if d == 2 and ("data:" and "code:") not in i: code.append(i)

    if "data:" in i:
        d = 1

    elif "code:" in i:
        d = 2


def num_to_bin(num_input): #Pasa numero de cualquier formato a binario

    num_input = str(num_input)
    fin = num_input[-1]
    if fin == 'd':
        num_input = num_input[:-1]
        output = "{0:b}".format(int(num_input)).zfill(16)
    elif fin == 'b':
        output = num_input[:-1].zfill(16)
    elif fin.isdigit():
        output = "{0:b}".format(int(num_input)).zfill(16)
    elif fin == 'h':
        num_input = num_input[:-1]
        output = bin(int(num_input, 16))[2:].zfill(16)


    return output



lista_int = []
lista_opcodes = []
for i in range(0,68):
    lista_int.append(i)
for k in lista_int:
    p = "{0:b}".format(k)
    h = p.zfill(17)
    lista_opcodes.append(h)

direcciones_memoria = {}
count = 0

for i in data:
    aux = []
    i = i.split(" ")
    for j in i:
        if j != "":
            aux.append(j)


    direcciones_memoria[aux[0]] = ["{0:b}".format(count).zfill(16), num_to_bin(aux[1])]
    count+= 1
    #direcciones_memoria -> key es nombre de variable, values es lista, lista[0] = address, lista[1] = valor





def instruccion_arreglada(lista):

    if len(lista) == 3:
        for k in lista:
            if k.isdigit() and lista.index(k) == 2 or k[0].isdigit():
                return (lista[0] + " " + lista[1] + ",lit")
            elif "(" in k and lista.index(k)==1:
                return (lista[0] + " (dir)," + lista[2])
            elif "(" in k and lista.index(k)==2:
                return (lista[0] + " " + lista[1] + ",(dir)")

    elif len(lista) == 2:
        if "(" not in lista[1]:
            return (lista[0] + " ins")
        elif "(" in lista[1]:
            return (lista[0] + " (dir)")

def deteccion(instruccion):
    #print(instruccion)
    lista_final = []
    list = []
    aux = instruccion.split()
    aux1 = aux[0]+" "
    i=1
    while i < int(len(aux)):
        aux1 += aux[i]
        i+=1
    aux2 = aux1.split()
    for k in aux2:
        if k == ',':
            aux2.remove(k)
    for k in aux2:
        k = k.split(",")
        list += k
    for k in list:
        if k == '':
            list.remove(k)

    operacion = instruccion_arreglada(list)
    #print(operacion)
    lista_final.append(operacion)
    if instruccion[-1:] == ":":
        return ["LABEL"]
    else: return lista_final

def generacion_diccionario():
    diccionario = {}
    for i in range(len(lista_opcodes)):
        diccionario[lista_opcodes[i]] = ""
        if lista_opcodes[i] == "00000000000000000":
            diccionario[lista_opcodes[i]] = "nop"
        elif lista_opcodes[i] == "00000000000000001":
            diccionario[lista_opcodes[i]] = "mov a,b"
        elif lista_opcodes[i] == "00000000000000010":
            diccionario[lista_opcodes[i]] = "mov b,a"
        elif lista_opcodes[i] == "00000000000000011":
            diccionario[lista_opcodes[i]] = "mov a,lit"
        elif lista_opcodes[i] == "00000000000000100":
            diccionario[lista_opcodes[i]] = "mov b,lit"
        elif lista_opcodes[i] == "00000000000000101":
            diccionario[lista_opcodes[i]] = "mov a,(dir)"
        elif lista_opcodes[i] == "00000000000000110":
            diccionario[lista_opcodes[i]] = "mov b,(dir)"
        elif lista_opcodes[i] == "00000000000000111":
            diccionario[lista_opcodes[i]] = "mov (dir),a"
        elif lista_opcodes[i] == "00000000000001000":
            diccionario[lista_opcodes[i]] = "mov (dir),b"

        elif lista_opcodes[i] == "00000000000001001":
            diccionario[lista_opcodes[i]] = "add a,b"
        elif lista_opcodes[i] == "00000000000001010":
            diccionario[lista_opcodes[i]] = "add b,a"
        elif lista_opcodes[i] == "00000000000001011":
            diccionario[lista_opcodes[i]] = "add a,lit"
        elif lista_opcodes[i] == "00000000000001100":
            diccionario[lista_opcodes[i]] = "add b,lit"
        elif lista_opcodes[i] == "00000000000001101":
            diccionario[lista_opcodes[i]] = "add a,(dir)"
        elif lista_opcodes[i] == "00000000000001110":
            diccionario[lista_opcodes[i]] = "add b,(dir)"
        elif lista_opcodes[i] == "00000000000001111":
            diccionario[lista_opcodes[i]] = "add (dir)"

        elif lista_opcodes[i] == "00000000000010000":
            diccionario[lista_opcodes[i]] = "sub a,b"
        elif lista_opcodes[i] == "00000000000010001":
            diccionario[lista_opcodes[i]] = "sub b,a"
        elif lista_opcodes[i] == "00000000000010010":
            diccionario[lista_opcodes[i]] = "sub a,lit"
        elif lista_opcodes[i] == "00000000000010011":
            diccionario[lista_opcodes[i]] = "sub b,lit"
        elif lista_opcodes[i] == "00000000000010100":
            diccionario[lista_opcodes[i]] = "sub a,(dir)"
        elif lista_opcodes[i] == "00000000000010101":
            diccionario[lista_opcodes[i]] = "sub b,(dir)"
        elif lista_opcodes[i] == "00000000000010110":
            diccionario[lista_opcodes[i]] = "sub (dir)"

        elif lista_opcodes[i] == "00000000000010111":
            diccionario[lista_opcodes[i]] = "and a,b"
        elif lista_opcodes[i] == "00000000000011000":
            diccionario[lista_opcodes[i]] = "and b,a"
        elif lista_opcodes[i] == "00000000000011001":
            diccionario[lista_opcodes[i]] = "and a,lit"
        elif lista_opcodes[i] == "00000000000011010":
            diccionario[lista_opcodes[i]] = "and b,lit"
        elif lista_opcodes[i] == "00000000000011011":
            diccionario[lista_opcodes[i]] = "and a,(dir)"
        elif lista_opcodes[i] == "00000000000011100":
            diccionario[lista_opcodes[i]] = "and b,(dir)"
        elif lista_opcodes[i] == "00000000000011101":
            diccionario[lista_opcodes[i]] = "and (dir)"

        elif lista_opcodes[i] == "00000000000011110":
            diccionario[lista_opcodes[i]] = "or a,b"
        elif lista_opcodes[i] == "00000000000011111":
            diccionario[lista_opcodes[i]] = "or b,a"
        elif lista_opcodes[i] == "00000000000100000":
            diccionario[lista_opcodes[i]] = "or a,lit"
        elif lista_opcodes[i] == "00000000000100001":
            diccionario[lista_opcodes[i]] = "or b,lit"
        elif lista_opcodes[i] == "00000000000100010":
            diccionario[lista_opcodes[i]] = "or a,(dir)"
        elif lista_opcodes[i] == "00000000000100011":
            diccionario[lista_opcodes[i]] = "or b,(dir)"
        elif lista_opcodes[i] == "00000000000100100":
            diccionario[lista_opcodes[i]] = "or (dir)"

        elif lista_opcodes[i] == "00000000000100101":
            diccionario[lista_opcodes[i]] = "xor a,b"
        elif lista_opcodes[i] == "00000000000100110":
            diccionario[lista_opcodes[i]] = "xor b,a"
        elif lista_opcodes[i] == "00000000000100111":
            diccionario[lista_opcodes[i]] = "xor a,lit"
        elif lista_opcodes[i] == "00000000000101000":
            diccionario[lista_opcodes[i]] = "xor b,lit"
        elif lista_opcodes[i] == "00000000000101001":
            diccionario[lista_opcodes[i]] = "xor a,(dir)"
        elif lista_opcodes[i] == "00000000000101010":
            diccionario[lista_opcodes[i]] = "xor b,(dir)"
        elif lista_opcodes[i] == "00000000000101011":
            diccionario[lista_opcodes[i]] = "xor (dir)"

        elif lista_opcodes[i] == "00000000000101100":
            diccionario[lista_opcodes[i]] = "not a"
        elif lista_opcodes[i] == "00000000000101101":
            diccionario[lista_opcodes[i]] = "not b,a"
        elif lista_opcodes[i] == "00000000000101110":
            diccionario[lista_opcodes[i]] = "not (dir),a"

        elif lista_opcodes[i] == "00000000000101111":
            diccionario[lista_opcodes[i]] = "shl a"
        elif lista_opcodes[i] == "00000000000110000":
            diccionario[lista_opcodes[i]] = "shl b,a"
        elif lista_opcodes[i] == "00000000000110001":
            diccionario[lista_opcodes[i]] = "shl (dir),a"

        elif lista_opcodes[i] == "00000000000110010":
            diccionario[lista_opcodes[i]] = "shr a"
        elif lista_opcodes[i] == "00000000000110011":
            diccionario[lista_opcodes[i]] = "shr b,a"
        elif lista_opcodes[i] == "00000000000110100":
            diccionario[lista_opcodes[i]] = "shr (dir),a"

        elif lista_opcodes[i] == "00000000000110101":
            diccionario[lista_opcodes[i]] = "inc a"
        elif lista_opcodes[i] == "00000000000110110":
            diccionario[lista_opcodes[i]] = "inc b"
        elif lista_opcodes[i] == "00000000000110111":
            diccionario[lista_opcodes[i]] = "inc (dir)"

        elif lista_opcodes[i] == "00000000000111000":
            diccionario[lista_opcodes[i]] = "dec a"

        elif lista_opcodes[i] == "00000000000111001":
            diccionario[lista_opcodes[i]] = "cmp a,b"
        elif lista_opcodes[i] == "00000000000111010":
            diccionario[lista_opcodes[i]] = "cmp a,lit"
        elif lista_opcodes[i] == "00000000000111011":
            diccionario[lista_opcodes[i]] = "cmp a,(dir)"

        elif lista_opcodes[i] == "00000000000111100":
            diccionario[lista_opcodes[i]] = "jmp ins"
        elif lista_opcodes[i] == "00000000000111101":
            diccionario[lista_opcodes[i]] = "jeq ins"
        elif lista_opcodes[i] == "00000000000111110":
            diccionario[lista_opcodes[i]] = "jne ins"
        elif lista_opcodes[i] == "00000000000111111":
            diccionario[lista_opcodes[i]] = "jgt ins"
        elif lista_opcodes[i] == "00000000001000000":
            diccionario[lista_opcodes[i]] = "jge ins"
        elif lista_opcodes[i] == "00000000001000001":
            diccionario[lista_opcodes[i]] = "jlt ins"
        elif lista_opcodes[i] == "00000000001000010":
            diccionario[lista_opcodes[i]] = "jle ins"
        elif lista_opcodes[i] == "00000000001000011":
            diccionario[lista_opcodes[i]] = "jcr ins"
    return diccionario



def funcion_transformadora(archivo, diccionario, lista_instrucciones, lista_lit):
    contador = 0
    for k in lista_instrucciones:


        if k in diccionario.values():
            key = [key for key, value in diccionario.items() if value == k][0]
            if key == "00000000000110101": #INC A
                archivo.write('"' + "0000000000000001" + "00000000000001011" + '"' + ',' + "\n")
            elif key == "00000000000111000": #DEC A

                archivo.write('"' + "0000000000000001" + "00000000000010010" + '"' + ',' + "\n")

            else:
                archivo.write('"' + lista_lit[contador] + key +'"' +','+ "\n")
        elif k == "LABEL":
            archivo.write('"' + lista_lit[contador] + "00000000000000001" + '"' +','+"\n")
        else:
            r = deteccion(k)

            for l in r:
                if l in diccionario.values():
                    key = [key for key, value in diccionario.items() if value == l][0]
                    if key == "00000000000110101": #INC A
                        archivo.write('"' + "0000000000000001" + "00000000000001011" + '"' + ',' + "\n")
                    elif key == "00000000000111000": #DEC A
                        archivo.write('"' + "0000000000000001" + "00000000000010010" + '"' + ',' + "\n")
                    else:
                       
                        archivo.write('"' + lista_lit[contador] + key +'"' +','+ "\n")


                elif l == "LABEL":
                    archivo.write('"' + lista_lit[contador] + "00000000000000001" + '"' +',' +"\n")
        contador +=1


diccionario = generacion_diccionario()
lista_lit = []


def crea_dict_labels(code):
    dict_labels = {}

    for j in code:


        aux = j.replace('(',"-")
        aux = aux.replace(')',"")
        aux = aux.replace(","," ")
        aux = aux.split(' ')
        if aux[0][-1] == ':':


            dict_labels[aux[0]] = code.index(j)


    return dict_labels
dict_labels = crea_dict_labels(code)

def crea_lista_literales(code, dict_labels, direcciones_memoria):
    
    for i in code:

        aux = i.replace('(',"-")
        aux = aux.replace(')',"")
        aux = aux.replace(","," ")
        aux = aux.split(' ')

        



        if len(aux) == 3 and aux[1][0] == '-': #CASO DIR MEMORIA

            if aux[1][1:] in direcciones_memoria:
                lista_lit.append(direcciones_memoria[aux[1][1:]][0])
            else:
                lista_lit.append(num_to_bin(aux[1][1:]))




        elif len(aux) == 3 and aux[2][0] == '-': #CASO DIR MEMORIA
            if aux[2][1:] in direcciones_memoria:
                lista_lit.append(direcciones_memoria[aux[2][1:]][0])
            else:
                lista_lit.append(num_to_bin(aux[2][1:]))



        elif len(aux) == 3 and aux[1].isdigit():
            lista_lit.append(num_to_bin(aux[1]))
        elif len(aux) == 3 and aux[2].isdigit():
            lista_lit.append(num_to_bin(aux[2]))
        elif len(aux) == 2: #FALTA DIVIDIR EL CASO DE INC Y DEC

            if aux[1] + ':' in dict_labels:

                numero = dict_labels[aux[1] + ':'] +1
                
                lista_lit.append(num_to_bin(str(numero)))
            else:
                lista_lit.append('0000000000000000')


        else:

            lista_lit.append('0000000000000000')
    return lista_lit



lista_lit = crea_lista_literales(code, dict_labels, direcciones_memoria)



def generador_literales(code):
    for i in code:
        pass

    pass



def creador_output(variables_iniciales,code,lista_lit, diccionario):
    output = open('Output.txt','w')

    texto_base = """library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;
USE IEEE.NUMERIC_STD.ALL;
entity ROM is
    Port (
      address : in  std_logic_vector(11 downto 0);
      dataout : out std_logic_vector(32 downto 0)
);
end ROM;

architecture Behavioral of ROM is

type memory_array is array (0 to ((2 ** 12) - 1) ) of std_logic_vector (32 downto 0);

signal memory : memory_array:= (""" + '\n'+'\n'
    output.write(texto_base)
    for variable in variables_iniciales.values():
        mova_alit = "00000000000000011"
        mov_dira =  "00000000000000111"

        output.write('"' + variable[1] + mova_alit + '"' + ',\n')
        output.write('"' + variable[0] + mov_dira + '"' + ',\n')

    funcion_transformadora(output, diccionario, code, lista_lit)


    for i in range(4095 - (len(code) + len(variables_iniciales)*2)):
        output.write('"000000000000000000000000000000000"' + ',' + '\n')
    texto_final = """"000000000000000000000000000000000"
); begin

    dataout <= memory(to_integer(unsigned(address)));

end Behavioral;   """
    output.write(texto_final)
    output.close()

    return

creador_output(direcciones_memoria,code, lista_lit, diccionario)