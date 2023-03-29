from django.db import models

from dispositivo.models import Dispositivo


class Leitura(models.Model):
    # dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    leitura = models.CharField(max_length=255, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id