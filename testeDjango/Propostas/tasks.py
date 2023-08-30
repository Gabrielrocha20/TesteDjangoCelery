
import json
from time import sleep

import requests
from celery import shared_task


@shared_task
def verificar_proposta(data=None, proposta_id=None):
    from .models import CampoProposta, Proposta, ValorCampo
    if data == None:
        return
    url = "https://loan-processor.digitalsys.com.br/api/v1/loan/"
    
    new_json = {
            "name": f"{data['nome']}",
        }
    for item in data['campos_valores']:
        campo_proposta = CampoProposta.objects.filter(id=item["campo"]).first()
        campo_valor = item.get('texto')
        item_data = {f"{campo_proposta.nome} pergunta": f"{campo_valor}"}

        new_json.update(item_data)
    new_json = json.dumps(new_json)
    response = requests.post(url, json=data)
    print(new_json)
    print(response.json())
    if not response.json().get("approved"):
        print('Deletando')
        deleteData(proposta_id)
    



def deleteData(proposta_id):
    from .models import CampoProposta, Proposta, ValorCampo
    proposta = Proposta.objects.get(id=proposta_id)
    proposta.delete()
    print(proposta, "deletado")

    
        