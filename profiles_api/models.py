"---IMPORTS-------------------------//"

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

"---MANAGER DEL PERFIL DE USUARIO-------------------------//"

class UserProfileManager(BaseUserManager):
    #Se encarga de permitirnos la creacion de usuarios, debido a que
    #nuestro modelo posee un sistema de usuarios distinto al default de django.
    
    def create_user(self, email, name, password=None):
        #Crea un nuevo perfil de usuario
        if not email:
            raise ValueError("El usuario debe tener una direccion email.")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_super_user(self, email, name, password):
        #Crea un perfil de super usuario.
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


"---PERFIL DE USUARIO-------------------------//"

class UserProfile(AbstractBaseUser,PermissionsMixin):
    #Modelo de la BDD para usuarios en el sistema
    #Hecha con la idea de cambiar el user por email.
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        #Devuelve el nombre del usuario.
        return self.name
    
    def get_short_name(self):
        #Igual pero corto :B
        return self.name

    def __str__(self):
        #Devuelve la representacion del user en string.
        return self.email
    