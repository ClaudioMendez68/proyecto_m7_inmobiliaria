from django import forms
from .models import SolicitudArriendo, Usuario
from django.contrib.auth.models import User

class SolicitudArriendoForm(forms.ModelForm):
    
    class Meta:
        model = SolicitudArriendo
        fields = ["estado", "usuario", "inmueble"]
        
        widgets = {
            "estado": forms.HiddenInput(),
            "usuario": forms.HiddenInput(),
            "inmueble": forms.HiddenInput()
        }
        
class SolicitudArrendadorForm(forms.ModelForm):
    
    class Meta:
        model = SolicitudArriendo
        fields = ["estado", "usuario", "inmueble"]
        
        widgets = {
            "estado" : forms.ChoiceField(choices=[(1, 'Aceptada'), (2, 'Rechazada'), (3, 'Pendiente')]),
            "usuario": forms.CharField(),
            "inmueble": forms.CharField()
        }
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    # password_confirm = forms.CharField(widget=forms.PasswordInput, label="Repita su password")
    
    class Meta:
        model = Usuario
        fields = ("rut", "direccion", "telefono")
        
'''        
    def clean_password(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Sus passwords no coinciden")
        
        return password_confirm
'''
        
class UserUpdateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = Usuario
        fields = ("rut", "direccion", "telefono")
'''        
class SolicitudArriendoForm(forms.ModelForm):
    class Meta:
        model = SolicitudArriendo
        fields = ['usuario', 'inmueble']     
'''