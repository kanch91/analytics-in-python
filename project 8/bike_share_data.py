
# coding: utf-8

# ## There are some instructions you need to follow:
# <li> You only need to write your code in the comment area "Your Code Here".</li>
# <li>Do not upload your own file. Please make the necessary changes in the Jupyter notebook file already present in the server.</li>
# <li>Please note, there are several cells in the Assignment Jupyter notebook that are empty and read only. Do not attempt to remove them or   edit them. They are used in grading your notebook. Doing so might lead to 0 points.</li>

# In[70]:


import numpy as np
import pandas as pd
from sklearn import datasets, linear_model

"""
Question 1

Transform the data.
"""


def filter_bike_data(filename = 'bikeshare_data.csv'):
    #Reading the file
    data = pd.read_csv(filename,header=0)
    
    #Removing the holidays
    hol = data[data['holiday'] == 1].index 
    data.drop(hol, inplace = True) 
    
    #Removing the working days
    working_day = data[data['workingday'] == 0].index
    data.drop(working_day, inplace = True)
    
    #Removing times before 9 AM and after 6 pm
    time_slot = data[data['hr'] < 9].index
    data.drop(time_slot, inplace = True)
    time_slot = data[data['hr'] > 17].index
    data.drop(time_slot, inplace = True)
    
    #Storing only the weather data related columns in dataframe
    weather_cols = ['temp', 'hum', 'windspeed', 'cnt']
    data = data[weather_cols]
    
    #saving the data
    data.to_csv('filtered.csv', index=False)


# In[87]:


"""
Question 2

Build the model and predict.
"""
    
def build_and_predict():
    from sklearn.model_selection import train_test_split
    
    #Reading the data
    data = pd.read_csv('filtered.csv')
    predict_data = pd.read_csv('topredict.csv')
    
    #Variables
    x = data[['temp', 'hum', 'windspeed']] #Independent
    y = data[['cnt']] #Dependent
    
    #Splitting the data into training & testing
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)
    
    #Preparing & training the model for linear regression
    model = linear_model.LinearRegression()
    model.fit(x_train,y_train)
    
    training_predictions = model.predict(x_train)
    
    final = []
    i = 0
    value = 0
    
    #Loop for saving the predictions in a dataframe
    for each in training_predictions:
        if int(each)>170:
            value = 1
        else:
            value = 0
        temp = [i, value]
        i = i + 1
        final.append(temp)
    final_sol = pd.DataFrame(final, columns = ['index', 'final_prediction'])
    #print(final_sol)
    final_sol.to_csv('predictions.csv')


# In[83]:


# Read-only
filter_bike_data()


# In[84]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# In[85]:


# Read-only
build_and_predict()


# In[ ]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# In[ ]:




