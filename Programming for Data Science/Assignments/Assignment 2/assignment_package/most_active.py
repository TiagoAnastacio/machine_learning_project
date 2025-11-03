import pandas as pd
from typing import List

def most_active(customers) -> List[str]:
    """
    Return the emails of the customers who have been active for the longest time.

    Parameters:
        customers : pd.DataFrame
            Customer info DataFrame containing 'YearsActive' and 'Email'.

    Returns:
        List[str]
            List of email strings for all customers whose YearsActive equals the maximum value observed.
    """
    #Get the maximum YearsActive value
    max_years = customers["YearsActive"].max() 
    
    # Filter customers with that maximum value and return their emails
    most_active_emails = customers.loc[customers["YearsActive"] == max_years, "Email"].tolist()
    
    return most_active_emails
