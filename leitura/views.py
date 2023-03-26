from rest_framework import viewsets
from rest_framework import permissions, authentication

from .models import Leitura
from .serializers import LeituraSerializer


class LeituraViewSet(viewsets.ModelViewSet):
    serializer_class = LeituraSerializer

    # CONFIGURAR PARA SÓ EXIBIR SE ESTIVER AUTENTICADO COM TOKEN
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [
            authentication.TokenAuthentication, 
            authentication.SessionAuthentication
        ]
    def get_queryset(self):
        return Leitura.objects.all()