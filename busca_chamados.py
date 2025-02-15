from cadastro_chamados import *
from limpar_tela import *

def busca():
    while True:
        print("""
            ________________________
            | metodo de procura      |
            |________________________|
            |lista de ID...........|1|
            |buscar diretamente....|2|
            |________________________|
            """)
        metodo = input('Como deseja realizar a busca? ')
        if metodo == "1":
            limpar_tela()
            
            print("Chamados disponíveis:")
            for id_chamado in chamados:
                
                print(f"ID: {id_chamado}, Descrição: {chamados[id_chamado]['descricao']}, "
                      f"Prioridade: {chamados[id_chamado]['prioridade']}, "
                      f"Status: {chamados[id_chamado]['status']}, "
                      f"Área: {chamados[id_chamado]['area']}")
        
        elif metodo == '2':
            id = int(input('Digite o id: '))
            if id in chamados:
                print(f'o id encontrado foi: {chamados[id]}')
            else:
                print('deu erro ai man')