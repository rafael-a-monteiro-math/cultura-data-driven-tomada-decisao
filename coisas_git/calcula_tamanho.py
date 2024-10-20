import pandas as pd

def calcula_tamanho_dataframe(dataframe : pd.DataFrame):
    """Dado um dataframe, imprime seu tamanho.

    Args:   
        dataframe (pandas DataFrame):dataframe.
        
    """
    print(
        f"O dataframe tem tamanho {dataframe.shape}"
        )