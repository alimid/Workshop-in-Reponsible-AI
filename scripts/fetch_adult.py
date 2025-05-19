
"""Fetch Adult dataset"""
import pandas as pd, os, urllib.request

URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
COLS = ["age","workclass","fnlwgt","education","education-num","marital-status","occupation","relationship","race","sex","capital-gain","capital-loss","hours-per-week","native-country","income"]

def main():
    os.makedirs("data", exist_ok=True)
    out = "data/adult.csv"
    if os.path.exists(out):
        print("Dataset already downloaded")
        return
    df = pd.read_csv(URL, header=None, names=COLS, skipinitialspace=True, na_values=" ?").dropna()
    df.to_csv(out, index=False)
    print("Saved to", out)

if __name__ == "__main__":
    main()
