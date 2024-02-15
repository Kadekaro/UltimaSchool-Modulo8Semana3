from django.core.management import BaseCommand
from rest_framework.authtoken.admin import User
from rest_framework.authtoken.models import Token


class Command(BaseCommand):
    help = 'Cria um novo token para ser usado.'

    def add_arguments(self, parser):
        parser.add_argument('--username', required=True)
        parser.add_argument('--password', required=True)

    def handle(self, *args, **options):
        username = options['username']
        password = options['password']
        self.stdout.write(
            self.style.WARNING(f'Criando usuário com o nome {username}.')
        )
        user = User(username=username)
        user.first_name = username
        user.set_password(password)
        user.save()
        self.stdout.write(
            self.style.SUCCESS(f'Usuário criado!')
        )
        self.stdout.write(
            self.style.WARNING(f'Criando token para o usuário {username}!')
        )
        token = Token.objects.create(user=user)
        self.stdout.write(
            self.style.SUCCESS(f'Token criado para o usuário: {token.key}')
        )
