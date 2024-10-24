import pandas as pd

def load_titanic_data(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath)
    return df

#testing function's execution
if _name_ == "_main_":
    filepath = "data/titanic.csv"  
    titanic_data = load_titanic_data(filepath)