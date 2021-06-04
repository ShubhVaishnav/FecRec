from django import forms
from .models import *


class TestForm(forms.ModelForm):
    class Meta:
        model = TestForm
        fields = ['Test_Img']

