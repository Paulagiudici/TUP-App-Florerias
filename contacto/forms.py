from django import forms
from .models import MensajeContacto

class ContactoForm(forms.Form):  # <-- ¡Asegúrate de que el nombre coincida!
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)

