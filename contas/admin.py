from django.contrib import admin
from .models import Usuario, Aluno, Professor
from .forms import ProfessorForm, AlunoForm
from django import forms

# Register your models here.


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('Email','Usuario','password','is_staff','is_superuser','Professor',
                  'Aluno', 'Data_Associacao', 'last_login', 'Ativo')

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user



class UserAdmin(admin.ModelAdmin):
    form = UserCreationForm

class ProfessorAdmin(admin.ModelAdmin):
    form = ProfessorForm

class AlunoAdmin(admin.ModelAdmin):
    form = AlunoForm



admin.site.register(Usuario, UserAdmin)
admin.site.register(Aluno,AlunoAdmin)
admin.site.register(Professor,ProfessorAdmin)

