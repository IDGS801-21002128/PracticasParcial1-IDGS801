from wtforms import Form,FloatField,SelectField,RadioField,StringField,validators

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

class Diccionario(Form):
    buscar = StringField("Buscar")
    ingles = StringField("Ingles",[
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=2,max=10,message="ingresa palabra valida")
    ])
    español = StringField("Español",[
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=2,max=10,message="ingresa palabra valida")
    ])
    palabraRadio = RadioField("palabraRadio", choices=[("ingles"),("español")],validators=
        [validators.DataRequired(message="Selecciona un lenguaje")
    ]) 
    