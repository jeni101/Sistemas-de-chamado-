from cadastro_chamados import *
from limpar_tela import *

def busca():
    while True:
        
        print("""
            _____________________________
            |     MEDOTO DE BUSCA       |
            |___________________________|
            |ver lista de ID..........|1|
            |buscar ID diretamente....|2|
            |buscar por descrição.....|3|
            |___________________________|
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
        
        
        elif metodo == '3':
            verificacao = input('Digite a descrição do chamado: (máximo 40 caracteres) ')
            
            if len(verificacao) > 40:
                print('Tente algo menor.')
            
            else:
                palavras_usuario = verificacao.lower().split()  

                
                lista_prioridade_alto_e_medio = []
                lista_prioridade_baixa = []

                for id_chamado, chamado in chamados.items():
                    descricao_existente = chamado['descricao'].lower()  

                    
                    if all(palavra in descricao_existente for palavra in palavras_usuario):
                        
                        if chamado['prioridade'] == 'alta':
                            lista_prioridade_alto_e_medio.insert(0, id_chamado)
                        
                        elif chamado['prioridade'] == 'media':
                            lista_prioridade_alto_e_medio.insert(-1, id_chamado)
                        
                        else:
                            lista_prioridade_baixa.append(id_chamado)

                
                lista_final = lista_prioridade_alto_e_medio + lista_prioridade_baixa

                if lista_final:
                    print("\nChamados encontrados:")
                    
                    for id_chamado in lista_final:
                        chamado = chamados[id_chamado]
                        print(f"ID: {id_chamado}, Descrição: {chamado['descricao']}, "
                              f"Prioridade: {chamado['prioridade']}, Status: {chamado['status']}, "
                              f"Área: {chamado['area']}")
                else:
                    print("Nenhum chamado encontrado para a descrição informada.")
                