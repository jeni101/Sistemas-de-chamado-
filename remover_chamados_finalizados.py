from cadastro_chamados import * 
def mudar_status():
    
    while True:
        id_input = input("\nMarque o id que deseja mudar de status. (um de cada vez ou pressione 'X' para sair): ")
        
        if id_input.lower() == 'x':
            decisao =input('Antes de sair gostaria de remover os chamados ja finalizados? (s/n)')
            if decisao.lower() =='s':
                remover()
                
            elif decisao.lower() =='n':
                break
        
        
        if id_input.isdigit():
            id = int(id_input)
            
            
            if id in chamados:
                chamados[id]['status'] = 'Fechado'
                print(f"Status do chamado {id} foi alterado para 'Fechado'.")
                
            else:
                print(f"Chamado com ID {id} não encontrado.")
        else:
            print("Entrada inválida. Por favor, insira um ID válido ou 'X' para sair.")


def remover():
    
    for id_chamado, chamado in list(chamados.items()):
        
        if chamado['status'].lower() == 'fechado':
            del chamados[id_chamado]
            print(f"Chamado {id_chamado} removido.")
