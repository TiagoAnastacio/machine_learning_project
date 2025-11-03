import pandas as pd

def top_five_spenders(df) -> list:
    """
    Return the CustomerIDs of the five customers who spent the most money.

    Parameters:
        df : pd.DataFrame
            Cleaned Online Retail DataFrame containing 'CustomerID' and the column 'amount_spent' (computed as Quantity * UnitPrice).

    Returns:
        list
            List of five CustomerIDs sorted by total spent in descending order.
    """
    # Calculate total amount spent per CustomerID
    total_spent = df.groupby("CustomerID")["AmountSpent"].sum()

    # Sort descending and take top 5 CustomerIDs
    top_spenders = total_spent.sort_values(ascending=False).head(5).index.tolist()
    
    return top_spenders
