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
        id = self.request.query_params.get('id', None)
        mac = self.request.query_params.get('mac', None)
        queryset = Dispositivo.objects.filter(user=user)

        # REALIZAR CONSULTAR NA URL: http://127.0.0.1:8000/dispositivos/?mac=teste 
        # SE ENVIAR O IR NA URL:
        if id:
            queryset = Dispositivo.objects.filter(pk=id)
        # SE ENVIAR O MAC NA URL:
        if mac:
            queryset = Dispositivo.objects.filter(mac__iexact=mac)

        return queryset
