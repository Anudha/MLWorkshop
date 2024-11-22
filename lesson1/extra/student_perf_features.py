#! /usr/bin/env python

from operator import itemgetter
from pprint import pp

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBRegressor

from lesson1.extra.student_perf_profile import get_student_performance_df


def _encode_categorical_features(df: pd.DataFrame) -> pd.DataFrame:
    cat_cols = [
        "Fjob",
        "Mjob",
        "Pstatus",
        "activities",
        "address",
        "famsize",
        "famsup",
        "guardian",
        "higher",
        "internet",
        "nursery",
        "paid",
        "reason",
        "romantic",
        "school",
        "schoolsup",
        "sex",
    ]
    le = LabelEncoder()
    for col in cat_cols:
        df[col] = le.fit_transform(df[col])
    return df


def _round4(n: float) -> float:
    return round(float(n), 4)


def find_informative_features() -> None:
    """
    Find the most informative features in the student performance dataset
    """
    df = get_student_performance_df().drop(columns=["G1", "G2"])
    df = _encode_categorical_features(df)

    model = XGBRegressor()
    model.fit(df.drop(columns=["G3"]), df.G3)
    feature_names = df.columns[:-1]
    feature_importances_ = map(_round4, model.feature_importances_)
    informative_features = sorted(
        zip(feature_names, feature_importances_, strict=True),
        key=itemgetter(1),
        reverse=True,
    )
    pp(informative_features)


if __name__ == "__main__":
    find_informative_features()
