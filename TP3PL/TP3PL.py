#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      dario
#
# Created:     27/02/2024
# Copyright:   (c) dario 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import re

def sumador_onoff(texto):

    activo = True
    suma = 0
    lista = re.split(r"(?<=\d)(?=\D)|(?<=\D)(?=\d)",texto)

    for i in lista:

        if re.search(r"\d+",i) and activo:
            suma += int(i)
            print("+ ",i)

        elif re.search(r"on|On|ON|oN",i):
            activo = True
            print("vuelve a ir")

        elif re.search(r"off|OFF|Off|OFf|OfF|ofF",i):
            activo = False
            print("deja de funcionar")

        elif i == "=":
            print(suma)




print(sumador_onoff("123abc456=789Off321On987=0"))