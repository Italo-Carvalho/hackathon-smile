from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.db.models import fields
from django.forms import ModelForm

from .models import *


class CustomUsuarioCreateForm(UserCreationForm):

    class Meta:
        model = CustomUsuario
        fields = ('username', 'first_name', 'last_name',)
        labels = {'username': 'E-mail'}
        widgets = {
            'username': forms.EmailInput(),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["username"]
        if commit:
            user.save()
        return user


class CustomUsuarioChangeForm(UserChangeForm):

    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name',)


class ViagemForm(ModelForm):

    class Meta:
        model = Viagem
        fields = ['salario', 'porcentagem', 'estado', 'lugar']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['lugar'].queryset = Lugar.objects.none()

        if 'estado' in self.data:
            try:
                estado_id = int(self.data.get('estado'))
                self.fields['lugar'].queryset = Lugar.objects.filter(
                    estado_id=estado_id).order_by('nome')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['lugar'].queryset = self.instance.estado.local_set.order_by(
                'nome')


class ExtrasForm(ModelForm):

    class Meta:
        model = Extras
        fields = ['ativadade', 'hospedagem', 'restaurante', 'viagem']
