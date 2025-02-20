from limpar_tela import *

contador_id = 0
chamados = {}

def cadastro():
    try:
        volta = False
        while volta == False:
            
            while True:
                global contador_id 
                inicializacao = input('Deseja iniciar um chamado? (s/n) ')
                
                if inicializacao.lower() =='s':
                    limpar_tela()
                    contador_id += 1
                    ser_humano = input('Informe seu nome e sobrenome para o inicio do chamado por gentileza: ')
                    if len(ser_humano) >36:
                        print('tente algo menor')
                        contador_id -=1
                        break
                    limpar_tela()
                    telefone = input('Informe seu telefoene de contato: ')
                    limpar_tela()
                    if len(telefone)>13:
                        print('numero de telefone muito grande tente outro.')
                        contador_id -=1
                        break
                    
                    descricao = input('Explique de forma resumida situação para o requerimento do chamado: ')
                    if len(descricao)>77:
                        print('A descrição esta muito longa, tente algo menor')
                        contador_id -=1
                        break
                    limpar_tela()
                    prioridade = input('Qual a prioridade? (Alta, Media ou Baixa) ')
                    limpar_tela()
                    if prioridade.lower() not in ['alta', 'media', 'baixa']:
                        print('Entrada invalida. Se atente as opções e tente novamente.')
                        contador_id -=1
                        break
                    area = input('Qual a area do chamado? (TI, RH, etc...)')
                    limpar_tela()
                    ver_tabela = input('Deseja ver o resultado do seu chamado antes de salvar? (s/n)')
                    
                    if ver_tabela.lower() =='s':
                        
                            
                        salvar = input(f"""
 ------------------------------------------------------------------------------
| NOME: {ser_humano:<37} | TELEFONE:  {telefone:<19} |    
|------------------------------------------------------------------------------|
| ID: {contador_id:<21} |PRIORIDADE:  {prioridade:<17} |ÁREA: {area:<12}|
|------------------------------------------------------------------------------|
|                                                                              |
| DESCRIÇÃO:                                                                   |
| {descricao:<77}| 
|                                                                              |
|                                                                              |
|______________________________________________________________________________| 

Deseja salvar essa versão:  
(s/n) """)
                    else:
                        chamados[contador_id] = {"nome": ser_humano, "telefone": telefone,"descricao": descricao, "prioridade": prioridade, "status": "Aberto", "area": area}
                        limpar_tela()
                        print(f'Chamado {contador_id} efetuado com sucesso')
                        continue
                    
                    if salvar.lower() =='s':    
                        chamados[contador_id] = {"nome": ser_humano, "telefone": telefone, "descricao": descricao, "prioridade": prioridade, "status": "Aberto", "area": area}
                        limpar_tela()
                        print(f'Chamado {contador_id} efetuado com sucesso')
                
                    elif salvar.lower() =='n':
                        contador_id -=1
                        limpar_tela()
                        print('Chamado cancelado')
                    
                    else:
                        print('Comando não encontrado')
                    
                elif inicializacao.lower() =='n':
                    print('Chamado cancelado')
                    volta = True
                    break
                    
                else:
                    limpar_tela()
                    print('Insira uma entrada valida. ')
                    input('Precione ENTER para continuar. ')
                
    except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            input("Pressione ENTER para continuar.")
            
            