from cadastro_chamados import * 
from reverter_limpar_chamados import *
def mudar_status():
    
    while True:
        
        print("\nMarque o id que deseja mudar de status de aberto para fechado. (um de cada vez ou pressione 'X' para sair): ")
        id_input = input("\n Você pode inverter a lista para melhor visualizacao precionando 'I' caso n queira so selecione o ID desejado ou 'X' para sair.")
        if id_input.lower() == 'i':
            limpar_tela()
            reverter()
        if id_input.lower() == 'x':
            decisao =input('Antes de sair gostaria de remover os chamados ja finalizados? (s/n)')
            if decisao.lower() =='s':
                remover()
                
            elif decisao.lower() =='n': 
                limpar_tela()
                break
        
        
        if id_input.isdigit():
            id = int(id_input)
            
            
            if id in chamados:
                chamados[id]['status'] = 'Fechado'
                print(f"\nStatus do chamado {id} foi alterado para 'Fechado'.")
                
            else:
                print(f"Chamado com ID {id} não encontrado.")
        else:
            print("Entrada inválida. Por favor, insira um ID válido ou 'X' para sair.")
            
    
    

def remover():
    
    for id_chamado, chamado in list(chamados.items()):
        
        if chamado['status'].lower() == 'fechado':
            del chamados[id_chamado]
            print(f"Chamado {id_chamado} removido.")
            break
