from flask import *
from math import *
from io import open

from forms import Resistencias,Diccionario
app=Flask(__name__)


@app.route("/distancia",methods=["GET","POST"])
def calDistancia():
    distanciaClase = Punto(request.form)
    x=''
    y=''
    x2=''
    y2=''
    resultado=''
    if request.method == "POST":
        x = distanciaClase.x.data
        y = distanciaClase.y.data
        x2= distanciaClase.x2.data
        y2=distanciaClase.y2.data

        resultado=sqrt((x2-x)**2 + (y2-y)**2)
        
    return render_template("distancia.html",form=distanciaClase,x=x,y=y,resultado=resultado)

@app.route("/dir",methods=["GET","POST"])
def diccionario():
    dir = Diccionario(request.form)
    ingles = ""
    español = ""
    palabraRadio = ""
    buscar = ""
    resultado=""
    archivo1=""
    if request.method == "POST":
        if request.form.get("btn") == "Registrar":
            dir.buscar.validators=[]
            dir.palabraRadio.validators=[]
            print("JEJE")
            if dir.validate():
                ingles = dir.ingles.data
                español = dir.español.data
                
                archivo1 = open("diccionario.txt","a")
                archivo1.write(ingles+","+español+"\n")
                archivo1.close()
        else:   
            dir.ingles.validators=[]
            dir.español.validators=[]
            if dir.validate():
                buscar = dir.buscar.data
                palabraRadio = dir.palabraRadio.data
                archivo1= open("diccionario.txt","r")
                datos = archivo1.readlines()
                for item in datos:
                    
                    palabra = item.strip().split(",")
                    
                    if palabra[0] == buscar and palabraRadio == "ingles": 
                        resultado=palabra[1]
                        break
                    elif palabra[1] == buscar and palabraRadio == "español":
                        resultado=palabra[0]
                        break
                    else:
                        resultado="no existe"
                   
    print(resultado)
    return render_template("diccionario.html",form=dir,resultado=resultado,buscar=buscar,ingles= ingles, español=español,palabraRadio=palabraRadio)

@app.route("/resis",methods=["GET","POST"])
def calResis():
    resistencia = Resistencias(request.form)
    R1=''
    R2=''
    R3=''
    oro=''
    plata=''
    resultado=''
    junto = ''
    colores = {"Negro":0,"Cafe":1,"Rojo":2,"Naranja":3,"Amarillo":4,"Verde":5,"Azul":6,"Violeta":7,"Gris":8,"Blanco":9}
    multiplicador = {"Negro":1,"Cafe":10,"Rojo":100,"Naranja":1000,"Amarillo":10000,"Verde":100000,"Azul":1000000,"Violeta":10000000,"Gris":100000000,"Blanco":1000000000}
    fin =''
    max=''
    min=''
    tol=''
    if request.method == "POST":
        R1 = resistencia.PrimerResistencia.data
        R2 = resistencia.SegundaResistencia.data
        R3 = resistencia.TerceraResistencia.data
        tolerancia = resistencia.tolerancia.data

        junto = str(colores[R1]) + str(colores[R2])
        
        resultado = int(junto) * multiplicador[R3]
        print(resultado)
        print()
        if tolerancia == "oro":
            tol=tolerancia
            fin = resultado*0.05
        elif tolerancia=="plata":
            tol=tolerancia
            fin = resultado*0.10
        else:
            fin =resultado
        
        max=resultado+fin
        min=resultado-fin
      

    return render_template("resistencia.html",form=resistencia, tol=tol,colores=colores, R1=R1, R2=R2,R3=R3,oro=oro,plata=plata,multiplicador=multiplicador,max=max,min=min,resultado=resultado,fin=fin)


    
@app.route("/resultado",methods=["GET","POST"])
def resultado():
     if request.method == "POST":
        n1 = request.form.get("n1")
        n2 = request.form.get("n2")
        suma = request.form.get("suma")
        resta = request.form.get("resta")
        multiplicacion = request.form.get("multiplicacion")
        division = request.form.get("division")
        if suma == "on":
            return "la suma de {} + {} es: {}".format(n1,n2,str(int(n1)+int(n2)))
        elif resta == "on":
            return "la resta de {} - {} es: {}".format(n1,n2,str(int(n1)-int(n2)))
        elif multiplicacion == "on":
            return "la multiplicacion de {} x {} es: {}".format(n1,n2,str(int(n1)*int(n2)))
        elif division == "on":
            return "la division de {} / {} es: {}".format(n1,n2,str(int(n1)/int(n2)))

     
if __name__=="__main__":
    app.run(debug=True)  