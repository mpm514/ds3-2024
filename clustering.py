"""clustering.py: Starter file for assignment on Clustering """

__author__ = "Shishir Shah"
__version__ = "1.0.0"
__copyright__ = "All rights reserved.  This software  \
                should not be distributed, reproduced, or shared online, without the permission of the author."

# Data Manipulation and Visualization
import pandas as pd #creating and manipulating dataframes
import matplotlib.pyplot as plt #visuals
import seaborn as sns #visuals
from sklearn.cluster import KMeans #K-Means
from sklearn.cluster import DBSCAN #DBSCAN

__author__ = "Please enter your name here"
__version__ = "1.1.0"

'''
Github Username: 
PSID:
'''

# Reading the data
data = pd.read_csv('data/clinical_records_dataset.csv')
class_labels = data['DEATH_EVENT']
data = data.drop('DEATH_EVENT', axis=1)
data = data.drop('time', axis=1)

''' Write your code here '''




