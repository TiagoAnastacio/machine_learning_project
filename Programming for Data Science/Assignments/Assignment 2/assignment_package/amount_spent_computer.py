import pandas as pd

def amount_spent_computer(df) -> pd.DataFrame:
    """
    Add a new column 'amount_spent' equal to Quantity * UnitPrice and return the result.

    Parameters:
        df : pd.DataFrame
            Online Retail DataFrame containing 'Quantity' and 'UnitPrice' columns.

    Returns:
        pd.DataFrame
            Copy of df with an additional 'amount_spent' column.
    """
    df = df.copy()

    # Calculate amount spent and add as new column
    df["AmountSpent"] = df["Quantity"] * df["UnitPrice"]
    return df
