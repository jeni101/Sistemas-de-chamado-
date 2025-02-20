from cadastro_chamados import *
from limpar_tela import *
from remover_chamados_finalizados import *

def busca():
    while True:
        
        print("""
             ___________________________
            |       MENU DE BUSCA       |
            |___________________________|
            |Ver lista de ID..........|1|
            |Buscar ID diretamente....|2|
            |Buscar por descrição.....|3|
            |Mudar status.............|4|
            |                           |
            |MENU PRINCIPAL...........|x|
            |___________________________|
            """)
        
        metodo = input('Como deseja realizar a busca? ')
        
        
        if metodo == "1":
            limpar_tela()
            
            ordem_prioridade()
        
        elif metodo == '2':
            while True:
                try:
                    limpar_tela()
                    id = int(input('Digite o id: '))
                    
                    if id in chamados:
                        print(f'\nO id encontrado foi: {chamados[id]}')
                        decisao = input("\nPara continuar procurando um ID especifico aperte uma tecla qualquer, para sair e voltar p o menu de busca aperte 'x'. ")
                        if decisao.lower() =='x':
                            limpar_tela()
                            break
                        else:
                            limpar_tela()
                            continue
                    else:
                        print('Esse id não existe tente outro.')
                        input('Precione ENTER para voltar.')
                        limpar_tela()
                except Exception as e:
                    print(f"Ocorreu um erro inesperado: {e}")
                    input("Pressione ENTER para continuar.") 
        
        elif metodo == '3':
            limpar_tela()
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
                    limpar_tela()
                    print("\nChamados encontrados por ordem de prioridade:")
                    
                    for id_chamado in lista_final:
                        chamado = chamados[id_chamado]
                        print(f"\nID: {id_chamado}, Descrição: {chamado['descricao']}, "
                              f"Prioridade: {chamado['prioridade']}, Status: {chamado['status']}, "
                              f"Área: {chamado['area']}")
                else:
                    limpar_tela()
                    print("Nenhum chamado encontrado para a descrição informada.")

        elif metodo =='4':
            
            limpar_tela()
            
            print("Chamados disponíveis:")
            for id_chamado in chamados:
                
                print(f"\nID: {id_chamado}, Descrição: {chamados[id_chamado]['descricao']}, "
                      f"Prioridade: {chamados[id_chamado]['prioridade']}, "
                      f"Status: {chamados[id_chamado]['status']}, "
                      f"Área: {chamados[id_chamado]['area']}")
            
            mudar_status()
            
        elif metodo.lower() =='x':
            break

def ordem_prioridade():
      
        lista_prioridade_alto_e_medio = []
        lista_prioridade_baixa = []

        for id_chamado, chamado in chamados.items():
                
            if chamado['prioridade'] == 'alta':
                lista_prioridade_alto_e_medio.insert(0, id_chamado)
                
            elif chamado['prioridade'] == 'media':
                lista_prioridade_alto_e_medio.insert(-1, id_chamado)
                
            else:
                lista_prioridade_baixa.append(id_chamado)

        
        lista_final = lista_prioridade_alto_e_medio + lista_prioridade_baixa

        if lista_final:
            limpar_tela()
            print("\nChamados encontrados por ordem de prioridade:")
            
            for id_chamado in lista_final:
                chamado = chamados[id_chamado]
                print(f"\nID: {id_chamado}, Descrição: {chamado['descricao']}, "
                        f"Prioridade: {chamado['prioridade']}, Status: {chamado['status']}, "
                        f"Área: {chamado['area']}")
        else:
            limpar_tela()
            print("Nenhum chamado encontrado para a descrição informada.")