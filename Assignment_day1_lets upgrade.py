#!/usr/bin/env python
# coding: utf-8

# # Exploring default methods in list

# In[2]:


lst=["Dhrumil","savalia","4th year","PDPU"]
print(lst)


# In[3]:


lst.append("Petroleum engineering")


# In[4]:


lst


# In[7]:


lst.extend(["pizza","burger"])


# In[8]:


lst


# In[9]:


lst.insert(0,"student")
lst


# In[10]:


lst.remove(1)
lst


# In[12]:


lst.pop(6)
lst


# In[14]:


lst


# In[16]:


lst.extend(["Dhrumil","savalia","4th year","PDPU"])
lst


# In[17]:


lst.index("Dhrumil")


# In[18]:


lst.count("savalia")


# In[22]:


lst.sort(key=len)
lst


# In[25]:


lst.reverse()
lst


# In[26]:


lst.copy()
lst


# # Exploring methods in dictionary

# In[27]:


fruits={"Oranges":5,"Bananas":6,"Mango":13}
fruits


# In[28]:


fruits_new=fruits.copy()
fruits_new


# In[30]:


fruits.values()


# In[31]:


fruits.keys()


# In[33]:


keys={"watermelon","apple","Guava"}
values=5
fruits.fromkeys(keys,values)


# In[34]:


fruits.get("Oranges")


# In[35]:


fruits.items()


# In[36]:


fruits.popitem()
fruits


# In[37]:


fruits.setdefault("Bananas")


# In[38]:


fruits["Peach"]=7
fruits


# In[39]:


fruits.pop("Oranges")
fruits


# In[42]:


d1={"kiwi":7}
fruits.update(d1)
fruits


# # Exploring methods in a set

# In[40]:


subjects={"production","reservoir","drilling","exploration",1,2,2,3,3,3,4,4,5,6}
subjects


# In[41]:


subjects.add("well logging")
subjects


# In[43]:


s1={7,8,9}
subjects.update(s1)
subjects


# In[44]:


subjects.discard(7)
subjects


# In[45]:


subjects.remove(4)
subjects


# In[47]:


s2={"disciplines","petroleum engineering"}
subjects.union(s2)


# In[48]:


s3={5,6,7,8}
subjects.intersection(s3)


# In[49]:


subjects.difference(s3)


# In[51]:


subjects.symmetric_difference(s3)


# In[52]:


s1.intersection_update(subjects,s3)
s1


# In[54]:


frozenset(s1)


# In[55]:


subjects.issubset(s2)


# In[57]:


subjects.issuperset(s3)


# In[58]:


subjects.isdisjoint(s2)


# In[61]:


s2.symmetric_difference_update(subjects)
s2


# # Exploring methods in a tuple

# In[62]:


numbers=(78,56,89,36,45,56,78,89)
numbers


# In[63]:


numbers.count(78)


# In[64]:


numbers.index(36)


# In[ ]:




