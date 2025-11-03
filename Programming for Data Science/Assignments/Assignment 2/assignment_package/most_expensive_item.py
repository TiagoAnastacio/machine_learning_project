import pandas as pd

def most_expensive_item(df) -> str:
    """
    Return the Description of the item with the highest UnitPrice.

    Parameters:
        df : pd.DataFrame
            Cleaned Online Retail DataFrame containing 'Description' and 'UnitPrice'.

    Returns
        str
            Description of the most expensive item (row with maximum UnitPrice).
    """
    # Find the description of the product with the highest unit price
    most_expensive = df.loc[df['UnitPrice'].idxmax()]['Description'] 

    return most_expensive
