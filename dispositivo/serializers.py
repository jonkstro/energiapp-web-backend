from rest_framework import serializers

from leitura.serializers import LeituraSerializer
from .models import Dispositivo


class DispositivoSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Dispositivo
        fields = ['id','mac', 'email']
