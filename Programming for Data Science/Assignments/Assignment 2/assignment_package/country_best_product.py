import pandas as pd

def country_best_product(df, country) -> str:
    """
    Return the description of the most frequently purchased item in a given country.

    Parameters:
        df : pd.DataFrame
            Cleaned Online Retail DataFrame containing 'Country', 'Description', and 'InvoiceNo'.
        country : str
            Country name to filter the dataset.

    Returns:
        str | None
            Description of the item with the highest number of distinct orders (unique InvoiceNo) within the given country. Returns None if the country is not present in the DataFrame.
    """
    # Check if the country exists in the DataFrame and compute the best product or None
    if country in df['Country'].values:
        country_data = df[df['Country'] == country] # Filter data for the specified country
        product_sales = country_data.groupby('Description')['Description'].count() # Count orders per product
        best_product = product_sales.idxmax() # Get the product with the maximum orders
        return best_product
    else:
        return None
