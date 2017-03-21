from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.db import models
from django.utils import timezone
from django.conf import settings



class UserManager(BaseUserManager):
    def create_user(self, Email, Usuario, password=None):


        user = self.model(
            Email=self.normalize_email(Email),
            Usuario=Usuario,
            password=password
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, Email, Usuario, password):
        user = self.create_user(
            Email,
            Usuario,
            password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user



class Usuario(AbstractBaseUser,PermissionsMixin):
    Usuario = models.CharField(max_length=20, unique=True)
    Email = models.EmailField(unique=True)
    Data_Associacao = models.DateTimeField(default=timezone.now)
    Ativo = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    Professor = models.BooleanField(default=False)
    Aluno = models.BooleanField(default=False)

    USERNAME_FIELD = "Email"
    REQUIRED_FIELDS = ["Usuario"]
    objects = UserManager()

    def __str__(self):
        return "@{}".format(self.Usuario)

    def get_short_name(self):
        return self.Usuario



class Professor(models.Model):
    Nome_Completo = models.CharField(max_length=255)
    Matricula = models.AutoField(primary_key=True, max_length=10)
    Usuario = models.OneToOneField(settings.AUTH_USER_MODEL)
    Data_Nascimento = models.DateTimeField('Data de Nascimento')
    Endereco = models.TextField(max_length=200)
    Instituicao = models.CharField('Instituição de Ensino', max_length=80)


class Aluno(models.Model):
    Nome_Completo = models.CharField(max_length=255)
    Matricula = models.AutoField(primary_key=True, max_length=10)
    Usuario = models.OneToOneField(settings.AUTH_USER_MODEL)
    Data_Nascimento = models.DateTimeField('Data de Nascimento')
    Endereco = models.TextField(max_length=200)
    Instituicao = models.CharField('Instituição de Ensino', max_length=80)