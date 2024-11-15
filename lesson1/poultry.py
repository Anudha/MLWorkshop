import pandas as pd
from ydata_profiling import ProfileReport

from util.fetch import fetch_csv_dataset
from util.temp_folder import TEMP

POULTRY_URL = (
    "https://github.com/darheman/project-feed-conversion-ratio-optimization"
    "/raw/refs/heads/main/poultry_data.csv"
)


def get_poultry_data() -> pd.DataFrame:
    d = {
        "Bird ID": "id",
        "Initial Weight (Grams)": "initial_wt",
        "Feed Intake (Grams/Week)": "feed_wt",
        "Final Weight (Grams)": "final_wt",
    }
    df = fetch_csv_dataset(POULTRY_URL).rename(columns=d)
    return pd.DataFrame(df[list(d.values())])


def main() -> None:
    df = get_poultry_data()
    df["wt_gain"] = df.final_wt - df.initial_wt
    print(df.describe())
    print(df.dtypes)
    print(df)
    report = ProfileReport(df)
    report.to_file(TEMP / "poultry_report.html")


if __name__ == "__main__":
    main()
