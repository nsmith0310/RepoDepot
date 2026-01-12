Note: The relevant datasets have not been uploaded due to file size. If you would like the datasets, please reach out to me at
nicholasms19920310@gmail.com 

EE output forecasting:
-uses a bidirectional GRU RNN to predict EEG (electroencephalogram) outputs from readings obtained from test subjects playing video games
-uses the GAMEEMO dataset
-model achieves over .88 accuracy

Smart grid load forecasting:
-compares ensemble gradient boosting regression against K-nearest neighbors regression for forecasting smart grid load 
-uses a dataset consisting of historical daily temperatures and loads
-performs a search for the best mapping between temperature recording stations and load recording stations
-gradient boosting achieves .88 average R^2 
-K-nearest neighbors achieves .82 average R^2
