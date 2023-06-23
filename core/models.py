from django.db import models

# Create your models here.
class Region(models.Model):
    idregion = models.AutoField(primary_key=True)
    descripcion= models.CharField(max_length=50)
    estado = models.IntegerField()

    def __str__(self):
        return self.descripcion

class Tipo(models.Model):
    idtipo = models.AutoField(primary_key=True)
    nombreTipo = models.CharField(max_length=50)
    estado = models.IntegerField()

    def __str__(self):
        return self.nombreTipo
    




class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    F_nac = models.DateField()
    telefono = models.IntegerField(max_length=9)
    correo = models.EmailField()
    #contrasena = models.#
    rut = models.CharField(max_length=9)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=500)
    cod_postal = models.CharField()
    comentario = models.CharField(max_length=100)



class

class Marca(models.Model):
    idmarca = models.AutoField(primary_key=True)
    descripcion= models.CharField(max_length=50)
    estado = models.IntegerField()

    def __str__(self):
        return self.descripcion

class Celular(models.Model):
    idcelu = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length=300)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    file = models.ImageField(upload_to="img/")
    precio = models.FloatField()
    stock = models.IntegerField()
    comentario = models.CharField(max_length=100)
    
    def __str__(self):
        return self.modelo
