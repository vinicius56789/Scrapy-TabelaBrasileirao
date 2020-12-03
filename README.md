# TREINANDO SCRAPY :robot:

Buscando dados de classificação do campeonato brasileiro de futebol do site CBF, tratando o html e pegando o primeiro lugar.

### ARQUIVOS

1. main.py
2. usandoJson.py

##### main.py

> Neste arquivo é feito a busca, leitura e tratamento do HTML. Assim, ficam só os dados e partir dali é feito um dicionário Python e criado um arquivo json com os dados.

##### usandoJson.py

> Faz o serviço contrário do arquivo main. Faz a leitura de um arquivo Json, passa para uma variável e partir dela é possível solicitar informações como -> data ["times"] [0] ["pos"] ou data ["times"] [0] ["pontos"]. Nesses casos, são solicitados nome e pontuação do primeiro colocado.

:wolf: