#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 14:01:56 2017

@author: maria
"""

import serial 
with serial.Serial('COM3',9600) as arduino:
    print("Ingrese número de pasos: " )
    banderaInput=input()
    bandera=bytes(banderaInput.encode())
    arduino.write(bandera)
    while True:
        print (arduino.readline().decode('utf-8'))
#arduino.close()