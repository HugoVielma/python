from django.db import models


class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()


class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()


class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)
    curso = models.ManyToManyField(Curso)


def __str__(self):
    return f'{self.nombre} {self.apellido}'


class Entregable(models.Model):
    nombres = models.CharField(max_length=40)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()
    link = models.CharField(max_length=256, null=True)
