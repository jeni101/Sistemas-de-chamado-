from cadastro_chamados import *
from busca_chamados import *
from limpar_tela import *

def escolhas():
    while True:
        
        limpar_tela()
        print("""
             _________________________
            |          MENU           |
            |_________________________|
            |cadastrar chamado......|1|
            |listar chamados........|2|                      
            |_________________________|
            """)
        
        decisao = input('oq dejara fazer:')
        
        if decisao == '1':
            limpar_tela()
            cadastro()
            
        elif decisao =='2':
            limpar_tela()
            busca()
            
        else:
            print('escola invalida tente novamente.')


escolhas()
    