__author__ = 'cristian_cn'
from collections import defaultdict

import tkinter as tk

# master = tk.Tk()
# master.title("Assembly")
# label = tk.Label(master, fg="blue")
# label.config(text="ingresa el nombre del archivo de input:")
# label.pack()
#
#
# e = tk.Entry(master)
# e.pack()
#
# def ensambla():
#
#     global path
#     path = e.get()
#
# button = tk.Button(master, text='Ensamblar', command=ensambla)
# button.pack()
# master.mainloop()

archi = open('alg6.txt','r')
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
##nt(nuevo_arreglo,'santapapa')
#for k in nuevo_arreglo:


    #if not(any(c.isalpha() for c in k)) or len(k) < 3:

#
    #    nuevo_arreglo.remove(k)


    # if k == '':
    #     print(k,'k')
    #     print('nuevo_array',nuevo_arreglo)
    #     nuevo_arreglo.remove(k)     DEBERIA IR DEBERIA IR


for i in nuevo_arreglo:

    i = i.lower()
    i = i.replace('\n',"")
    i = i.replace('\t', "")


    if i.isspace() or i == "":
        pass
    else:


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

code.insert(0,'str sp')
# print(code)
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
for i in range(0,100):    #eso es cambio era hasta 99
    lista_int.append(i)

for k in lista_int:
    p = "{0:b}".format(k)
    h = p.zfill(17)

    lista_opcodes.append(h)


direcciones_memoria = defaultdict(list)
count = 0
#print(data)
nombre = None

for i in data:
    aux = []
    i = i.split(" ")

    #print(i,'hola pepit')
    for j in i:
        if j != "":
            aux.append(j)
   # print(aux,'este es aux ')
    if len(aux) > 1:
        nombre = aux[0]

        if aux[1][0] == "'":
            aux[1] = aux[1].replace("'","")
            aux[1] = ord(aux[1])
            print('JAJAJAJAJAJAAJAJAJ')
            print(aux[1])

        if aux[1][0] != '"':

            direcciones_memoria[nombre].append(("{0:b}".format(count).zfill(16), num_to_bin(aux[1])))

        elif aux[1][0] == '"':
            aux[1] = aux[1].replace('"',"")

            for i in aux[1]:
                direcciones_memoria[nombre].append(("{0:b}".format(count).zfill(16), num_to_bin(ord(i))))
            direcciones_memoria[nombre].append(("{0:b}".format(count).zfill(16), num_to_bin(0)))



    else:
        direcciones_memoria[nombre].append(("{0:b}".format(count).zfill(16), num_to_bin(aux[0])))




    count+= 1
#print(direcciones_memoria)
    #direcciones_memoria -> key es nombre de variable, values es lista, lista[0] = address, lista[1] = valor


for i in direcciones_memoria:
    print(i,direcciones_memoria[i],'direccion')
def instruccion_arreglada(lista): # manejar todo lo que tenga lit


    if len(lista) == 3:

        for k in lista:
            if k.isdigit() and lista.index(k) == 2 or k[0].isdigit():
                return (lista[0] + " " + lista[1] + ",lit")
            elif "(" in k and lista.index(k)==1:


                if lista[1][1].isdigit():
                    return lista[0]+ " "+ "(dir)," + lista[2]

                elif lista[0] == 'in' or (lista[0] == 'mov' and (lista[1][1] == 'a' or lista[1][1] == 'b') ):



                    return lista[0]+ " "+ lista[1] + ",lit"

                return (lista[0] + " (dir)," + lista[2])
            elif "(" in k and lista.index(k)==2:

                return (lista[0] + " " + lista[1] + ",(dir)")

    elif len(lista) == 2:
        if "(" not in lista[1]:
            if lista[1][0].isdigit():
                return (lista[0] + " dir")
            elif lista[0] == 'call':
                return (lista[0] + " dir")

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
    lista_sin_corregir = [['mov','a','(b)'],['mov','b','(b)'],['mov','(b)','a'],['add','a','(b)'],
                          ['add','b','(b)'],['sub','a','(b)'], ['sub','b','(b)'], ['and','a','(b)'],
                          ['and','b','(b)'], ['or','a','(b)'], ['or','b','(b)'], ['xor','a','(b)'],
                          ['xor','b','(b)'] ,['not','(b)','a'], ['shl','(b)','a'], ['and','a','(b)'],
                          ['shr','(b)','a'], ['inc','(b)'],  ['cmp','a','(b)']]

    if list in lista_sin_corregir:
        if len(list) == 3:
            operacion = list[0] + ' ' + list[1] + ',' + list[2]
        elif len(list) == 2:
            operacion = list[0] + ' ' + list[1]
    else:
        operacion = instruccion_arreglada(list)

    lista_final.append(operacion)

    if instruccion[-1:] == ":":

        return ["LABEL"]
    else: return lista_final

