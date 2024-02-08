from wtforms import Form,FloatField,SelectField,RadioField

class Punto(Form):
    x = FloatField('Punto x')
    y = FloatField('Punto y')
    x2 = FloatField('Punto x2')
    y2 = FloatField('Punto y2')

class Resistencias(Form):
    PrimerResistencia = SelectField("Primer Resistencia")
    SegundaResistencia = SelectField("Segunda Resistencia")
    TerceraResistencia = SelectField("Tercer Resistencia")
    tolerancia = RadioField("Tolerancia")
