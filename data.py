import pandas as pd

def data_lending():
    df = pd.read_csv('lending_club_loan_two.csv')
    return df.head(50)