def generacion_diccionario():
    diccionario = {}
    for i in range(len(lista_opcodes)):
        #diccionario[lista_opcodes[i]] = ""
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
        #de aqui las nuevas
        elif lista_opcodes[i] == "00000000001000100":
            diccionario[lista_opcodes[i]] = "mov a,(b)"
        elif lista_opcodes[i] == "00000000001000101":
            diccionario[lista_opcodes[i]] = "mov b,(b)"
        elif lista_opcodes[i] == "00000000001000110":
            diccionario[lista_opcodes[i]] = "mov (b),a"
        elif lista_opcodes[i] == "00000000001000111":
            diccionario[lista_opcodes[i]] = "mov (b),lit" #do

        elif lista_opcodes[i] == "00000000001001000":
            diccionario[lista_opcodes[i]] = "add a,(b)"
        elif lista_opcodes[i] == "00000000001001001":
            diccionario[lista_opcodes[i]] = "add b,(b)"





        elif lista_opcodes[i] =="00000000001001010":
            diccionario[lista_opcodes[i]] = "sub a,(b)"
        elif lista_opcodes[i] =="00000000001001011":
            diccionario[lista_opcodes[i]] = "sub b,(b)"
        elif lista_opcodes[i] =="00000000001001100":
            diccionario[lista_opcodes[i]] = "and a,(b)"
        elif lista_opcodes[i] =="00000000001001101":
            diccionario[lista_opcodes[i]] = "and b,(b)"
        elif lista_opcodes[i] =="00000000001001110":
            diccionario[lista_opcodes[i]] = "or a,(b)"
        elif lista_opcodes[i] =="00000000001001111":
            diccionario[lista_opcodes[i]] = "or b,(b)"
        elif lista_opcodes[i] =="00000000001010000":
            diccionario[lista_opcodes[i]] = "xor a,(b)"
        elif lista_opcodes[i] =="00000000001010001":
            diccionario[lista_opcodes[i]] = "xor b,(b)"
        elif lista_opcodes[i] =="00000000001010010":
            diccionario[lista_opcodes[i]] = "not (b),a"
        elif lista_opcodes[i] =="00000000001010011":
            diccionario[lista_opcodes[i]] = "shl (b),a"
        elif lista_opcodes[i] =="00000000001010100":

            diccionario[lista_opcodes[i]] = "shr (b),a"
        elif lista_opcodes[i] =="00000000001010101":
            diccionario[lista_opcodes[i]] = "inc (b)"
        elif lista_opcodes[i] =="00000000001010110":
            diccionario[lista_opcodes[i]] = "cmp a,(b)"
        elif lista_opcodes[i] =="00000000001010111":
            diccionario[lista_opcodes[i]] = "push a"
        elif lista_opcodes[i] =="00000000001011000":
            diccionario[lista_opcodes[i]] = "push b"
        elif lista_opcodes[i] =="00000000001011001":
            diccionario[lista_opcodes[i]] = "pop a"
        elif lista_opcodes[i] =="00000000001011011":
            diccionario[lista_opcodes[i]] = "pop b"
        elif lista_opcodes[i] =="00000000001011101":
            diccionario[lista_opcodes[i]] = "call dir"
        elif lista_opcodes[i] =="00000000001011110":
            diccionario[lista_opcodes[i]] = "ret"
        elif lista_opcodes[i] =="00000000001100000":
            diccionario[lista_opcodes[i]] = "in a,lit"
        elif lista_opcodes[i] =="00000000001100001":
            diccionario[lista_opcodes[i]] = "in b,lit"
        elif lista_opcodes[i] =="00000000001100010":
            diccionario[lista_opcodes[i]] = "in (b),lit"

        elif lista_opcodes[i] == "00000000001100011":
            diccionario[lista_opcodes[i]] = "str sp"

        




    return diccionario



