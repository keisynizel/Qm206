import numpy as np

class estadistica:
    def __init__(self,x):
        self.x=x
    def promedio(self):
        n=len(self.x)
        promedio=sum(self.x)/n
        return promedio
    def varianza(self):
        n=len(self.x)
        sigma2=sum((self.x-promedio(self.x))*(self.x-promedio(self.x)))/(n-1)
        return sigma2
    def minimo(self):
        minx=9E99
        for a in self.x:
            if a <minx:
                minx=a
        return minx
    def maximo(self):
        max_x=-9E99
        for a in self.x:
            if a >max_x:
                max_x=a
        return max_x