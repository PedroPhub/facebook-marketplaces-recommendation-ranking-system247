import pandas as pd


def remove_null_rows(dataframe: pd.DataFrame) -> pd.DataFrame:
  """
  Drops rows with null values from a DataFrame.

  Keyword arguments:
    dataframe: pd.DataFrame -- The DataFrame to clean.

  Returns:
    dataframe: pd.DataFrame -- The DataFrame with rows containing null values removed.
  """
  return dataframe.dropna()

def clean_dataframe_data(filename: str) -> pd.DataFrame:
    """
    Removes null values from dataframe and £ from the price column.
    
    Keyword arguments:
      filename: str -- Name of the file containing the DataFrame to clean.

    Returns:
      dataframe: pd.DataFrame -- Dataframe with £ and null values in price column.
    """
    dataframe = pd.read_csv(filename, lineterminator='\n')
    dataframe = remove_null_rows(dataframe)
    if 'price' in dataframe.columns:
      dataframe['price'] = dataframe['price'].replace({'£':'',',':''}, regex=True)
    print(dataframe)

    return dataframe