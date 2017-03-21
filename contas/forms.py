from dal import autocomplete
from .models import Professor, Aluno
from django import forms


class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ('__all__')
        widgets = {
            'Usuario': autocomplete.ModelSelect2(url='usuarios-autocomplete')
        }


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ('__all__')
        widgets = {
            'Usuario': autocomplete.ModelSelect2(url='usuarios-autocomplete')
        }