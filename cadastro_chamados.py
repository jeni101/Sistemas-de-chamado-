contador_id = 1
chamados = {
    
    1: {'descricao': 'problema de email', 'prioridade': 'media', 'status': 'aberto', 'area': 'suport' },
    2: {'descricao': 'solicitacao de aumento', 'prioridade': 'alta', 'status': 'fechado', 'area': 'financeiro' },
    3: {"descricao": "problema na impressora", "prioridade": "baixa", "status": "fechado", "area": "TI"},
    4: {"descricao": "problema na impressora", "prioridade": "alta", "status": "fechado", "area": "TI"},
    5: {'descricao': 'problema de convivio', 'prioridade': 'alta', 'status': 'aberto', 'area': 'RH' }
       }

def cadastro():
    global contador_id 
    inicializacao = input('deseja iniciar um chamado? (s/n)')
    
    if inicializacao =='s':
        contador_id += 1
        descricao = input('poderia descrever a situação para o requerimento do chamado: ')
        prioridade = input('qual a prioridade? (alta, media ou baixa)')
        area = input('qual a area do chamado? (TI, RH, etc...)')
        chamados[contador_id] = {"descricao": descricao, "prioridade": prioridade, "status": "aberto", "area": area}
        
        print(f'chamado {contador_id} efetuado com sucesso')
        
    else:
        print('chamado cancelado')
