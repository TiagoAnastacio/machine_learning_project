import pandas as pd
from typing import List

def parenthood_marketing(df, customers) -> List[str]:
    """
    Return the 5 countries with the highest average number of children among their customers.

    Parameters:
        df : pd.DataFrame
            Cleaned Online Retail DataFrame containing 'CustomerID' and 'Country'.
            Used to determine which customers belong to which country (unique customers, not orders).
        customers : pd.DataFrame
            Customer info DataFrame containing 'CustomerID' and 'Children'.

    Returns:
        List[str]
            List of 5 country names (strings), ordered by average number of children in descending order.
    """
    # Remove duplicate CustomerID entries
    df = df.drop_duplicates(subset="CustomerID") 
    merged = pd.merge(df, customers, on="CustomerID", how="inner")
    
    # Compute average number of children per country
    avg_children = merged.groupby("Country")["NumChildren"].mean()
    
    # Order and get the top 5
    top5_countries = avg_children.sort_values(ascending=False).head(5).index.tolist()
    
    return top5_countries
