
# coding: utf-8

# # Loan Prediction

# In[1]:


import pandas as pd
import numpy as np
import matplotlib as plt
# importing the dataset from local directory
df = pd.read_csv("file:///C:/Git-Projects/Loan-prediction/train_u6lujuX_CVtuZ9i.csv")


# In[2]:


df.head(10) #displaying the top 10 rows


# In[3]:


#looking at the summary of of numeric fields by using describe()
df.describe()


# In[4]:


# for non-numeric values like Property_Area, Credit_History etc. we can look
# at the frequency distribution to undestand whether they make sense or not.
# the frequncy table can be printed by:
df['Property_Area'].value_counts()


# #### Studying the distributions of various variables

# In[6]:


# plotting the histogram of ApplicantIncome
df['ApplicantIncome'].hist(bins=50)


# In[7]:


# using box plot to uderstand the distribution
df.boxplot(column='ApplicantIncome')


# #### Lot of outliers can be attributed to the income disparity in the society. Part of this can be driven by the fact that we are looking at people with different education levels.

# In[9]:


# segregating people by Education
df.boxplot(column= 'ApplicantIncome', by='Education')


# #### Taking a look at the histogram and boxplot of LoanAmount 

# In[10]:


df['LoanAmount'].hist(bins=50)


# In[12]:


df.boxplot(column='LoanAmount')


# In[15]:


temp1 = df['Credit_History'].value_counts(ascending=True)
temp2 = df.pivot_table(values='Loan_Status', index=['Credit_History'], 
                       aggfunc=lambda x: x.map({'Y':1,'N':0}).mean())
print('Frequency Table for Credit History:')
print(temp1)
print('Probability of getting loan for each credit History class:')
print(temp2)


# In[19]:


# plotting the pivot table 
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8,4))
ax1 = fig.add_subplot(1,2,1)
ax1.set_xlabel('Credit History')
ax1.set_ylabel('Count of Applicants')
ax1.set_title('Applicants by Credit History')
temp1.plot(kind='bar')

ax2 = fig.add_subplot(1,2,2)
temp2.plot(kind='bar')
ax2.set_xlabel('Credit History')
ax2.set_ylabel('Probability of getting loan')
ax2.set_title('Probability of getting loan by credit history')

