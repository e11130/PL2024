#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      dario
#
# Created:     14/03/2024
# Copyright:   (c) dario 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import ply.lex as lex
import sys
import re

stock = [     {"cod": "A1", "nome": "água 0.5L", "quant": 8, "preco": 0.7},
          {"cod": "A2", "nome": "saco patatas", "quant": 8, "preco": 1.2},
           {"cod": "A3", "nome": "cerveza", "quant": 8, "preco": 1.0},
            {"cod": "A4", "nome": "saco tomates", "quant": 8, "preco": 0.7}]



# List of token names.   This is always required
tokens = (
   'Listar',
   'Moneda',
   'Seleccionar',
   'Salir',
)

saldo = 0

# Regular expression rules for simple tokens

# A regular expression rule with some action code
def t_Moneda(t):
    r'(?i)moneda\s((1e|2e|50c|20c|10c|5c|2c|1c),)*\s((1e|2e|50c|20c|10c|5c|2c|1c)).'
    monedasMetidas = re.findall(r"(1c)|(2c)|(5c)|(10c)|(20c)|(50c)|(1e)|(2e)", t.value)
    global saldo
    for i in monedasMetidas:
        if i == "1c":
            saldo += 0.01
        elif i == "2c":
            saldo += 0.02
        elif i == "5c":
            saldo += 0.05
        elif i == "10c":
            saldo += 0.10
        elif i == "20c":
            saldo +=0.20
        elif i == "50c":
            saldo += 0.50
        elif i == "1e":
            saldo += 1.00
        elif i == "2e":
            saldo += 2.00


# A regular expression rule with some action code
#(?i) mayus y minus
#\b para que pille la palabra sola
def t_Listar(t):
    r'(?i)listar'
    for i in range(len(stock)):
        print("cod  | nombre    | cantidad  | precio")
        print("-----------------------")
##        print(""+ stock[i][0] + "\t" + stock[i][1] + "\t" + stock[i][1] + "\t" + stock[i][2])
        print(""+ stock[i]["cod"]  + "\t" + stock[i]["nome"] + "\t" + str(stock[i]["quant"]) + "\t" + str(stock[i]["preco"]))
# A regular expression rule with some action code
def t_Seleccionar(t):
    r'(?i)seleccionar\sA\d+'
    codR = re.search(r"(?<=A)\d+",t.value)
    cod = int(codR.group())
    global saldo
    if cod <= len(stock) and cod > 0:
        articulo = stock[cod]["nome"]
        valor = stock[cod]["preco"]

        if valor <= saldo:
            print("Artículo " + articulo + " ha sido seleccionado")
            saldo-=valor
        else:
            print("Saldo insuficiente, faltan: ", (valor-saldo), "e")
    else:
        print("No existe producto que corresponda a ese código")

    return t

def calculaCambio():
    valor = 0
    cambio = {}
    for i in [2,1,0.5,0.2,0.1,0.05,0.02,0.01]:
        if valor == saldo:
            break
        cont = 0
        while valor+i <= saldo:
            valor+= i
            cont+=1
        cambio[i]=cont
    return cambio

def cambioBien(cambio):
    c = ""
    for i in cambio:
        c += cambio[i] + " x " + i + " "
    return c


# A regular expression rule with some action code
def t_Salir(t):
    r"(?i)\bSalir\b"
    cambio = calculaCambio()
    cambioB = cambioBien(cambio)
    print(f"Cambio: {cambioB}")
    print("Muchas gracias")
    exit()

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

### Build the lexer
##lexer = lex.lex()
##
##
### Give the lexer some input
##lexer.input(data)


print("2024-03-08, Stock carregado, Estado atualizado.")
print("Bom dia. Estou disponível para atender o seu pedido.")
lexer = lex.lex()
linha = "moneda  1e, 20c, 5c, 5c."
lexer.input(linha)
for tok in lexer:
        print(tok)