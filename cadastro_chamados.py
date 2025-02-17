from limpar_tela import *

contador_id = 0
chamados = {
    
    1: {'descricao': 'problema de email', 'prioridade': 'media', 'status': 'aberto', 'area': 'suport' },
    2: {'descricao': 'solicitacao de aumento', 'prioridade': 'alta', 'status': 'fechado', 'area': 'financeiro' },
    3: {"descricao": "problema na impressora", "prioridade": "baixa", "status": "fechado", "area": "TI"},
    4: {"descricao": "problema na impressora", "prioridade": "alta", "status": "fechado", "area": "TI"},
    5: {'descricao': 'problema de convivio', 'prioridade': 'alta', 'status': 'aberto', 'area': 'RH' }
       }

def cadastro():
    try:
        volta = False
        while volta == False:
            
            while True:
                global contador_id 
                inicializacao = input('deseja iniciar um chamado? (s/n)')
                
                if inicializacao =='s':
                    limpar_tela()
                    contador_id += 1
                    descricao = input('poderia descrever a situação para o requerimento do chamado: ')
                    prioridade = input('qual a prioridade? (alta, media ou baixa)')
                    if prioridade.lower() not in ['alta', 'media', 'baixa']:
                        print('entrada invalida. Se atente as opções e tente novamente.')
                        break
                    area = input('qual a area do chamado? (TI, RH, etc...)')
                    chamados[contador_id] = {"descricao": descricao, "prioridade": prioridade, "status": "Aberto", "area": area}
                    limpar_tela()
                    print(f'chamado {contador_id} efetuado com sucesso')
                
                elif inicializacao.lower() =='n':
                    print('chamado cancelado')
                    volta = True
                    break
                    
                else:
                    limpar_tela()
                    print('Insira uma entrada valida. ')
                    input('Precione ENTER para continuar. ')
                
    except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            input("Pressione ENTER para continuar.")