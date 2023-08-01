from django.db import models

# Create your models here.
class fonoaudiologo(models.Model):
    nombre = models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()
    profesion= models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nombre}, {self.apellido},   email:{self.email}"

class pediatra(models.Model):
    nombre = models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()
    profesion= models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nombre}, {self.apellido},   email:{self.email}"
    
class medico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()
    profesion= models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nombre}, {self.apellido},   email:{self.email}"
    
class odontologo(models.Model):
    nombre = models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()
    profesion= models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nombre}, {self.apellido},   email:{self.email}"
    
class Nuevoprofesional(models.Model):
    nombre = models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()
    profesion= models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nombre}, {self.apellido},   email:{self.email}, {self.profesion}"