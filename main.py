from flask import *
from math import *
from forms import Punto
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