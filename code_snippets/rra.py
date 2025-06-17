"""Perform Robust Rank Aggregate (RRA) (Kolde et al., 2012) on a dataframe of scores.
"""
from _aggregate import _robust_rank_aggregate
import pandas as pd

def robust_rank_aggregate(df: pd.DataFrame, score_columns: list[str]) -> pd.Series:
    ranks = df[score_columns].rank(method="min", ascending=True)
    pvals = _robust_rank_aggregate(ranks.to_numpy())
    return pd.Series(pvals, index=df.index)

if __name__ == "__main__":
    df = pd.DataFrame({
        "scorer1": [1, 3, 2],
        "scorer2": [1, 2, 3],
        "scorer3": [1, 3, 2],
    })
    df.index = ["gene1", "gene2", "gene3"]
    print("rho values from robust rank aggregate (RRA):\n")
    print(robust_rank_aggregate(df, ["scorer1", "scorer2", "scorer3"]))