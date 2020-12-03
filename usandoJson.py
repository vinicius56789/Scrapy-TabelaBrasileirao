import json

def readJson():
    with open('tabela.json', 'r', encoding='utf8') as json_file:
        return json.load(json_file)


data = readJson()
print('Primeiro colocado:')
print(data['times'][0]['pos'])
print(data['times'][0]['pontos'])
print('Atualizado hoje.')