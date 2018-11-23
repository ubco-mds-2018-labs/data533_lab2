
# coding: utf-8

# In[ ]:


def summary_data(data):
    import pandas as pd   
    data['Start'] = pd.to_datetime(data['Start'])
    data =data.drop(['Finish'], axis =1)
    data.columns = ['date', 'distance', 'steps']
    table = data.groupby(pd.Grouper(key='date',freq='M')).agg({'steps':'mean'})
    table.sort_values(['date'], ascending = True)
    return table

