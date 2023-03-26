from rest_framework import serializers

from leitura.models import Leitura

class LeituraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leitura
        fields = ['leitura','created',]