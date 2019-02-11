# -*- coding: utf-8 -*-
import sys
from math import exp, fabs, sin, cos, log
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from metodos import MetodosHalleyRidders
import numpy as np



Ui_MainWindow, QtBaseClass = uic.loadUiType("metodoshalleyeridders.ui")

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButtonCalcularHalley.clicked.connect(self.calcularHalley)
        self.ui.pushButtonCalcularRidders.clicked.connect(self.calcularRidders)
        
    def calcularHalley(self):
        
        mtds = MetodosHalleyRidders()
        f = lambda x: eval(self.ui.lineEditFuncaoHalley.text())
        d1f = lambda x: eval(self.ui.lineEditDerivadaHalley.text())
        d2f = lambda x: eval(self.ui.lineEditDerivada2Halley.text())
        x0 = eval(self.ui.lineEditX0.text())
        self.ui.lineEditRaizHalley.setText((str)(mtds.halley(f, d1f, d2f, x0, 0.001, 100)))
        
        x = np.arange(0, 8, 0.001)
        y = f(x)
        self.ui.MplWidgetHalley.canvas.axes.clear()
        self.ui.MplWidgetHalley.canvas.axes.axhline(y=0, color='r')
        self.ui.MplWidgetHalley.canvas.axes.plot(x, y, label='f(x)')
        self.ui.MplWidgetHalley.canvas.axes.legend()
        self.ui.MplWidgetHalley.canvas.axes.grid()
        self.ui.MplWidgetHalley.canvas.draw()
        
        
    def calcularRidders(self):
        
        mtds = MetodosHalleyRidders()
        f = lambda x: eval(self.ui.lineEditFuncaoRidders.text())
        x1 = eval(self.ui.lineEditX1Ridders.text())
        x2 = eval(self.ui.lineEditX2Ridders.text())
        self.ui.lineEditRaizRidders.setText((str)(mtds.ridders(f, x1, x2, 0.001, 100)))
        
        x = np.arange(0, 20.2, 0.001)
        y = f(x)
        self.ui.MplWidgetRidders.canvas.axes.clear()
        self.ui.MplWidgetRidders.canvas.axes.axhline(y=0, color='r')
        self.ui.MplWidgetRidders.canvas.axes.plot(x, y, label='f(x)')
        self.ui.MplWidgetRidders.canvas.axes.legend()
        self.ui.MplWidgetRidders.canvas.axes.grid()
        self.ui.MplWidgetRidders.canvas.draw()

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())