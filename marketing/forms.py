# -*- coding: utf-8 -*-
u''

from django import forms
from marketing.models import Promocion, Suscriptores, Receta

class PromoForm(forms.ModelForm):
    class Meta:
        model = Promocion
        fields = '__all__'

class CorreoForm(forms.ModelForm):
    class Meta:
        model = Suscriptores
        fields = '__all__'

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = [
            'imagen',
        ]
