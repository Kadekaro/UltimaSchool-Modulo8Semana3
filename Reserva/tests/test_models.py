from datetime import date

import pytest
from model_bakery import baker
from Reserva.models import Reserva, Petshop


@pytest.fixture
def reserva():
    data = date(2024, 1, 17)
    reserva = baker.make(
        Reserva,
        nome='Tom',
        data=data,
        turno='tarde'
    )
    return reserva


@pytest.mark.django_db
def test_str_reserva_deve_retornar_string_formatada(reserva):
    assert str(reserva) == 'Tom: 2024-01-17 - tarde'


@pytest.mark.django_db
def test_quantidade_reservas_deve_retornar_reservas():
    petshop = baker.make(Petshop)
    quantidade = 3
    baker.make(
        Reserva,
        quantidade,
        petshop=petshop
    )

    assert petshop.quantidade_reservas() == 3
