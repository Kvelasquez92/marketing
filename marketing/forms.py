# -*- coding: utf-8 -*-
u''

from django import forms
from marketing.models import Promocion

class PromoForm(forms.ModelForm):
    class Meta:
        model = Promocion
        fields = '__all__'
