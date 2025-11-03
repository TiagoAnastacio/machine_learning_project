import pandas as pd
from typing import Tuple

def read_sport_dfs(teams_filepath: str, managers_filepath: str) -> Tuple[pd.DataFrame]:
    """
    Load the teams and managers CSV files into pandas DataFrames and return them.

    Parameters:
        teams_filepath : str
            Path to the Teams.csv file with teams data.
        managers_filepath : str
            Path to the Managers.csv file containing managers data.

    Returns:
        (pd.DataFrame, pd.DataFrame)
            A tuple where:
              - teams_df is the DataFrame read from teams_filepath.
              - managers_df is the DataFrame read from managers_filepath.
    """
    teams_df = pd.read_csv(teams_filepath)
    managers_df = pd.read_csv(managers_filepath)
    return teams_df, managers_df
