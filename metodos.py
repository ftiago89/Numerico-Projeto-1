# -*- coding: utf-8 -*-
from math import exp, fabs, sin, cos, log

class MetodosHalleyRidders():

    #metodo de Halley
    def halley(self, f, d1f, d2f, x0=1.0, errto=0.001, imax=100):
        """
        retorna a raiz de f utilizando o metodo de Halley
        
        * f: funcao
        * d1f: derivada de f
        * d2f: derivada segunda de f
        * x0: estimativa de ponto incial
        * errto: erro de uma iteracao para outra
        * imax: maximo de iteracoes
    
        return: the root next x0
    
        """
    
        xn = x0
        errno = errto + 1
        iterCount = 0
        
        while errno > errto and iterCount < imax:
            x0 = xn
            xn = xn - (2*f(xn)*d1f(xn))/(2*d1f(xn)*d1f(xn) - f(xn)*d2f(xn))
            iterCount += 1
    
            if xn != 0:
                errno = fabs((xn-x0)/xn)
    
        return xn
    
    #metodo de Ridders
    def ridders(self, F, xl, xr, errto=0.001, imax=100):
         """
         retorna a raiz de f utilizando o método de Ridders
         
         f: funcao
         xl: limite esquerdo do intervalo
         xr: limite direito do intervalo
         imax: maximo de iteracoes
         errto: erro de uma iteracao para outra
    
         """
         x = 0
         iterCount = 0
         errno = 1
    
         while errno > errto and iterCount < imax:          
              fr = F(xr)
              fl = F(xl)
              d0 = abs(fr - fl)
              x = xr - fr*(xl-xr)/(fl - fr)
              fx = F(x)
              
              a = (fl - fx)/(fx - fr)
              b = (fl - fx)/(fl - a*fx)
              beta = b - 1
              alfa = a - 1
              lnb = beta - beta*beta/2 + beta*beta*beta/3
              lna = alfa - alfa*alfa/2 + alfa*alfa*alfa/3
              root = xl + d0*lnb/lna
              froot = F(root)
    
              if fl * fx < 0:
                   if xl < root and root < x:
                        if fx * froot < 0:
                             xl = root
                             xr = x
                        else:
                             xr = root
                   else:
                        xr = x
              elif fl * fx > 0:
                   if x < root and root < xr:
                        if fx * froot < 0:
                             xl = x
                             xr = root
                        else:
                             xl = root
                             fl = froot
                   else:
                        xl = x
                        fl = fx
              else:
                   if fl == 0:
                        x = xl
                   break
       
              errno = abs(xr - xl)
              iterCount += 1
         return x
    
"""
if __name__ == "__main__":
    f = lambda x: exp(-x) + x/5.0 - 1.0
    d1f = lambda x: -exp(-x)+ 1.0/5.0
    d2f = lambda x: exp(-x)

    print("Uma raiz se encontra em x = " + (str)(halley(f,d1f,d2f,x0=2)))

    #print("Uma raiz se encontra em x = " + (str)(ridders((lambda x: x*log(x/3) - x), 1.5, 20.2, 1e-14, 500)))
    
    #plotGrafico((lambda x: x*np.log(x/3) - x), 1.5, 20.2, 0.001, -5, 5)
    
    plotGrafico((lambda x: np.exp(-x) + x/5.0 - 1.0), -5, 10, 0.001, -5, 5)
"""