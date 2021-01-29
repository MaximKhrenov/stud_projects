from django.db import models
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=200, verbose_name='ФИО')
    sex = models.CharField(max_length=200, verbose_name='Пол')
    dateOfBirth = models.DateField()
    adress = models.CharField(max_length=500, verbose_name='Адрес')
    doctors = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Врач')

    def __str__(self):
        return self.name

class CardPatient(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="Пациент")
    dateOfVizit = models.DateField(verbose_name="Дата визита")
    placeVizit = models.CharField(max_length=500, verbose_name='Место визита')
    descVizit = models.TextField(verbose_name="Описание и назначения")
    def __str__(self):
        return self.placeVizit

