import pandas as pd
from sklearn.model_selection import train_test_split
from features import compute_aqi
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("data/global_air_quality_data.csv")
df = compute_aqi(df)

df.set_index('Date', inplace=True)
df.sort_index(inplace=True)

train_df, test_df = train_test_split(df, test_size=0.25, random_state=42)
train_df = pd.DataFrame(train_df)
test_df = pd.DataFrame(test_df)

########### files saved ########
# train_df.to_csv("data/train_data.csv")
# test_df.to_csv("data/test_data.csv")

X_train = train_df.drop(['City', 'Country', 'AQI'], axis=1)
y_train = train_df['AQI']

X_test = test_df.drop(['City', 'Country', 'AQI'], axis=1)
y_train = test_df['AQI']

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

