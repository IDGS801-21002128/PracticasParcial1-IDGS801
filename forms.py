from wtforms import Form,FloatField

class Punto(Form):
    x = FloatField('Punto x')
    y = FloatField('Punto y')
    x2 = FloatField('Punto x2')
    y2 = FloatField('Punto y2')
   