from django import forms

class profesionalForms(forms.Form):
    nombre = forms.CharField(label="nombre del curso",max_length=50, required=True)
    apellido = forms.CharField(label="apellido",max_length=50, required=True)
    email = forms.EmailField(label="email", required=False)
    profesion = forms.CharField(label="profesion", required=True)