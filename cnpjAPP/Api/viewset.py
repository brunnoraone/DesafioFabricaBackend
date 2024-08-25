from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from ..models import Empresa
from .serializers import CNPJSerializer
import requests




class cnpjViewSet(ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = CNPJSerializer
    
    def create(self, request):
        cnpj = request.data.get('cnpj')
        site = (f'https://receitaws.com.br/v1/cnpj/{cnpj}')
        requisicao = requests.get(site)
        json = requisicao.json()
        
        cnpjsalvo = [] 

        cnpj = json.get('cnpj')
        nome = json.get('nome')
        nomeFantasia = json.get('fantasia')

        dados= {
            "cnpj": f"{cnpj}",
            "nome": f"{nome}",
            "nomeFantasia": f"{nomeFantasia}" 
            }
        
        serial = CNPJSerializer(data=dados)
        if serial.is_valid(): 
            serial.save()
            serial.append(serial.data)
        else:
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
            
        return Response(serial.data, status=status.HTTP_201_CREATED)  