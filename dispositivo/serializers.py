from rest_framework import serializers

from leitura.serializers import LeituraSerializer
from .models import Dispositivo


class DispositivoSerializer(serializers.ModelSerializer):
    # ADICIONAR CAMPO leituras, POIS TERÁ VÁRIAS LEITURAS POR DISPOSITIVO
    leituras = LeituraSerializer(many=True)
    class Meta:
        model = Dispositivo
        fields = ['id','mac', 'email', 'leituras']