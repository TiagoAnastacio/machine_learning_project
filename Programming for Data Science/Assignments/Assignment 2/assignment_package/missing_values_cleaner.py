import pandas as pd

def missing_values_cleaner(df) -> pd.DataFrame:
    """
    Return a copy of df with rows removed where CustomerID or Description is missing. 
    Missing values in any other columns are preserved.

    Parameters: 
        df : pd.DataFrame
            Original Online Retail DataFrame.

    Returns: 
        pd.DataFrame
            DataFrame filtered to keep only rows with non-null 'CustomerID' and 'Description'.
    """
    df = df.copy()

    # Remove rows with missing CustomerID or Description
    df = df.dropna(subset=["CustomerID", "Description"]) 
    
    return df
