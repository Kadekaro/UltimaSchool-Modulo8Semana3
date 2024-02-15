from django.urls import path
from Api.views import hello_world, AgendamentoModelViewSet, PetshopModelViewSet
from rest_framework.routers import SimpleRouter


app_name = 'api'

router = SimpleRouter(trailing_slash=False)  # O argumento trailing_slash Tira a barra "/" do final que é criada..
# … como padrão.

router.register('agendamento', AgendamentoModelViewSet)
router.register('petshop', PetshopModelViewSet)

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world_api'),
]

urlpatterns += router.urls
