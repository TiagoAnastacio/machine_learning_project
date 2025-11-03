import pandas as pd
from missing_values_cleaner import missing_values_cleaner
from quantity_handler import quantity_handler
from amount_spent_computer import amount_spent_computer
from date_handler import date_handler

def data_cleaner(df) -> pd.DataFrame:
    
    """
    Clean the Online Retail DataFrame by applying the provided steps in order.

    Parameters:
        df : pd.DataFrame
            Original Online Retail DataFrame.

    Returns
        pd.DataFrame
            Cleaned DataFrame after applying previous functions.
    """
    
    # Clean missing values in CustomerID and Description
    clean = missing_values_cleaner(df)
    
    # Remove rows with Quantity <= 0
    clean = quantity_handler(clean)
    
    # Compute the amount spent for each row
    clean = amount_spent_computer(clean)
    
    # Remove invoices from the year 2011
    clean = date_handler(clean)
    
    return clean
