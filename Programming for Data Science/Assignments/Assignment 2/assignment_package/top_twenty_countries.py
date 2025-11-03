import pandas as pd
from typing import List

def top_twenty_countries(df) -> List[str]:
    """
    Return the 20 countries with the highest number of orders (unique InvoiceNo).

    Parameters:
        df : pd.DataFrame
            Cleaned Online Retail DataFrame containing 'Country' and 'InvoiceNo'.

    Returns:
        List[str]
            List of country names (strings), ordered by number of orders in descending order, limited to the top 20.
    """
    # Drop duplicates of InvoiceNo per Country to count each order only once
    unique_orders = df.drop_duplicates(subset=["Country", "InvoiceNo"])

    # Count number of orders per Country
    orders_count = unique_orders.groupby("Country")["InvoiceNo"].count()
    
    # Sort descending and take top 20 Countries
    top_countries = orders_count.sort_values(ascending=False).head(20).index.tolist()
    
    return top_countries
