import pandas as pd
from go_sports import go_sports

def go_manager(teams: pd.DataFrame, managers: pd.DataFrame) -> str:
    """
    Return the managerID of the manager with the highest total number of wins (W).

    Parameters:
        teams : pd.DataFrame
            Team-season DataFrame used to compute wins per manager (via `go_sports`).
        managers : pd.DataFrame
            Manager assignments DataFrame passed to `go_sports`.

    Returns:
        str
            The managerID whose aggregated wins (sum of W across seasons) is the highest.
    """
    # Dropna to avoid issues when summing
    sports = go_sports(teams, managers).dropna(subset=["managerID"])

    # Ensure W is numeric just in case the column is not
    sports["W"] = pd.to_numeric(sports["W"], errors="coerce").fillna(0)

    # Total wins per manager and pick the top one
    wins_by_manager = sports.groupby("managerID")["W"].sum()
    top_manager = wins_by_manager.idxmax() # if there are ties, idxmax returns the first one it encounters

    return str(top_manager)
