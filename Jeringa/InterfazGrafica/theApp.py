#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 13:31:02 2017
la aplicacion
@author: maria
"""



from PyQt5 import QtWidgets, QtCore
import Ui_theApp  # Importamos nuestra interfaz
import serial

class TheApp(QtWidgets.QMainWindow, Ui_theApp.Ui_theApp):
    '''@class TheApp
    Aplicación ejemplo de Qt
    '''
#inicializador:
    def __init__(self, parent=None):
        '''Constructor.
        Inicialización de la aplicación.
        '''
        super(TheApp, self).__init__(parent)
        self.setupUi(self)
        self.updateUi()
        # Un atributo privado:
        #self.__count = 0
        # Conectando señales con slots:
        self.aPushButtonC.clicked.connect(self.__SlotComenzar)
        #self.aPushButton.clicked.connect(self.__anotherSlot)
        self.aPushButtonP.clicked.connect(self.__SlotParar)
#Es conveniente definir una función de sincronización de estados entre la 
#aplicación y la UI:
    def updateUi(self):
        '''IMPORTANTE:
        En esta función se sincronizan los elementos del programa con la UI.
        '''
         # En nuestro programa sencillo no tenemos estados almacenados.

#Agregando los slots
    def __SlotComenzar(self):
        Input=self.aLineEdit.text()
        with serial.Serial('COM3',9600) as arduino:        
            pasos=bytes(Input.encode())
            arduino.write(pasos)
            self.aLabel.setText('{} pasos enviados'.format(Input))
    def __SlotParar(self):
        with serial.Serial('COM3',9600) as arduino:        
            arduino.write("0".encode())
#Toda nuestra aplicación está lista, solo falta proveer de la rutina principal
# de ejecución, en nuestro archivo theApp.py:
#    def __aSlot(self):
#            self.aLabel.setText('¡Hola!')
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form = TheApp()
    form.show()
    sys.exit(app.exec_())
    try:
        sys.exit(app.exec_())
    except SystemExit as e:
        del app, form
        print("La aplicación se cerró con código: "+str(e))
