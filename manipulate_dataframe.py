import pandas as pd

def clean_dataframe(df):
  # drop invalid rows and columns
  df = df.dropna()
  df = df.drop(columns=['ID', 'Notes', 'Source'])

  # rename columns
  df = df.rename(columns={'Price USD': 'Price'})

  # check for duplicates
  df = df.drop_duplicates()

  return df

if __name__ == '__main__':
  # read dataframe from csv file
  df = pd.read_csv('data_frame.csv')

  # clean dataframe
  df = clean_dataframe(df)

  # write cleaned dataframe to csv file
  df.to_csv('cleaned_dataframe.csv', index=False)
