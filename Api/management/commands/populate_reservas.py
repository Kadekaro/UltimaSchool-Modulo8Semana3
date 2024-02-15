from django.core.management.base import BaseCommand
from model_bakery import baker
from Reserva.models import Reserva


class Command(BaseCommand):
    help = 'Cria dados fakes para testar a API de agendamento'

    def handle(self, *args, **options):

        total = 50

        self.stdout.write(
            self.style.WARNING(f'Criando {total} agendamentos')
        )

        for i in range(total):
            reserva = baker.make(Reserva)
            reserva.save()

        self.stdout.write(
            self.style.SUCCESS('Agendamentos criados!')
        )
