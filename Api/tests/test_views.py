import pytest
import datetime
from rest_framework import status
from rest_framework.test import APIClient
from model_bakery import baker
from Reserva.models import Petshop, Reserva


@pytest.fixture
def usuario():  # cria-se essa classe porque para criar um agendamento tem que estar autenticado como usuário
    return baker.make('auth.User')


@pytest.fixture
def dados_agendamento():
    hoje = datetime.date.today()
    petshop = baker.make(Petshop)
    return {
        'nome': 'nome teste', 'email': 'email@gmail.com',
        'nome_pet': 'pet teste', 'data': hoje, 'turno': 'manhã',
        'tamanho': 0, 'observacoes': '', 'petshop': petshop.pk,
    }


@pytest.fixture
def agendamento():
    return baker.make(Reserva)


@pytest.mark.django_db
def test_criar_agendamento(usuario, dados_agendamento):
    cliente = APIClient()
    cliente.force_authenticate(usuario)
    resposta = cliente.post('/api/agendamento', dados_agendamento)
    assert resposta.status_code == 201


@pytest.mark.django_db
def test_todos_agendamentos(agendamento):
    cliente = APIClient()
    resposta = cliente.get('/api/agendamento')
    assert len(resposta.data['results']) == 1


@pytest.mark.django_db
def test_todos_petshops():
    cliente = APIClient()
    resposta = cliente.get('/api/petshop')
    assert len(resposta.data['results']) == 0


@pytest.mark.django_db
def test_deletar_agendamento(usuario, agendamento):
    cliente = APIClient()
    cliente.force_authenticate(usuario)
    resposta = cliente.delete(f'/api/agendamento/{agendamento.id}')
    assert resposta.status_code == 204
