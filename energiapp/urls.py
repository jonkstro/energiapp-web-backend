from django.urls import include, path
from rest_framework import routers
from django.contrib import admin

from dispositivo.views import DispositivoViewSet
from leitura.views import LeituraViewSet
from energiapp.views import UserActivationView

router = routers.DefaultRouter()
# SEMPRE APÓS DEFINIR UM get_queryset TEMOS QUE DIZER SEU BASENAME
router.register(r'dispositivos', DispositivoViewSet, basename='Dispositivo')
router.register(r'leituras', LeituraViewSet, basename='Leitura')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls.authtoken')),
    # path('auth/', include('djoser.social.urls')),
    path('activate/<str:uid>/<str:token>/', UserActivationView.as_view()),
]