def funcion_transformadora(archivo, diccionario, lista_instrucciones, lista_lit):
    contador = 0


    global cont_dirs
    global cont_dos_ciclos
    cont_dos_ciclos = 0
    cont_dirs = 0

    for k in lista_instrucciones:
        #print(k,'esta es la lista asi nomas')
        # debug print(k,'instruccion recibida')



        if k in diccionario.values():


            key = [key for key, value in diccionario.items() if value == k][0]
            #print(k,'esta es inmediata', key)

            if key == "00000000000110101": #INC A
                archivo.write('"' + "0000000000000001" + "00000000000001011" + '"' + ',' + "\n")
                print(k,'CORRESPONDE 1')
            elif key == "00000000000111000": #DEC A
                print(k,'CORRESPONDE 1')

                archivo.write('"' + "0000000000000001" + "00000000000010010" + '"' + ',' + "\n")

            elif key == "00000000001011001": # POP A
                print(k,'CORRESPONDE 1')
                archivo.write('"' + lista_lit[contador] + "00000000001011001" + '"' +','+"\n")
                archivo.write('"' + "0000000000000000" + "00000000001011010" + '"' +','+"\n")
                cont_dos_ciclos +=1
            elif key == "00000000001011011": # POP B
                print(k,'CORRESPONDE 1')
                archivo.write('"' + lista_lit[contador] + "00000000001011011" + '"' +','+"\n")
                archivo.write('"' + "0000000000000000" + "00000000001011100" + '"' +','+"\n")
                cont_dos_ciclos +=1
            elif key == "00000000001011110": # RET
                print(k,'CORRESPONDE 1')
                archivo.write('"' + lista_lit[contador] + "00000000001011110" + '"' +','+"\n")
                archivo.write('"' + "0000000000000000" + "00000000001011111" + '"' +','+"\n")
                cont_dos_ciclos +=1








            elif key == "00000000000110111": #INC DIR

                archivo.write('"' + "0000000011111111" + "00000000000000111" + '"' + ',' + "\n") #mov dir1,a
                archivo.write('"' + "0000000000000001" + "00000000000000011" + '"' + ',' + "\n") #mov a,1
                archivo.write('"' + lista_lit[contador] + "00000000000001101" + '"' + ',' + "\n") # add A, dir2 la q crspone
                archivo.write('"' + lista_lit[contador] + "00000000000000111" + '"' + ',' + "\n") #mov dir2, a
                archivo.write('"' + "0000000011111111" + "00000000000000101" + '"' + ',' + "\n") #mov a, dir1

                cont_dirs +=1
                # debug print(k,'CORRESPONDE 1')


            else:
                archivo.write('"' + lista_lit[contador] + key +'"' +','+ "\n")
                print(k,'CORRESPONDE 1')

        elif k == "LABEL":
            print(k,'CORRESPONDE 1')


            archivo.write('"' + lista_lit[contador] + "00000000000000000" + '"' +','+"\n")
        else:
            r = deteccion(k)

            for l in r:


                if l in diccionario.values():
                    key = [key for key, value in diccionario.items() if value == l][0]
                    #print(l,'esta se busca',key)


                    if key == "00000000000110101": #INC A
                        archivo.write('"' + "0000000000000001" + "00000000000001011" + '"' + ',' + "\n")
                        print(l,'CORRESPONDE 2')
                    elif key == "00000000000111000": #DEC A
                        archivo.write('"' + "0000000000000001" + "00000000000010010" + '"' + ',' + "\n")
                        print(l,'CORRESPONDE 2')

                    elif key == "00000000000110111": #INC DIR
                        print(l,'CORRESPONDE 2')


                        archivo.write('"' + "0000000011111111" + "00000000000000111" + '"' + ',' + "\n") #mov dir1,a
                        archivo.write('"' + "0000000000000001" + "00000000000000011" + '"' + ',' + "\n") #mov a,1
                        archivo.write('"' + lista_lit[contador] + "00000000000001101" + '"' + ',' + "\n") # add A, dir2 la q crspone
                        archivo.write('"' + lista_lit[contador] + "00000000000000111" + '"' + ',' + "\n") #mov dir2, a
                        archivo.write('"' + "0000000011111111" + "00000000000000101" + '"' + ',' + "\n") #mov a, dir1

                        cont_dirs +=1
                    else:

                        archivo.write('"' + lista_lit[contador] + key +'"' +','+ "\n")
                        print(l,'CORRESPONDE 2')


                elif l == "LABEL":
                    print(l,'CORRESPONDE 2')
                   # print(l,'esta se busca', 'laabel')

                    archivo.write('"' + lista_lit[contador] + "00000000000000000" + '"' +',' +"\n")
        contador +=1


diccionario = generacion_diccionario()

lista_lit = []


