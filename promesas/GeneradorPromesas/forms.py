from django import forms

class formularioPromesas(forms.Form):
    RT = forms.CharField()
    fecha_RT = forms.CharField()
    # numeroPromesa = forms.CharField(required = False)
    direccion = forms.CharField()
    folio = forms.CharField()
    Cedula_Catastral = forms.CharField()
    CHIP = forms.CharField()
    area = forms.FloatField()
    avaluo = forms.CharField()
    Fecha_Avaluo = forms.CharField()
    descripcion_de_la_Construccion = forms.CharField()
    valor_Terreno = forms.IntegerField()
    valor_Dano = forms.IntegerField()
    valor_Lucro = forms.IntegerField()
    CDP = forms.IntegerField()
    fecha_CDP = forms.CharField()
    # resolucion = forms.IntegerField(required = False)
    # fechaResolucion = forms.CharField(required = False)
    proyecto = forms.CharField()
    # linderosEP = forms.CharField(required = False)
    # linderosRT = forms.CharField(required = False)