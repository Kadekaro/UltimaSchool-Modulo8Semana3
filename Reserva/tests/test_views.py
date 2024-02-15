from datetime import date, timedelta

import pytest
from pytest_django.asserts import assertTemplateUsed

from Reserva.models import Reserva


def test_reserva_view_deve_retornar_template(client):
    response = client.get('/reserva/')

    assert response.status_code == 200
    assertTemplateUsed(response, 'reserva.html')


@pytest.fixture
def dados_validos():
    amanha = date.today() + timedelta(days=1)
    dados = {
        'nome': 'joão',
        'email': 'joao@email.com',
        'nome_pet': 'Tom',
        'data': amanha,
        'turno': 'tarde',
        'tamanho': 0,
        'observacoes': 'O Tom está bem fedorento',
    }
    return dados


@pytest.mark.django_db
def test_reserva_view_deve_retornar_sucesso(client, dados_validos):
    response = client.post('/reserva/', dados_validos)

    assert response.status_code == 200
    assert 'Reserva concluída com sucesso!' in response.content.decode('utf-8')


@pytest.mark.django_db
def test_reserva_view_deve_criar_reserva(client, dados_validos):
    response = client.post('/reserva/', dados_validos)

    assert Reserva.objects.all().count() == 1
    reserva = Reserva.objects.first()

    assert reserva.nome == dados_validos['nome']
    assert reserva.nome_pet == dados_validos['nome_pet']
    assert response.status_code == '201'

