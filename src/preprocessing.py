import pandas as pd
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.metrics import mean_squared_error
from features import compute_aqi
from sklearn.preprocessing import StandardScaler
import joblib

df = pd.read_csv("data/global_air_quality_data.csv")
df = compute_aqi(df)
df.dropna(inplace=True)

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
y_test = test_df['AQI']

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# joblib.dump(scaler, "saved_models/scaler.joblib")

model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, max_depth=5, eta=0.1)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

error = mean_squared_error(y_test, y_pred)

print("Error: ", error)

# joblib.dump(model, "saved_models/model.joblib")
# print("Models saved successfully")