def crea_dict_labels(code):
    dict_labels = {}
    cont_inc_dir = 0
    cont_doble_ins = 0
    cont_variables_iniciales = 0
    for i in direcciones_memoria.values():
        cont_variables_iniciales+=len(i)

    for j in code:




        aux = j.replace('(',"-")
        aux = aux.replace(')',"")
        aux = aux.replace(","," ")
        aux = aux.split(' ')
        if aux[0] == 'inc' and aux[1][0] == '-' and aux[1][1] != 'b':

            cont_inc_dir +=1
        if aux[0] == 'pop' or aux[0] == 'ret':

            cont_doble_ins+=1


        if aux[0][-1] == ':':


            #print(aux[0], code.index(j),'el indice que tiene', len(direcciones_memoria)*2,'len dir memo',cont_inc_dir,'nro de inc dirs', cont_doble_ins,'este el el contador doble ins')
            dict_labels[aux[0]] = code.index(j) + cont_variables_iniciales*2 + 4*cont_inc_dir + cont_doble_ins
            print(aux,'este es el index del code ->',code.index(j),'\/','-> inc dirs',cont_inc_dir)

            print(cont_variables_iniciales,'variables iniciales')
            print(cont_doble_ins,'conteo de doble ins')
            print(cont_inc_dir,'conteo inc dirs')
            print(aux,'este es aux',code.index(j) + cont_variables_iniciales*2 + 4*cont_inc_dir + cont_doble_ins,'direccion en code efectiva')


    return dict_labels
dict_labels = crea_dict_labels(code)



def crea_lista_literales(code, dict_labels, direcciones_memoria):

    for i in code:

        aux = i.replace('(',"-")
        aux = aux.replace(')',"")
        aux = aux.replace(","," ")
        aux = aux.split(' ')
        for j in aux:
            if j == "":
                aux.remove(j)



        if len(aux) == 3 and aux[1][0] == '-': #CASO DIR MEMORIA


            if aux[1][1:] in direcciones_memoria:

                lista_lit.append(direcciones_memoria[aux[1][1:]][0][0]) #hice 1 cambio para soportar literal en memorias
            elif aux[1][1].isdigit(): #antes era [1][1:] pero puede ser formato no decimal
                lista_lit.append(num_to_bin(aux[1][1:]))#da la direccion de memoria siendo un literal la direccion
            elif aux[2][0].isdigit(): # seria un mov dir,lit

                lista_lit.append(num_to_bin(aux[2])) #quizas no pasa nunca
            else:
                lista_lit.append('0000000000000000')



        elif len(aux) == 3 and aux[2][0] == '-': #CASO DIR MEMORIA chequiado

            if aux[2][1:] in direcciones_memoria:


                lista_lit.append(direcciones_memoria[aux[2][1:]][0][0]) # da la direccion de memoria siendo una variable
            else:
                lista_lit.append(num_to_bin(aux[2][1:])) #da la direccion de memoria siendo un literal la direccion



        elif len(aux) == 3 and aux[1].isdigit(): # creo que nunca lo pesca
            lista_lit.append(num_to_bin(aux[1]))
        elif len(aux) == 3 and aux[2][0].isdigit(): #caso instr A o B, lit antes no tenia el [0] es para soportar 10h
            lista_lit.append(num_to_bin(aux[2]))
        elif len(aux) == 2: #FALTA DIVIDIR EL CASO DE INC Y DEC

            if aux[1][0] == '-': # caso ins , mem
                if aux[1][1:] in direcciones_memoria: #aqui manejo el inc (b) si no esta en dir_memo tiro ceros

                    lista_lit.append(direcciones_memoria[aux[1][1:]][0][0]) #agregue un [0] pq ahora son tuplas
                else:
                    lista_lit.append('0000000000000000')


            elif aux[1] + ':' in dict_labels:


                numero = dict_labels[aux[1] + ':'] # NO ES NECESARIO+1 + 1 #este uno por la ins inicial
                print(numero,aux, 'este es el numero al que salta efectivo')
                
                lista_lit.append(num_to_bin(str(numero)))
            elif aux[1][0].isdigit():
                lista_lit.append(num_to_bin(aux[1]))

            else:
                lista_lit.append('0000000000000000')


        else:

            lista_lit.append('0000000000000000')

    return lista_lit



lista_lit = crea_lista_literales(code, dict_labels, direcciones_memoria)


global len_var_iniciales
len_var_iniciales = 0

for i in direcciones_memoria.values():
    len_var_iniciales+=len(i)






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
        for i in variable:




            output.write('"' + i[1] + mova_alit + '"' + ',\n')
            output.write('"' + i[0] + mov_dira + '"' + ',\n')


    funcion_transformadora(output, diccionario, code, lista_lit)


    for i in range(4095 - (len(code) + cont_dirs*4 + len_var_iniciales*2 + cont_dos_ciclos)):
        output.write('"000000000000000000000000000000000"' + ',' + '\n')
    texto_final = """"000000000000000000000000000000000"
); begin

    dataout <= memory(to_integer(unsigned(address)));

end Behavioral;   """
    output.write(texto_final)
    output.close()
    print(cont_dirs, 'contador de dirs')
    print(len_var_iniciales,' len variables init')
    print(cont_dos_ciclos,'contador de las de dos ciclos')
    return

creador_output(direcciones_memoria,code, lista_lit, diccionario)

#print(len(code))