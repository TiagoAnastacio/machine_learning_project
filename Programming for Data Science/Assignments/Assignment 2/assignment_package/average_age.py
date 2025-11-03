import pandas as pd
from top_five_cust import top_five_cust

def average_age(df, customers) -> float:
    """
    Compute the average age of the top 5 customers (by number of orders).

    Parameters:
        df : pd.DataFrame
            Cleaned Online Retail DataFrame (used to determine the top 5 customers).
        customers : pd.DataFrame
            Customer info DataFrame containing 'CustomerID' and 'Age'.

    Returns:
        float
            The mean age of the top 5 customers. Rows with missing/non-numeric ages
            are ignored in the average.
    """
    top_customers = top_five_cust(df) 

    # Select ages of top customers
    ages = customers[customers['CustomerID'].isin(top_customers)]['Age'] 
    
    # Compute the mean age
    average = ages.mean() 
    
    return average
