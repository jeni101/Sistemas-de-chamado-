from cadastro_chamados import *
from busca_chamados import *
from limpar_tela import *
from estatistica_chamados import *
from reverter_limpar_chamados import *

def escolhas():
    while True:
        
        limpar_tela()
        print("""
             _________________________
            |          MENU           |
            |_________________________|
            |cadastrar chamado......|1|
            |listar chamados........|2|
            |estatisticas...........|3|
            |limpar chamados........|4|
            |                         |
            |sair...................|x|
            |_________________________|
            """)
        
        decisao = input('Selecione o numero desejado: ')
        
        if decisao == '1':
            limpar_tela()
            cadastro()
            
        elif decisao =='2':
            limpar_tela()
            busca()
            
        elif decisao =='3':
            limpar_tela()
            estatisticas()
            
        elif decisao =='4':
            limpar()
            
        elif decisao.lower() =='x':
            limpar_tela()
            print('saindo......')
            break
        
        else:
            input('Escolha invalida, precione ENTER e tente novamente.')
            


escolhas()
    



   