
class operacionBasica:
    #Declaracion de propiedades
    n=0
    #declaracion del constructor de la clase
    def __init__(self,a):
        self.n = a
    #metodos de prueba

    def imprimirEscalera(self):
        for i in range(1,self.n+1):
            print("*" * i)

def main():
    obj = operacionBasica(3)
    obj.imprimirEscalera()
if __name__ == "__main__":
        main()
    
