from django.db import models

from dispositivo.models import Dispositivo


class Leitura(models.Model):
    mac = models.CharField(max_length=255, null=False, blank=False)
    leitura = models.CharField(max_length=255, null=False, blank=False)
    dateCreated = models.DateField(auto_now_add=True, null=False, blank=False)
    timeCreated = models.TimeField(auto_now_add=True, null=False, blank=False)
    def __str__(self):
        return self.id