# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 14:51:29 2020

@author: htbc
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %matplotlib inline
sales = pd.read_csv(
    'data/sales_data.csv',
    parse_dates=['Date'])
sales.head()
sales['Customer_Age'].mean()
sales['Customer_Age'].plot(kind='kde', figsize=(8,4))
#sales['Year'].plot(kind='pie')
sales['Year'].value_counts().plot(kind='pie', figsize=(6,6))

