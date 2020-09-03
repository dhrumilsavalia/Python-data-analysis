#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df=pd.read_csv(r'E:\Dhrumil\Datasets\fruit_data (1).csv')
df.head()


# In[18]:


data=df.values
x=data[:,3:]
y=data[:,0]
y=y.astype('int')


# In[19]:


x.shape


# In[20]:


y.shape


# In[49]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.2)


# In[50]:


from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=3)
classifier.fit(X_train,y_train)


# In[51]:


y_pred=classifier.predict(X_test)


# In[52]:


from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
result=confusion_matrix(y_test,y_pred)
print("Confusion Matrix:",result)
result1=classification_report(y_test,y_pred)
print("Classification report",result1)
result2=accuracy_score(y_test,y_pred)
print("Accuracy score is:",result2)


# In[ ]:




