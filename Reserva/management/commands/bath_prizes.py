from random import sample
from Reserva.models import Petshop
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    @staticmethod
    def list_petshops():
        return Petshop.objects.all().values_list('pk', flat=True)

    def add_arguments(self, parser):
        parser.add_argument(
            'quantity',
            nargs='?',
            default=5,
            type=int,
            help='Quantas pessoas devem participar do sorteio!'
        )
        parser.add_argument(
            '-petshop',
            required=True,
            type=int,
            choices=self.list_petshops(),
            help='IDs do Petshop para realizar o sorteio!'
        )

    @staticmethod
    def escolher_reservas(banhos, quantidade):
        banhos_list = list(banhos)
        if quantidade > len(banhos_list):
            quantidade = len(banhos_list)

        return sample(banhos_list, quantidade)

    def imprimir_info_petshop(self, petshop):
        self.stdout.write(
            self.style.HTTP_INFO(
                'Dados do petshop que realizou o sorteio:'
            )
        )
        self.stdout.write(f'Nome do Petshop: {petshop.nome}\n'
                          f'Endereço: {petshop.rua}, {petshop.numero} - {petshop.bairro}'
                          )

    def imprimir_reservas_sorteadas(self, reservas):
        self.stdout.write()
        self.stdout.write(
            self.style.HTTP_INFO(
                'Dados das pessoas e animais sorteados:'
            )
        )
        self.stdout.write(
            self.style.HTTP_INFO(
                '=' * 100
            )
        )
        for reserva in reservas:
            self.stdout.write(
                f'Animal: {reserva.nome_pet}\n'
                f'Tutor: {reserva.nome} - {reserva.email}'
            )
            self.stdout.write(
                self.style.HTTP_INFO(
                    '=' * 100
                )
            )

    def handle(self, *args, **options):
        quantity = options['quantity']
        petshop_id = options['petshop']

        petshop = Petshop.objects.get(pk=petshop_id)
        reservas = petshop.reservas.all()

        banhos_escolhidos = self.escolher_reservas(reservas, quantity)

        self.stdout.write(
            self.style.SUCCESS('Sorteio concluído.')
        )

        self.imprimir_info_petshop(petshop)
        self.imprimir_reservas_sorteadas(banhos_escolhidos)
