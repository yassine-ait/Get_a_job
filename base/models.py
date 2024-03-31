from django.contrib.auth.models import User
from django.db import models

from django.db.models.base import Model


# Create your models here.
class Postule(models.Model):
    nom = models.CharField(max_length=200, null=True, blank=True)
    prenom = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    motivation = models.TextField(null=True, blank=True)
    cvfile = models.FileField(null=True, blank=True)
    idoffre = models.CharField(max_length=200, null=True, blank=True)
    namecampany = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nom


class Recruter(models.Model):
    nom = models.CharField(max_length=200, null=True, blank=True)
    prenom = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    password = models.CharField(max_length=200, null=True, blank=True)
    civilite = models.CharField(max_length=200, null=True, blank=True)
    telephone = models.CharField(max_length=200, null=True, blank=True)
    namecampany = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nom


class Offre(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    namecampany = models.CharField(max_length=200, null=True, blank=True)
    region = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    timetype = models.CharField(max_length=200, null=True, blank=True)
    experience = models.CharField(max_length=200, null=True, blank=True)
    diplome = models.CharField(max_length=200, null=True, blank=True)
    salaire = models.CharField(max_length=200, null=True, blank=True)
    contrat = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
