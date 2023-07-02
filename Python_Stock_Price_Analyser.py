import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import datetime as dt
# Install these on command line: pip install numpy, ...

from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM

# 1. Load Data
company = 'TSLA'

start = dt.datetime(2012,1,1)
end = dt.datetime(2020,1,1)

data = web.DataReader(company, 'yahoo', start, end)
# Using yahoo finance API from start to end date

# 2. Prepare Data
# Scale down all values to fit between 0 and 1
scaler = MinMaxScaler(feature_range = (0,1))  # from sklearn.preprocessing module
scaled_data = scaler.fit_transform(data['Close'].values.reshape(-1,1))  # Only interested in closing price after markets close

prediction_days = 60

x_train = []
y_train = []
# Prepare training data

for x in range(prediction_days, len(scaled_data)):
    # start counting from 60th index up until the last index

    x_train.append(scaled_data[x-prediction_days:x, 0])
    # add value to x_train and append 60 values then prepare the 61st value - model can learn to predict what 61st value is

    y_train.append(scaled_data[x,0])
    # 61st value

x_train, y_train = np.array(x_train), np.array(y_train)
# now reshape x_train so it fits with the scaler in the neural network
x_train = np.reshape(x_train, (x_train.shape[0], (x_train[1], 1)))  # add one additional dimension, 1

# 3. Build The Model
model = Sequential()

model.add(LSTM(units = 50, return_sequences = True, input_shape = (x_train.shape[1],1)))
model.add(Dropout(0.2))
model.add(LSTM(units = 50, return_sequences = True))
model.add(Dropout(0.2))
model.add(LSTM(units = 50))
model.add(Dropout(0.2))
model.add(Dense(units = 1))  # Prediction of next closing value/price

model.compile(optimizer = 'adam', loss = 'mean_squared_error')
model.fit(x_train, y_train, epochs = 25, batch_size = 32)
# epocs means model will see the data 25 times
# batch_size means model will see 32 units at once

""" Test The Model Accuracy on Existing Data """

# 4. Load Test Data
test_start = dt.datetime(2022,1,1)
test_end = dt.datetime.now()

test_data = web.DataReader(company, 'yahoo', test_start, test_end)
actual_prices = test_data['Close'].values

total_dataset = pd.concat((data['Close'],test_data['Close']), axis = 0)

model_inputs = total_dataset[len(total_dataset) - len(test_data) - prediction_days:].values
model_inputs = model_inputs.reshape(-1,1)
model_inputs = scaler.transform(model_inputs)

# 5. Make Predictions on Test Data

x_test = []

for x in range(prediction_days, len(model_inputs)):
    x_test.append(model_inputs[x-prediction_days:x, 0])

x_test = np.array(x_test)
x_test = np.reshape(x_test, x_test.shape[0], x_test.shape[1], 1)

predicted_prices = model.predict(x_test)
predicted_prices = scaler.inverse_transform(predicted_prices)

# 19.48s

#  6. Plot The Test Predictions
plt.plot(actual_prices, color = "black", label = f"Actual {company} Price")
plt.plot(predicted_prices, color = "green", label = f"Predicted {company} Price")
plt.title(f"{company} Share Price")
plt.xlabel("Time")
plt.ylabel(f"{company} Share Price")
plt.legend()
plt.show()

