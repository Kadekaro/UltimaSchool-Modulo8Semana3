# Generated by Django 4.2.8 on 2024-01-11 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Reserva",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=50, verbose_name="Nome:")),
                ("email", models.EmailField(max_length=75, verbose_name="Email:")),
                (
                    "nome_pet",
                    models.CharField(max_length=50, verbose_name="Nome do Pet:"),
                ),
                (
                    "data",
                    models.DateField(help_text="dd/mm/aaaa", verbose_name="Data:"),
                ),
                (
                    "turno",
                    models.CharField(
                        choices=[("manhã", "Manhã"), ("tarde", "Tarde")],
                        max_length=10,
                        verbose_name="Turno:",
                    ),
                ),
                (
                    "tamanho",
                    models.IntegerField(
                        choices=[(0, "Pequeno"), (1, "Médio"), (2, "Grande")],
                        verbose_name="Tamanho:",
                    ),
                ),
                ("observacoes", models.TextField(blank=True, verbose_name="Mensagem:")),
            ],
            options={
                "verbose_name": "Reserva de Banho",
                "verbose_name_plural": "Reservas de Banho",
            },
        ),
    ]
