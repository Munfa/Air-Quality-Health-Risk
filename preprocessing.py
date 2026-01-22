import pandas as pd
from sklearn.model_selection import train_test_split
from features import compute_aqi

df = pd.read_csv("data/global_air_quality_data.csv")
df = compute_aqi(df)

df.set_index('Date', inplace=True)
df.sort_index(inplace=True)

# train_df, test_df = train_test_split(df, test_size=0.25, random_state=42)
# train_df = pd.DataFrame(train_df)
# test_df = pd.DataFrame(test_df)

# train_df.to_csv("data/train_data.csv")
# test_df.to_csv("data/test_data.csv")

# print(df[:3])