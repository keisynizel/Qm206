class RegLineal:
    def __init__(self):
        self.intercepto=0
        self.pendiente=0
    def regresion_lineal(self,x,y):
        n=len(x)
        detM=n*sum(x*x)-sum(x)*sum(x)
        detA=sum(y)*sum(x*x)-sum(x*y)*sum(x)
        detB=n*sum(x*y)-sum(x)*sum(y)
        a=detA/detM
        b=detB/detM
        self.intercepto=a
        self.pendiente=b
        return[a,b]
    def graficar(self,x,y):
        ycalc=self.intercepto+self.pendiente*x
        plt.plot(x,y,'ro')
        plt.plot(x,ycalc,'b--')
        plt.xlabel("Concentración(Mol/L)")
        plt.ylabel("Absorbancia")
        plt.suptitle("Curva de Calibración de Fe")
        plt.show()