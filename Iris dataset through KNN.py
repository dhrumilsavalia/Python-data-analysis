#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install sklearn


# In[3]:


import numpy as np
import pandas as pd


# In[5]:


df=pd.read_csv(r'E:\Dhrumil\Datasets\tableconvert_csv_qze8gx.csv')
df.head()


# In[7]:


print(df.shape)


# In[8]:


print(df.columns)


# In[9]:


data=df.values


# In[10]:


x=data[:,:-1]
y=data[:,4]


# In[11]:


x.shape


# In[12]:


y.shape


# In[14]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.2)


# In[16]:


from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=7)
classifier.fit(X_train,y_train)


# In[18]:


y_pred=classifier.predict(X_test)


# In[19]:


from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
result=confusion_matrix(y_test,y_pred)
print("Confusion Matrix:",result)
result1=classification_report(y_test,y_pred)
print("Classification report",result1)
result2=accuracy_score(y_test,y_pred)
print("Accuracy score is:",result2)


# In[ ]:




