from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=10)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    fecha_inicio = models.DateField()
    cantidad_pedida = models.IntegerField()
    MESES_CHOICES = [
        ('3', 3),
        ('6', 6),
        ('9', 9)
    ]
    plazo = models.CharField(max_length=1, choices=MESES_CHOICES, default='3')
    total = models.DecimalField(max_digits=5, decimal_places=2,default=0.0)

    def __str__(self):
        return self.nombre

    def interes(self):
        return self.cantidad_pedida * 0.02
    
    def calcular_total(self):
        self.total = (self.cantidad_pedida + self.interes()) * self.plazo 
    
    def get_absolute_url(self):
        return "list"
    
