from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from ..models import Empresa
from .serializers import CNPJSerializer, EnderecoSerializer
import requests

class cnpjViewSet(ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = CNPJSerializer
    
    def create(self, request):
        cnpj = request.data.get('cnpj') #passar no body com o nome cnpj, numeros sem . e - 
        site = f'https://receitaws.com.br/v1/cnpj/{cnpj}' #url da api de cnpj
        requisicao = requests.get(site)
        json = requisicao.json()
  
        cnpj = json.get('cnpj')
        nome = json.get('nome')
        nomeFantasia = json.get('fantasia')
        logradouro = json.get('logradouro')
        numero = json.get('numero')
        cep = json.get('cep')
        
        dados1= {
            "cnpj": cnpj,
            "nome": nome,
            "nomeFantasia": nomeFantasia 
        }
        
        
        serial = CNPJSerializer(data=dados1)
        if serial.is_valid(): 
            empresa = serial.save()
        else:
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

       
        dadosEndereco= {
            "cnpj": empresa.id,  
            "logradouro": logradouro,
            "numero": numero,
            "cep": cep 
        }
        
        serial2 = EnderecoSerializer(data=dadosEndereco)
        if serial2.is_valid(): 
            serial2.save()
        else:
            return Response(serial2.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serial.data, status=status.HTTP_201_CREATED)
