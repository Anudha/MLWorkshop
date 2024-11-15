import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
from statsmodels.regression.linear_model import RegressionResultsWrapper

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


def create_ydata_profile_report(df: pd.DataFrame) -> None:
    from ydata_profiling import ProfileReport

    print(df)
    report = ProfileReport(df)
    report.to_file(TEMP / "poultry_report.html")


def ols_regression(x: pd.Series, y: pd.Series) -> RegressionResultsWrapper:
    model = sm.OLS(y, x).fit()
    assert isinstance(model, RegressionResultsWrapper)
    return model


def main(*, want_profile: bool = False) -> None:
    df = get_poultry_data()
    df["wt_gain"] = df.final_wt - df.initial_wt
    if want_profile:
        create_ydata_profile_report(df)

    df = df.drop(columns=["id"])
    sns.pairplot(df)

    model = ols_regression(df.feed_wt, df.wt_gain)
    df["predicted_gain"] = model.predict(df.feed_wt)

    # Reshape from wide to long format.
    df_long = df.melt(
        id_vars=["feed_wt"],
        value_vars=["wt_gain", "predicted_gain"],
        var_name="gain_type",
        value_name="gain",
    )
    ax = sns.scatterplot(data=df_long, x="feed_wt", y="gain", hue="gain_type")
    ax.set_xlim(0, None)
    ax.set_ylim(0, None)
    plt.show()


if __name__ == "__main__":
    main()
