# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 19:42:24 2018

@author: Jake
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

class TimeSeriesSmoother():
    
    '''Points comprised of time stamp and value'''
    TimeSeries = np.zeros((0))
    
    '''Reach is in days'''
    SmoothReach = 0
    
    '''Bounds are time stamps'''
    TimeLowerBound = 0
    TimeUpperBound = 0
    
    def __init__(self,timeSeries,smoothReach):
        
        '''Store the data internally within the TimeSeriesSmoother object'''
        self.TimeSeries = timeSeries
        
        '''Time series data should be ordered newest to oldest from top to bottom'''
        self.SmoothReach = smoothReach
        
        '''Pandas Timestamps'''
        self.TimeLowerBound = timeSeries[len(timeSeries)-1,:]
        self.TimeUpperBound = timeSeries[0,:]
        
        return
    
    
    def Smooth(self):
        
        '''Initialize the smoothed time series array to be returned'''
        smoothTimeSeries = np.zeros((len(self.TimeSeries),2))
        
        '''Smooth each data point'''
        smoothTime = self.TimeLowerBound
        while smoothTime <= self.TimeUpperBound:
            
            '''Construct a boolean array to tell whether or not each time stamp is within historical reach'''
            aboveLowerBound = self.TimeSeries[:,0] >= self.TimeLowerBound
            belowUpperBound = self.TimeSeries[:,0] <= self.TimeUpperBound
            withinReach = (aboveLowerBound == belowUpperBound)
            
            '''Count the number of time stamps that are within historical reach'''
            relevantPoints = np.count_nonzero(withinReach)
            
            
            '''Extract relevant data points for time series subset'''
            subsetTimeSeries = np.zeros((relevantPoints,2))
            timeSeriesIndex = 0
            subsetIndex = 0
            while timeSeriesIndex <= len(self.TimeSeries)-1:
                
                if self.TimeSeries[timeSeriesIndex,0] == True:
                    subsetTimeSeries[subsetIndex,:] = self.TimeSeries[timeSeriesIndex,0:2]        
                    subsetIndex = subsetIndex + 1
                    
                timeSeriesIndex = timeSeriesIndex + 1
            
            '''
            Things to do yet:
                1) Convert time stamps into numerical values
                2) Create extra column to hold quadratic terms
                3) Calibrate MLR model
                4) Predict smooth point
                5) Store smooth point
            '''
            
            '''Increment current time stamp by one day'''
            smoothTime += pd.Timedelta('1d')
        
        return
    
