import pandas as pd

def load_customer_data(filepath: str) -> pd.DataFrame:
    """
    Load the 'customer_info.csv' into a pandas DataFrame and return it.

    Parameters:
        filepath : str
            Path to the 'customer_info.csv' file.

    Returns:
        pd.DataFrame
            DataFrame with the customer information as read from CSV.
    """
    df = pd.read_csv(filepath)
    return df
