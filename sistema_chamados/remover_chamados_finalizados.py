from cadastro_chamados import * 
from reverter_limpar_chamados import *
import time
def mudar_status():
    
    instrucoes_mudar_status()
    
    while True:
        
        id_input = input("\n ")
        
        if id_input.lower() == 'i':
            limpar_tela()
            reverter()
            instrucoes_mudar_status()
            
            
        if id_input.lower() == 'x':
            decisao =input('Antes de sair gostaria de remover os chamados ja finalizados? (s/n)')
            if decisao.lower() =='s':
                limpar_tela()
                remover()
                break
            elif decisao.lower() =='n': 
                limpar_tela()
                break
        
        
        if id_input.isdigit():
            id = int(id_input)
            
            
            if id in chamados:
                chamados[id]['status'] = 'Fechado'
                print(f"\nStatus do chamado {id} foi alterado para 'Fechado'.")
                time.sleep(2)
                
            else:
                print(f"Chamado com ID {id} não encontrado.")
        elif id_input.lower() =='i':
            continue
        else:
            print("Entrada inválida. Por favor, insira um ID válido ou 'X' para sair.")
            
    
    

def remover():
    
    for id_chamado, chamado in list(chamados.items()):
        
        if chamado['status'].lower() == 'fechado':
            del chamados[id_chamado]
            print(f"Chamado {id_chamado} removido.")
       
        
        
def instrucoes_mudar_status():
     print("""\n 
    OPÇÕES:
              
    - Marque o id dejado para mudar o status de aberto para fechado um de cada vez.
    - Caso necessario precione 'I + ENTER' para inverter a ordem de lista e facilitar a visulização.
    - Pressione 'X' para sair.  """)