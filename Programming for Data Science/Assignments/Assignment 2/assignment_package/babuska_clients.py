import pandas as pd

def babuska_clients(df, customers) -> float:
    """
    Calculate the average age of customers who purchased the item
    'HAND WARMER BABUSHKA DESIGN'.

    Parameters:
        df : pd.DataFrame
            Cleaned Online Retail DataFrame containing 'CustomerID' and 'Description'.
        customers : pd.DataFrame
            Customer info DataFrame containing 'CustomerID' and 'Age'.

    Returns:
        float
            Average age of customers who purchased the 'HAND WARMER BABUSHKA DESIGN' item.
    """
    # Remove duplicate purchases of the same item by the same customer
    df = df.drop_duplicates(subset=["CustomerID","Description"]) 

    # Filter for the specific item
    babuska_df = df[df["Description"] == "HAND WARMER BABUSHKA DESIGN"] 
    
    # Merge with customers to get their ages
    merged = pd.merge(babuska_df, customers, on="CustomerID", how="inner")
    
    # Compute the average age of these customers
    avg_age = merged["Age"].mean()
    
    return avg_age
