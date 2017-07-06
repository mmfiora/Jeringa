#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 10:49:43 2017
Interfaz grafica o interfaz de usuario Ui
@author: maria
"""

from PyQt5 import QtCore, QtGui, QtWidgets
#clase interfaz grafica que depende de la aplicacion:
class Ui_theApp(object):
    #la funcion setup es la funcion de configuracion
    def setupUi(self,theApp):
        theApp.setObjectName("TheApp")
        theApp.resize(400, 200)
        # El widget central --------------------------------------------------#
        self.centralwidget = QtWidgets.QWidget(theApp)  # Aquí se determina el
                                                        # "padre" del objeto.
        # Comportamiento frente al resize:
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy()
                                     .hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        # Nombre del objeto:
        self.centralwidget.setObjectName("centralwidget")
        

#Ahora digamos como se deben organizar los elementos, definiendo un 
#Layout:

    # Layout Vertical ---------------------------------------------------#
        self.VerticalLayout = QtWidgets.QVBoxLayout(
                self.centralwidget)
        
    # Layout Horizontal ---------------------------------------------------#
        self.PrimerHorizontalLayout = QtWidgets.QHBoxLayout(
        self.centralwidget)
        self.SegundoHorizontalLayout = QtWidgets.QHBoxLayout(
        self.centralwidget)
                

#Etiqueta numero de pasos --------------------------------------------------#
        self.aLabel=QtWidgets.QLabel(self.centralwidget)
        self.aLabel.setText("Ingresar cantidad de pasos:")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aLabel.sizePolicy()
                                     .hasHeightForWidth())
        self.aLabel.setSizePolicy(sizePolicy)
        self.aLabel.setMinimumSize(QtCore.QSize(60, 20))
        # Agregándolo al Layout
        self.PrimerHorizontalLayout.addWidget(self.aLabel)
        
#Linea a completar por el usuario -------------------------------------------#
        self.aLineEdit=QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aLineEdit.sizePolicy()
                                     .hasHeightForWidth())
        self.aLineEdit.setSizePolicy(sizePolicy)
        self.aLineEdit.setMinimumSize(QtCore.QSize(60, 20))
        # Agregándolo al Layout
        self.PrimerHorizontalLayout.addWidget(self.aLineEdit)
        self.VerticalLayout.addLayout(self.PrimerHorizontalLayout)
#        Input=self.aLineEdit.displayText
#Boton comenzar -----------------------------------------------------------#
        self.aPushButtonC = QtWidgets.QPushButton(self.centralwidget)
        self.aPushButtonC.setText("Comenzar")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aPushButtonC.sizePolicy()
                                     .hasHeightForWidth())
        self.aPushButtonC.setSizePolicy(sizePolicy)
        self.aPushButtonC.setMinimumSize(QtCore.QSize(60, 20))
        # Agregándolo al Layout
        self.SegundoHorizontalLayout.addWidget(self.aPushButtonC)
        
#Boton parar -----------------------------------------------------------#
        self.aPushButtonP = QtWidgets.QPushButton(self.centralwidget)
        self.aPushButtonP.setText("Parar")        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aPushButtonP.sizePolicy()
                                     .hasHeightForWidth())
        self.aPushButtonP.setSizePolicy(sizePolicy)
        self.aPushButtonP.setMinimumSize(QtCore.QSize(60, 20))
        # Agregándolo al Layout
        self.SegundoHorizontalLayout.addWidget(self.aPushButtonP)
        self.VerticalLayout.addLayout(self.SegundoHorizontalLayout)

## Otra etiqueta ------------------------------------------------------#
#        
#        self.anotherLabel = QtWidgets.QLabel(self.centralwidget)
#        self.anotherLabel.setObjectName("anotherLabel")
#        # Agregándola al Layout
#        self.VerticalLayout.addWidget(self.anotherLabel)
# Agregando el widget central a la aplicación ------------------------#
        theApp.setCentralWidget(self.centralwidget)       



#main de prueba :     
if __name__ == "__main__":
    import sys #biblioteca System-specific parameters and functions
     
    #crea la aplicacion:
    app = QtWidgets.QApplication(sys.argv)
    #sys.argvs retorna una lista con todos 
    #los argumentos pasados por línea de comandos
    #crea la ventana pricipal:
    theApp = QtWidgets.QMainWindow()
    #clase interfaz grafica:
    ui = Ui_theApp()
    #la funcion definida dentro de la clase Ui_theApp evaluada en la aplicacion:
    ui.setupUi(theApp)
    # muestra la ventana principal
    theApp.show()
    #sys.exit(app.exec_())

   
    
   
    
    
    
    
    