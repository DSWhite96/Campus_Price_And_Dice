from django.db import models
from django import forms
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class UserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, 
        email, date_of_birth, is_maintainer=False, password=None):

        if not email:
            raise ValueError("Oops! Looks like you didn't write in your email")
        
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth
        )

        user.is_admin = False
        user.set_password(password)
        user.save(using=self._db)

        return User
    
    def create_superuser(self, username, first_name, last_name, 
        email, date_of_birth, password=None):

        if not email:
            raise ValueError("Oops! Looks like you didn't write in your email")
        
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth
        )

  
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)

        return User


class User(AbstractBaseUser):
    is_maintainer = models.BooleanField(
        verbose_name='Do you own/manage a restaurant?',
        default='False'
    )

    username = models.CharField(
        max_length=100,
        unique=True,
    )

    email = models.EmailField(
        verbose_name='Email Address',
        max_length=255,
        unique=True,
    )

    first_name = models.CharField(
        verbose_name='First Name',
        max_length=255,
    )

    last_name = models.CharField(
        verbose_name='Last Name',
        max_length=255,
    )

    date_of_birth = models.DateField(
        verbose_name='Date of Birth',
    )

    is_maintainer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'date_of_birth']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        return self.is_admin

