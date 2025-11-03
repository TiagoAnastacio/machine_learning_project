import pandas as pd

def top_five_cust(df) -> list:
    """
    Return the CustomerIDs of the five customers who placed the highest number of orders.
    
    Parameters:
        df : pd.DataFrame
            Cleaned Online Retail DataFrame containing 'CustomerID' and 'InvoiceNo'.
            An order is defined by a unique 'InvoiceNo' (multiple rows per invoice count as one).

    Returns:
        list
            List of five CustomerIDs sorted by number of orders in descending order.
    """
    # Drop duplicates of InvoiceNo per CustomerID to count each order only once
    unique_orders = df.drop_duplicates(subset=["CustomerID", "InvoiceNo"])
    
    # Count number of orders per CustomerID
    orders_count = unique_orders.groupby("CustomerID")["InvoiceNo"].count()
    
    # Sort descending and take top 5 CustomerIDs
    top_customers = orders_count.sort_values(ascending=False).head(5).index.tolist()
    
    return top_customers
