from rest_framework.serializers import ModelSerializer
from ..models import Empresa, Endereco


class CNPJSerializer(ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'        