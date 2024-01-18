class operacionBasica:
    #Declaracion de propiedades
    num1 = 0
    num2 = 0
    res = 0
    #declaracion del constructor de la clase
    def __init__(self,a,b):
        self.num1 = a
        self.num2 = b 
    #metodos de prueba

    def suma(self):
        self.res = self.num1 + self.num2
        print("la suma es: {}".format(self.res))

def main():
    obj = operacionBasica(3,5)
    obj.suma()
if __name__ == "__main__":
        main()
    
