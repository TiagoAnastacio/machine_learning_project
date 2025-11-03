import pandas as pd

def load_retail_data(filepath: str) -> pd.DataFrame:
    """
    Load the Online Retail CSV into a pandas DataFrame and return it.

    Parameters: 
        filepath : str
            Path to 'onlineretail.csv'.

    Returns: 
        pd.DataFrame
            The dataset as loaded (no additional processing).
    """
    df = pd.read_csv(filepath,encoding='ISO-8859-1')
    return df
