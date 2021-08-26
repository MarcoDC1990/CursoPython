# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 08:41:52 2021

@author: mdcor
"""

numero=10
maximo=5
if numero>maximo:
    raise Exception("El número a ingresar no debe ser mayor que {}.el valor ingresado fue: {}'. format(maximo,numero"))