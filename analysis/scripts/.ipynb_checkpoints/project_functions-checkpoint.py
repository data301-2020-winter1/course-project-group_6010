import pandas as pd
import numpy as np

def unprocessed(csv_file):
    df = pd.read_csv(csv_file)
    return df

def load_and_process(csv_file):
    df = pd.read_csv(csv_file)
    df1=(df.dropna(subset=["Year_of_Release","Publisher","Critic_Score","Critic_Count","User_Score","User_Count","Developer","Rating"]) 
        .sort_values("Genre")
        .reset_index(drop=True)
        )    
    return df1
         