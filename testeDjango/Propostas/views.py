import json

from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import View
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CampoProposta, Proposta, ValorCampo
from .serializer import (CampoPropostaSerializer, PropostaRegisterSerializer,
                         PropostaSerializer)
from .tasks import verificar_proposta


class PropostaApiList(generics.ListAPIView):
    queryset = Proposta.objects.all()
    serializer_class = PropostaSerializer

class PropostaUserApiList(generics.ListAPIView):
    serializer_class = PropostaSerializer
    def get_queryset(self):
        proposta_id = self.kwargs['id']
        queryset = Proposta.objects.filter(id=proposta_id)
        return queryset

class PropostaApiRegister(generics.ListCreateAPIView):
    queryset = Proposta.objects.all()
    serializer_class = PropostaRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            proposta_obj = serializer.save()
            
            proposta_id = proposta_obj.id
            response_task = verificar_proposta(data=request.data, proposta_id=proposta_id)

            return Response({"message": "true"}, status=202)

        return Response(serializer.errors, status=400)
    
class CampoPropostaApiList(generics.ListAPIView):
    queryset = CampoProposta.objects.all()
    serializer_class = CampoPropostaSerializer



class PropostaDeleteAPI(generics.DestroyAPIView):
    queryset = Proposta.objects.all()
    serializer_class = PropostaSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        
        return Response({"message": "Proposta foi deletada com sucesso."})
