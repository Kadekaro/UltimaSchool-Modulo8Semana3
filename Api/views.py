from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from Api.serializers import AgendamentoModelSerializer, PetshopModelSerializer
from Reserva.models import Reserva, Petshop


class PetshopModelViewSet(ReadOnlyModelViewSet):
    queryset = Petshop.objects.all()
    serializer_class = PetshopModelSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class AgendamentoModelViewSet(ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = AgendamentoModelSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated] # Essa opção impede que qualquer um que não esteja autenticado possa ver...
    # ... Ou consultar os dados.
    permission_classes = [IsAuthenticatedOrReadOnly]  # Já essa opção impede que os usuários que não forem...

    # ...autenticados possam editar o agendamento ou criar um, mas qualquer um poderá consultar a agenda.


@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({'message': f'Hello, {request.data.get("name")}'})
    return Response({'hello': 'World API'})
