import pandas as pd
from typing import List

def popular_products(df) -> List[str]:
    """
    Return the descriptions of the 5 products purchased the most times (by order count).

    Parameters:
        df : pd.DataFrame
            Cleaned Online Retail DataFrame containing 'Description' and 'InvoiceNo'.

    Returns:
        List[str]
            List with 5 product descriptions ordered by number of distinct orders (unique InvoiceNo) in descending order.
    """
    # Count number of orders per Description
    products = df.groupby("Description")["Description"].count()

    # Sort descending and take top 5 Descriptions
    top_products = products.sort_values(ascending=False).head(5).index.tolist()
    
    return top_products
