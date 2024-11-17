import unittest

import pandas as pd
from ucimlrepo import fetch_ucirepo

from util.fetch import fetch_csv_dataset


def get_soybean_cultivars() -> pd.DataFrame:
    ds = fetch_ucirepo("Forty Soybean Cultivars from Subsequent Harvests")  # id=913
    assert ds.data
    assert ds.data.ids is None
    assert ds.data.targets is None
    return ds.data.features


class FetchTest(unittest.TestCase):
    def test_uci(self) -> None:
        df = get_soybean_cultivars()
        self.assertEqual((320, 11), df.shape)

    def test_fetch(self) -> None:
        soybean_url = "https://archive.ics.uci.edu/static/public/913/data.csv"

        df = fetch_csv_dataset(soybean_url, (22735, "c89ff5cc"))
        self.assertEqual((320, 11), df.shape)

        df = fetch_csv_dataset(soybean_url)
        self.assertEqual((320, 11), df.shape)
