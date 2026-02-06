# etl.py
import pandas as pd

def limpar_nome_colunas(df):
    """Padroniza nomes de colunas: minusculo e sem espaco"""
    df.columns = [c.lower().replace(' ', '-') for c in df.columns]
    return df

if __name__ == "__main__":
    # Simula um dado chegando
    data = {'Nome Cliente': ['Vitor', 'Maria'], 'VALOR COMPRA': [100, 200]}
    df = pd.DataFrame(data)
    
    print("--- Antes ---")
    print(df.columns)
    
    df_limpo = limpar_nome_colunas(df)
    
    print("\n--- Depois ---")
    print(df_limpo.columns)