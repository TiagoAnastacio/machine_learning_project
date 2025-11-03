import pandas as pd

def date_handler(df) -> pd.DataFrame:
    """
    Remove all rows whose invoices are from the year 2011 and return the filtered DataFrame.

    Parameters:
        df : pd.DataFrame
            Online Retail DataFrame containing an 'InvoiceDate' column.

    Returns:
        pd.DataFrame
            Copy of df without any rows where InvoiceDate belongs to year 2011.
    """
    # Convert 'InvoiceDate' to datetime if not already
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

    # Remove rows from year 2011
    df = df[df["InvoiceDate"].dt.year != 2011]
    
    return df
