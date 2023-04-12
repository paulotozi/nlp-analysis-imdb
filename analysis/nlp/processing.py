import pandas as pd

def processar_dados():

    df = pd.read_csv("../web_scraper/test.csv")

    df.dropna(inplace = True)

    df.drop_duplicates(subset = None, keep = 'first', inplace = True)

    df["review_pt_processado"] = df["review_pt"].str.lower()

    return df