# Time-Series-Data-Smoother
Suppress noise and extract the meaningful trends for time series data

This module is useful for pre-processing time series data for forecasting purposes. It is assumed that forecasting models are for predefined amounts of time. For example, a particular model should be able to predict 5 days into the future and only 5 days based upon all of the information up until that point in time.

Noisy data requires more observations in order to tease out relationships and fit a model to the true underlying phenomena. Furthermore, noisy data artificially reduces testing and validation scores when assessing model performance. Data points are smoothed with a quadratic fit that is calibrated with time series subset data that reaches back into history by a predefined amount.

To prevent overfitting, the smoothing fit for each data point in the time series depends only upon historical values. If it were fit partially by future values, then the data point would have information about where future data points would be. Furthermore, the historical reach amount should not exceed the forecasting window.
