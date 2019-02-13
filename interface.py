# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from metodos import MetodosHalleyRidders
from numpy import exp, log, sin, cos, fabs
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvas

from matplotlib.figure import Figure



Ui_MainWindow, QtBaseClass = uic.loadUiType("metodoshalleyeridders.ui")

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButtonCalcularHalley.clicked.connect(self.calcularHalley)
        self.ui.pushButtonCalcularRidders.clicked.connect(self.calcularRidders)
        self.ui.pushButtonAtualizarLimitesHalley.clicked.connect(self.desenhaGraficoHalley)
        self.ui.pushButtonAtualizarLimitesRidders.clicked.connect(self.desenhaGraficoRidders)
        
    def calcularHalley(self):
        
        mtds = MetodosHalleyRidders()
        f = lambda x: eval(self.ui.lineEditFuncaoHalley.text())
        d1f = lambda x: eval(self.ui.lineEditDerivadaHalley.text())
        d2f = lambda x: eval(self.ui.lineEditDerivada2Halley.text())
        x0 = eval(self.ui.lineEditX0.text())
        self.ui.lineEditRaizHalley.setText((str)(mtds.halley(f, d1f, d2f, x0, 0.001, 100)))
        self.ui.lineEditLimiteEsquerdoHalley.setText((str)(0))
        self.ui.lineEditLimiteDireitoHalley.setText((str)(20))
        
        self.desenhaGraficoHalley()
        
    def calcularRidders(self):
        
        mtds = MetodosHalleyRidders()
        f = lambda x: eval(self.ui.lineEditFuncaoRidders.text())
        x1 = eval(self.ui.lineEditX1Ridders.text())
        x2 = eval(self.ui.lineEditX2Ridders.text())
        self.ui.lineEditRaizRidders.setText((str)(mtds.ridders(f, x1, x2, 0.001, 100)))
        self.ui.lineEditLimiteEsquerdoRidders.setText((str)(0))
        self.ui.lineEditLimiteDireitoRidders.setText((str)(20))
        
        self.desenhaGraficoRidders()
        
    def desenhaGraficoHalley(self):
        
        f = lambda x: eval(self.ui.lineEditFuncaoHalley.text())
        limEsq = (float)(self.ui.lineEditLimiteEsquerdoHalley.text())
        limDir = (float)(self.ui.lineEditLimiteDireitoHalley.text())
        x = np.arange(limEsq, limDir, 0.001)
        y = f(x)
        
        self.ui.MplWidgetHalley.canvas.axes.clear()
        self.ui.MplWidgetHalley.canvas.draw()
        self.ui.MplWidgetHalley.canvas.axes.set_xlim([limEsq, limDir])
        self.ui.MplWidgetHalley.canvas.axes.axhline(y=0, color='r')
        self.ui.MplWidgetHalley.canvas.axes.plot(x, y, label='f(x)')
        self.ui.MplWidgetHalley.canvas.axes.legend()
        self.ui.MplWidgetHalley.canvas.axes.grid()
        self.ui.MplWidgetHalley.canvas.draw()
        
        
    def desenhaGraficoRidders(self):
        
        f = lambda x: eval(self.ui.lineEditFuncaoRidders.text())
        limEsq = (float)(self.ui.lineEditLimiteEsquerdoRidders.text())
        limDir = (float)(self.ui.lineEditLimiteDireitoRidders.text())
        x = np.arange(limEsq, limDir, 0.001)
        y = f(x)
        
        self.ui.MplWidgetRidders.canvas.axes.clear()
        self.ui.MplWidgetRidders.canvas.draw()
        self.ui.MplWidgetRidders.canvas.axes.set_xlim([limEsq, limDir])
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