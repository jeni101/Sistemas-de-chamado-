from cadastro_chamados import *

contador = 0


def limpar():
    global chamados
    print('Tem certeza que dejeja limpar a lista de chamados? isso apagara todo o historico de uma vez.')
    decisao = input('\n(s/n): ')
    if decisao.lower() =='s':
        chamados.clear()
        print('Lista limpa com sucesso.')
        input('Precione enter para continuar.')
    elif decisao.lower() =='n':
        print('voltando....')
    else:
        print('opcao invalida tente novamente.')





def reverter():
    global contador
    global chamados
    dicionario_invertido = dict(reversed(list(chamados.items())))
    if contador % 2 ==0:
        contador += 1
        for id_chamado in dicionario_invertido:
                    
            print(f"\nID: {id_chamado}, Descrição: {chamados[id_chamado]['descricao']}, "
                f"Prioridade: {chamados[id_chamado]['prioridade']}, "
                f"Status: {chamados[id_chamado]['status']}, "
                f"Área: {chamados[id_chamado]['area']}")
    else:
        contador +=1
        print("Chamados disponíveis:")
        for id_chamado in chamados:
            
            print(f"\nID: {id_chamado}, Descrição: {chamados[id_chamado]['descricao']}, "
                    f"Prioridade: {chamados[id_chamado]['prioridade']}, "
                    f"Status: {chamados[id_chamado]['status']}, "
                    f"Área: {chamados[id_chamado]['area']}")