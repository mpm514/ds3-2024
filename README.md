# COSC 3337 - Data Science I 
## Clustering ##

### Due Date: November 17, 11:59 PM ###

#### The goal of this assignment is to:
1. Learn to use popular clustering algorithms, K-means and DBSCAN.
2. Learn how to interpret and summarize results of clustering.
3. Learn to write evaluation functions to better understand clustering results.
4. Learn to use cross-validation techniques to assess model performance.

## Dataset - Patient Clinical Records
You are given a dataset of patient clinical records. The dataset contains 1000 records, each with 13 attributes. The attributes are as follows:

*Age*: Age of the patient

*Anaemia*: Whether the patient has anaemia (decrease in hemoglobin) (0 = no, 1 = yes)

*Creatinine Phosphokinase*: Level of the CPK enzyme in the blood (mcg/L)

*Diabetes*: Whether the patient has diabetes (0 = no, 1 = yes)

*Ejection Fraction*: Percentage of blood leaving the heart at each contraction (percentage)

*High Blood Pressure*: Whether the patient has hypertension (0 = no, 1 = yes)

*Platelets*: Platelets in the blood (kiloplatelets/mL)

*Serum Creatinine*: Level of serum creatinine in the blood (mg/dL)

*Serum Sodium*: Level of serum sodium in the blook (mEq/L)

*Sex*: Whether the patient is male of female (0 = female, 1 = male)

*Smoking*: Whether the patient smokes or not (0 = no, 1 = yes)

*Time*: Follow-up period (days)

*Death Event*: Whether the patient died during the follow-up period (0 = no, 1 = yes)

### Assignment Tasks ###
The last attribute, *Death Event*, is the class label. The goal of this assignment is to cluster the patients into two groups: those who died during the follow-up period and those who did not. This attribute is to be ignored and you will use the other 12 attributes to cluster the patients.  
The class label is to be used in the post analysis of the clusters generated by running
K-means and DBSCAN.  In addition, ignore the *Time* attribute as well when clustering.

**Task 1**

Write a function ``purity(a,b)`` that computes the purity of a clustering result
based on the class labels of the data points.  The function takes two arguments:
a list of class labels, a, and a list of cluster labels, b.  The function returns a
single number, the purity of the clustering result.  The purity is defined as
the number of data points that were assigned to the correct class label divided
by the total number of data points.  For example, if there are 1000 data points
and 800 of them were assigned to the correct class label, then the purity is
0.8.  The purity is a number between 0 and 1, with 1 being the best possible
purity score.

**Task 2**

Run K-means on the dataset with k=2.  Use the default parameters for the
algorithm.  Compute the purity of the clustering result.  Compute the
purity of the clustering result for each of the two clusters.  Which cluster
has the highest purity?  What percentage of the data points were assigned
to this cluster?  What percentage of the data points were assigned to the
other cluster?  

**Task 3**

Run K-means on the dataset with k=3 and k = 5.  Compute the overall purity of clustering
and the purity of each cluster for each value of k.  Which value of k gives the best
clustering result?  Explain why.

**Task 4**

Run DBSCAN on the dataset with minPts=5 and eps=0.5.  Compute the purity
of the clustering result.  Compute the purity of the clustering result for
each of the two clusters.  Which cluster has the highest purity?  What
percentage of the data points were assigned to this cluster?  What percentage
of the data points were assigned to the other cluster?

**Task 5**

Develop a search procedure to find the best parameters for DBSCAN.  The
parameters to search over are minPts and eps.  The procedure should
maximize the purity of the clustering result, subject to the following constraints:
1. There should be between 2 and 18 clusters.
2. The percentage of outliers should be less than 10%.

Which parameters give the best clustering result?  What is the purity of the 
clustering result?  What is the purity of the clustering result for each of the
clusters?  Which cluster has the highest purity?  



## Deliverables

1. A report that contains the results of your analysis for each of the tasks.  The report should be a pdf file.
2. The code for each of the tasks within the provided shell file ``clustering.py``.  
3. The code should be well documented and easy to follow.  The code should be able to be run from the command line.  The code should generate all the plots required for the report.

## Submission Instructions
Please push and commit your code and report solution to the github repository. Please ensure that your Github username, name, and PSID are filled in at the start of the file.