
# coding: utf-8

# In[ ]:


def getMin(data):
    import pandas as pd
    return data.loc[data['Steps (count)'].idxmin()]

