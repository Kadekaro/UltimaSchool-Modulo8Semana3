import datetime

from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedRelatedField,
    PrimaryKeyRelatedField,
    ValidationError
)

from Reserva.models import Reserva, Petshop


class PetShopRelatedFieldCustomSerializer(PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.serializer = PetshopNestedModelSerializer
        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False

    def to_representation(self, value):
        return self.serializer(value, context=self.context).data


class PetshopModelSerializer(ModelSerializer):
    reservas = HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='api:reserva-detail'
    )

    class Meta:
        model = Petshop
        fields = '__all__'


class PetshopNestedModelSerializer(ModelSerializer):
    class Meta:
        model = Petshop
        fields = '__all__'


class AgendamentoModelSerializer(ModelSerializer):
    petshop = PetShopRelatedFieldCustomSerializer(
        queryset=Petshop.objects.all(),
        read_only=False
    )

    @staticmethod
    def validate_data(value):
        hoje = datetime.date.today()
        if value < hoje:
            raise ValidationError('Não é possível realizar um agendamento para o passado!')
        return value

    class Meta:
        model = Reserva
        fields = '__all__'
