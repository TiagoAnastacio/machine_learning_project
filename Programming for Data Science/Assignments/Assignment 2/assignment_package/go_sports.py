import pandas as pd

def go_sports(teams: pd.DataFrame, managers: pd.DataFrame) -> pd.DataFrame:
    """
    Combine teams and managers by season and return a DataFrame.

    Parameters:
        teams : pd.DataFrame
            Team-season DataFrame.
        managers : pd.DataFrame
            Manager assignments DataFrame.

    Returns:
        pd.DataFrame
            DataFrame with columns: 'name', 'managerID', 'yearID' (yyyy string), 'W', 'L'.
    """
    # Work on copies
    t = teams.copy()
    m = managers.copy()

    # Remove the spaces in managersID column 
    m["managerID"] = m["managerID"].str.replace(" ", "")

    # Normalize yearID to 4-char string
    t["yearID"] = t["yearID"].astype(str).str[:4]
    m["yearID"] = m["yearID"].astype(str).str[:4]

    # Merge
    merged = pd.merge(t,
                      m[["teamID", "yearID", "managerID"]],
                      how="left",
                      on=["teamID", "yearID"])
                      

    # Return only required columns
    return merged[["name", "managerID", "yearID", "W", "L"]]
