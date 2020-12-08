
# coding: utf-8

# In[61]:


import pandas as pd
import numpy as np
import datetime


def transform():
    import pandas as pd
    import numpy as np
    
    #Reading the data from CV into the dataframe
    df = pd.read_csv('311_data.csv')
    
    #Extracting only the needed columns
    cols = ['Created Date','Closed Date','Borough','Descriptor','Complaint Type', 'Agency', 'Longitude', 'Latitude', 'Status']
    df = df[cols]
    
    #Adding porcessing time column
    df['processing_time'] =  pd.to_datetime(df['Closed Date']) - pd.to_datetime(df['Created Date'])
    
    #Adding 'start_time_window' column
    df['start_time_window'] = pd.to_datetime(df['Created Date']).apply(lambda x: x.hour)
    
    return df.to_csv('output1.csv',index=False)


# In[62]:


# Read-only
transform()
df = pd.read_csv('output1.csv')
df


# In[49]:


# Read-only
transform()
df = pd.read_csv('output1.csv')
df


# In[50]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# In[51]:


sample


# In[52]:


output


# In[53]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# In[54]:


set(list(sample))


# In[55]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# In[56]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# In[57]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# In[58]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# In[59]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# In[60]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# In[ ]:





# In[ ]:




