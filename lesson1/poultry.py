import pandas as pd

from util.fetch import fetch_csv_dataset

POULTRY_URL = (
    "https://github.com/darheman/project-feed-conversion-ratio-optimization"
    "/raw/refs/heads/main/poultry_data.csv"
)


def get_poultry_data() -> pd.DataFrame:
    d = {
        "Bird ID": "id",
        "Initial Weight (Grams)": "initial_wt",
        "Final Weight (Grams)": "final_wt",
        "Feed Intake (Grams/Week)": "feed_wt",
    }
    df = fetch_csv_dataset(POULTRY_URL).rename(columns=d)
    df = df[list(d.values())]
    assert isinstance(df, pd.DataFrame)
    return df


def main() -> None:
    df = get_poultry_data()
    print(df.describe())
    print(df.dtypes)
    print(df)


if __name__ == "__main__":
    main()
