#! /usr/bin/env python

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from util.temp_folder import TEMP


def student_performance_report(df: pd.DataFrame) -> None:
    # This can take ~ ten seconds to import, so only do it when needed.
    from ydata_profiling import ProfileReport

    print(df.describe())
    report = ProfileReport(df)
    report.to_file(TEMP / "student_performance_math_report.html")


def plot_correlations(df: pd.DataFrame) -> None:
    df = clean_student_dataframe(df)
    print(df)
    sns.heatmap(df.corr(), annot=True)
    sns.jointplot(x="G1", y="G3", data=df, kind="reg")
    sns.jointplot(x="G2", y="G3", data=df, kind="reg")
    plt.show()


def clean_student_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop(
        columns=[
            "Fjob",
            "Mjob",
            "Pstatus",
            "address",
            "famsize",
            "guardian",
            "reason",
            "school",
            "sex",
        ]
    )

    pd.set_option("future.no_silent_downcasting", value=True)
    y_or_n_cols = [
        "activities",
        "famsup",
        "higher",
        "internet",
        "nursery",
        "paid",
        "romantic",
        "schoolsup",
    ]
    for col in y_or_n_cols:
        df[col] = df[col].replace({"yes": 1, "no": 0})

    return df.infer_objects(copy=False)


def get_student_performance_df() -> pd.DataFrame:
    return pd.read_csv(TEMP / "student-mat.csv", sep=";")


def main(*, want_report: bool = False) -> None:
    df = get_student_performance_df()

    if want_report:
        student_performance_report(df)

    plot_correlations(df)


if __name__ == "__main__":
    main()
