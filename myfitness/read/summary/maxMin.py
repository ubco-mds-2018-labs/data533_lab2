
# coding: utf-8

# In[ ]:


def getMax(data):
    import pandas as pd
    maximum = data.loc[data['Steps (count)'].idxmax()]
    return maximum

def getMin(data):
    import pandas as pd
    minimum = data.loc[data['Steps (count)'].idxmin()]
    return minimum

