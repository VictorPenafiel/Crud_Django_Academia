from django import forms
from web.models import *

class MainForm(forms.Form):
    region_selector = forms.ModelChoiceField(queryset=Region.objects.all(), to_field_name='codigo_region',label="Región", widget=forms.Select(attrs={'class':'form-select'}), required=False, empty_label="Seleccione una región")
    curso_selector = forms.ModelChoiceField(queryset=Curso.objects.all(), to_field_name='codigo_curso',label="Curso", widget=forms.Select(attrs={'class':'form-select'}), required=False, empty_label="Seleccione un curso")