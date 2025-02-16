from cadastro_chamados import *

def estatisticas():
    
    chamados_em_aberto = 0
    chamados_finalizados = 0
    chamados_urgentes = 0
    chamados_media_prioridade = 0
    chamados_baixa_prioridade = 0
    
    
    total_chamados = (len(chamados))
    for id_chamado, chamado in chamados.items():
        
        if chamado['status'].lower() == 'aberto':
            chamados_em_aberto += 1
            
        elif chamado['status'].lower() == 'fechado':
            chamados_finalizados += 1
            
        if chamado['prioridade'].lower() == 'alta':
            chamados_urgentes += 1
            
        elif chamado['prioridade'].lower() == 'media':
            chamados_media_prioridade += 1
            
        elif chamado['prioridade'].lower() == 'baixa':
            chamados_baixa_prioridade += 1
            
    
    
    
    input(f"""
          |---------------------------------------------------|
          |                   ESTATÍSTICAS:                   |
          |-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|
          | TOTAL DE CHAMADOS:             |        {total_chamados:<3}       |
          | CHAMADOS EM ABERTO:            |        {chamados_em_aberto:<3}       |
          | CHAMADOS FINALIZADOS:          |        {chamados_finalizados:<3}       |
          | CHAMADOS URGENTES:             |        {chamados_urgentes:<3}       |
          | CHAMADOS DE PRIORIDADE MEDIANA:|        {chamados_media_prioridade:<3}       |
          | CHAMADOS COM POUCA URGÊNCIA:   |        {chamados_baixa_prioridade:<3}       |
          |________________________________|__________________|
          
          Precione ENTER para voltar ao menu.
          """)

