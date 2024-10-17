import pandas as pd

def calcula_tamanho_dataframe(dataframe : pd.DataFrame):
    """Dado um dataframe, imprime seu tamanho.

    Args:   
        dataframe (_type_): _description_
    """
    print(
        f"O dataframe tem tamanho {dataframe.shape}"
        )