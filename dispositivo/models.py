from django.db import models
from django.contrib.auth.models import User


class Dispositivo(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    mac = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    rua = models.CharField(max_length=50, null=False, blank=False)
    bairro = models.CharField(max_length=50, null=False, blank=False)
    cidade = models.CharField(max_length=50, null=False, blank=False)
    estado = models.CharField(max_length=50, null=False, blank=False)
    latitude = models.DecimalField(max_digits=8, decimal_places=3)
    longitude = models.DecimalField(max_digits=8, decimal_places=3)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.mac