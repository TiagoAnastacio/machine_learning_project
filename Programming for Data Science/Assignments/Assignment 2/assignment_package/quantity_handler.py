import pandas as pd

def quantity_handler(df) -> pd.DataFrame:
    """
    Remove rows where Quantity is zero or negative and return the filtered DataFrame.

    Parameters:
        df : pd.DataFrame
            Original Online Retail DataFrame containing a 'Quantity' column.

    Returns:
        pd.DataFrame
            Copy of df keeping only rows with strictly positive Quantity (> 0).
    """
    df = df.copy()

    # Keep only rows with Quantity > 0
    df = df[df["Quantity"] > 0]

    return df
