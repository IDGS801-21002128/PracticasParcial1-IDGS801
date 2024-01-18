
class listaOperacion:
    #Declaracion de propiedades
    n=0
    #declaracion del constructor de la clase
    def __init__(self,lista):
        self.n = lista
    #metodos de prueba

    def ordenarLista(self):
        lista = self.n
        listaRepetidos=[]
        print("lista ordenada: ", sorted(lista))
    def numerosParesImpares(self):
        listaPares = []
        listaImpares=[]
        lista = self.n
        for numero in lista:
            if numero % 2 == 0:
                listaPares.append(numero)
            else:
                listaImpares.append(numero)
        print("lista pares: ", listaPares)
        print("lista impares: ",listaImpares)
    def repetidos(self):
        countRepetido={}
        lista = self.n
        for n in lista:
            countRepetido[n] = lista.count(n)
        for n,repetido in countRepetido.items():
            if repetido>1:
                print(f"El numero {n} se repite {repetido} veces")

def main():
    objLista = []
    for i in range(5):
        num = int(input("inserta una numero: "))
        objLista.append(num)
    print(objLista)
    obj = listaOperacion(objLista)
    obj.ordenarLista()
    obj.numerosParesImpares()
    obj.repetidos()
if __name__ == "__main__":
        main()
    
