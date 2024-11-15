from pathlib import Path

import pandas as pd
from ydata_profiling import ProfileReport

TEMP = Path("/tmp")


def student_performance_report() -> None:
    df = pd.read_csv(TEMP / "student-mat.csv", sep=";")
    print(df)
    print(df.dtypes)
    print(df.describe())
    prof = ProfileReport(df)
    prof.to_file(str(TEMP / "student_performance_math_report.html"))


if __name__ == "__main__":
    student_performance_report()
