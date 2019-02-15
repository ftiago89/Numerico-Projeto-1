# -*- coding: utf-8 -*-
from math import exp, fabs, sin, cos, log

class MetodosHalleyRidders():

    #metodo de Halley
    def halley(self, f, d1f, d2f, x0=1.0, erroLim=0.001, imax=100):
        """
        retorna a raiz de f utilizando o metodo de Halley
        
        * f: funcao
        * d1f: derivada de f
        * d2f: derivada segunda de f
        * x0: estimativa de ponto incial
        * erroLim: erro limite para finalizar o metodo
        * imax: maximo de iteracoes
    
        """
    
        xn = x0
        errItr = erroLim + 1
        iteracoes = 0
        
        while errItr > erroLim and iteracoes < imax:
            x0 = xn
            xn = xn - (2*f(xn)*d1f(xn))/(2*d1f(xn)*d1f(xn) - f(xn)*d2f(xn))
            iteracoes += 1
    
            if xn != 0:
                errItr = fabs((xn-x0)/xn)
    
        return xn
    
    #metodo de Ridders
    def ridders(self, F, xl, xr, errLim=0.001, imax=100):
         """
         retorna a raiz de f utilizando o método de Ridders
         
         f: funcao
         xl: limite esquerdo do intervalo
         xr: limite direito do intervalo
         imax: maximo de iteracoes
         erroLim: erro limite para finalizar o metodo
    
         """
         x = 0
         iteracoes = 0
         erroItr = 1
    
         while erroItr > errLim and iteracoes < imax:          
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
       
              erroItr = abs(xr - xl)
              iteracoes += 1
         return x