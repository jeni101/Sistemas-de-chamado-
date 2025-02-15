contador_id = 1
chamados = {
    id: {'descricao': 'proplemas de email', 'prioridade': 'media', 'status': 'aberto', 'area': 'suport' },
    id: {'descricao': 'solicitacao de aumento', 'prioridade': 'alta', 'status': 'fechado', 'area': 'financeiro' }
       }
def cadastro():
    global contador_id 
    inicializacao = input('deseja iniciar um chamado? (s/n)')
    if inicializacao =='s':
        contador_id+=1
        descricao = input('poderia descrever a situação para o requerimento do chamado: ')
        prioridade = input('qual a prioridade? (alta, media ou baixa)')
        area = input('qual a area do chamado? (TI, RH, etc...)')
        chamados[contador_id] = {"descricao": descricao, "prioridade": prioridade, "status": "aberto", "area": area}
        print(f'chamado {contador_id} efetuado com sucesso')
        
    else:
        print('chamado cancelado')
cadastro()

        
    #estrutura inicial da logica:
    
    #comecar perguntando a prioridade/area dps a descricao.   feito.
     
    #e ja armazenar a informacao em um sistema de id p facilitar.  feito.
     
    # fez isso ja foi 50% dps so fazer um sistema basico de busca por id ou descricao.
     
    # descricao pelo oq? palavras chaves? como suport/ financeiro/ outros ou outra maneira?
    #remover chamados finalizados, como vai ser o salvamento? txt/json ou algo mais simples? 

    #pode ser uma lista q armazene o valor id junto com a descricao, lista? seria melhor um dicionario ett
    # pois assim q criar o valor prioridade dentro do dicionario ja entra com a lista com o id e a descricao.  em desenvolvimento.
    
    #chamados em ordem de prioridade: listar dependendo da area q o usuario escolheu ou perguntar ao usuario o nivel de urgencia
    #considerando que a maioria seria listada como urgente pois todos querem ser atentidos na hora, ou 
    # dentro de cada subarea colocar uma urgencia pre estabelecida? desse jeito ainda seria eficiente?
    
    #exibir estatisticas: numero de chamados abertos, finalizados e em andamento. Chamados por área (quantos chamados estão em TI, RH, etc.).

    # reverter e limpar lista de chamados: acho q é literalmene so inverter na fila e remover certos chamados
    #inadequados ou finalizados
     
    # se so colocar os dados dentro de um dicionario ele vai deletar tudo dps de fechado, me daria mais trabalho fazer um json 
    # ou pouparia esforco?
     