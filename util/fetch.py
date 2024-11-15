from hashlib import file_digest, sha3_224
from io import BytesIO

import pandas as pd
import requests


def fetch_csv_dataset(
    url: str,
    fingerprint: tuple[int, str] | None = None,
    *,
    sep: str = ",",
) -> pd.DataFrame:
    """Fetches the dataset and returns it as a DataFrame.

    Caller can optionally supply size and hash to verify the dataset's integrity.
    This helps us notice inadvertent edits and revisions to data outside the git repo.
    """
    assert url.startswith("http"), url

    resp = requests.get(url)
    resp.raise_for_status()
    content = BytesIO(resp.content)

    if fingerprint:
        hash_ = fingerprint_hash(content)
        n = len(resp.content)
        assert fingerprint[0] == n, f"Expected {fingerprint}, got {n} bytes"
        assert fingerprint[1] == hash_, f"Expected {fingerprint}, got {hash_}"

    return pd.read_csv(content, sep=sep)


def fingerprint_hash(text: BytesIO, num_nybbles: int = 8) -> str:
    """Returns the given text's size along with a truncated SHA3 hash,
    so we know we have the expected file version.
    """
    digest = file_digest(text, sha3_224)
    return digest.hexdigest()[:num_nybbles]
