# test_etl.py
import pandas as pd
from etl import limpar_nome_colunas

def test_limpeza_colunas():
    # Cria um DataFrame "sujo" para teste
    df_sujo = pd.DataFrame({'Nome Cliente': [], 'Data Venda': []})
    
    # Aplica a função
    df_limpo = limpar_nome_colunas(df_sujo)
    
    # O que eu espero que aconteça (Expectativa vs Realidade)
    colunas_esperadas = ['nome_cliente', 'data_venda']
    
    # Se isso for mentira, o teste quebra
    assert list(df_limpo.columns) == colunas_esperadas