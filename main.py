from flask import *
from math import *
from forms import Resistencias
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