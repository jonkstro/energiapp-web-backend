from rest_framework import viewsets
from rest_framework import permissions, authentication

from .models import Dispositivo
from .serializers import DispositivoSerializer


class DispositivoViewSet(viewsets.ModelViewSet):
    serializer_class = DispositivoSerializer

    # CONFIGURAR PARA SÓ EXIBIR SE ESTIVER AUTENTICADO COM TOKEN
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [
            authentication.TokenAuthentication, 
            authentication.SessionAuthentication
        ]
    # SERÁ MOSTRADO SOMENTE AS LISTAS DO USUÁRIO QUE TIVER LOGADO
    def get_queryset(self):
        user = self.request.user
        return Dispositivo.objects.filter(user=user)