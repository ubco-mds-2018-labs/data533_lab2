
# coding: utf-8

# In[ ]:


def getMax(data):
    import pandas as pd
    return data.loc[data['Steps (count)'].idxmax()]

