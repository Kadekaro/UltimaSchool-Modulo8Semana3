from django.urls import path
from Reserva.views import reserva

app_name = 'reserva'
urlpatterns = [
    path('', reserva, name='reserva')
]