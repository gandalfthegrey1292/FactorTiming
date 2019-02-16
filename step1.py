# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 13:53:22 2019

@author: yangy
"""

import numpy as np
import pandas as pd
import os
os.chdir('C:/UCB/230K/factor timing project')
import datetime


inflation = pd.read_csv('WRDS_inflation.csv')

inflation.set_index(pd.to_datetime(inflation.caldt, format = '%Y%m%d'),inplace = True)
del inflation['caldt']

factor = pd.read_csv('WRDS_factors.csv')
factor.set_index(pd.to_datetime(factor.date, format = '%Y%m%d'), inplace = True)
del factor['date']


