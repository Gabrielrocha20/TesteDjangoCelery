import json as js

json = {"nome": "Gabriel Rocha Teste",
        "campos_valores": 
        [
            {"campo": "Sobre", "valor_text": "imagen000 teste de celery"},
            {"campo": "Sobre", "valor_text": "d teste de celery"},
            {"campo": "Sobre", "valor_text": "imagen0a00 teste de celery"},
            {"campo": "Sobre", "valor_text": "imagen0av00 teste de celery"},
            {"campo": "Sobre", "valor_text": "imagen0010 teste de celery"},
        ]}
new_json = {
                "nome": f"{json['nome']}",
            }

for item in json["campos_valores"]:
    campo_valor = item.get("valor_texto")
    item_data = {item['campo']: item['valor_text']}

    new_json.update(item_data)
new_json = js.dumps(new_json)
print(new_json)

