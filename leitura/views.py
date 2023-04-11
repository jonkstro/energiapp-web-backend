from rest_framework import viewsets
from rest_framework import permissions, authentication

from .models import Leitura
from .serializers import LeituraSerializer


class LeituraViewSet(viewsets.ModelViewSet):
    serializer_class = LeituraSerializer

    # CONFIGURAR PARA SÓ EXIBIR SE ESTIVER AUTENTICADO COM TOKEN
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [
    #         authentication.TokenAuthentication, 
    #         authentication.SessionAuthentication
    #     ]
    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        mac = self.request.query_params.get('mac', None)
        date_start = self.request.query_params.get('date-start', None)
        date_end = self.request.query_params.get('date-end', None)
        created = self.request.query_params.get('created', None)
        queryset = Leitura.objects.all()
        # REALIZAR CONSULTAR NA URL: http://127.0.0.1:8000/leituras/?mac=teste 
        # SE ENVIAR O ID NA URL:
        if id:
            queryset = Leitura.objects.filter(pk=id)
        # SE ENVIAR O MAC NA URL:
        if mac:
            queryset = Leitura.objects.filter(mac__iexact=mac)
        # RANGE DE DATAS NO FORMATO: '2016-01-01T00:00:00+03:00'
        # EXEMPLO DE CONSULTA NA URL: http://127.0.0.1:8000/leituras/?created=1&date-start=2023-04-01&date-end=2023-05-01

            queryset = Leitura.objects.filter(dateCreated__range=[date_start, date_end]).order_by('dateCreated')
        
        # NO FINAL DO PROJETO IREMOS QUERER BUSCAR AS LEITURAS POR MAC / DATA INICIAL / DATA FINAL
        # PARA ISSO, USAREMOS A QUERY ABAIXO: 
        # http://127.0.0.1:8000/leituras/?mac=teste:mac:1&created=1&date-start=2023-04-01&date-end=2023-05-01
        
        return queryset
    
    # CRIAR UMA CONDIÇÃO DE QUE PARA QUE SEJA CRIADO UMA NOVA LEITURA, SEJA PRECISO REALIZAR O ENVIO DE UM HEADER
    # INFORMANDO QUE SE TRATA DE UM DISPOSITIVO
    def perform_create(self, serializer):
        if self.request.headers.get('Disp'):
            serializer.save()
        
