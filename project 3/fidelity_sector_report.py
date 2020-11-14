
# coding: utf-8

# ## There are some instructions you need to follow:
# <li> You only need to write your code in the comment area "Your Code Here".</li>
# <li>Do not upload your own file. Please make the necessary changes in the Jupyter notebook file already present in the server.</li>
# <li>Please note, there are several cells in the Assignment Jupyter notebook that are empty and read only. Do not attempt to remove them or   edit them. They are used in grading your notebook. Doing so might lead to 0 points.</li>

# In[ ]:


"""

Check the following pages to inspect the structure of the site (right click -> inspect):
1. https://eresearch.fidelity.com/eresearch/goto/markets_sectors/landing.jhtml 
2. https://eresearch.fidelity.com/eresearch/markets_sectors/sectors/sectors_in_market.jhtml?tab=learn&sector=50 

Modify the following fidelity_sector_report so that it returns a json dump
(same structure as a dictionary, except for the quotation marks) that contains the 
following information about each sector:
1. The sector name
2. The enterprise value (in USD billions)
3. The Return on Equity TTM (trailing twelve months, in percentages)
4. The dividend yield (in percentages)

The structure of the json dump is given in the assignment description on EdX.

You should expect outputs like following for the first 3 sectors:
{'results': {'Communication Services': {'enterprise_value': 286.81,
   'return_on_equity': 15.82,
   'dividend_yield': 3.91},
  'Consumer Discretionary': {'enterprise_value': 279.53,
   'return_on_equity': -293.98,
   'dividend_yield': 2.32},
  'Consumer Staples': {'enterprise_value': 164.55,
   'return_on_equity': -5.36,
   'dividend_yield': 2.75}}}

Note:
To read files, use:

with open('filename') as f:
    lines = f.readlines()
"""

# do not change anything that is originally written in here
# write the solution in suggested area


# In[6]:


# Run this cell and do not change it
with open('Sector Performance.htm') as f:
    file1 = f.readlines()
from bs4 import BeautifulSoup
BeautifulSoup("".join(file1), "lxml")


# In[7]:


def fidelity_sector_report(file1):
    ref_json = dict()
    import requests
    from bs4 import BeautifulSoup
    result = BeautifulSoup("".join(file1),"lxml")
    main_div = result.find('div', class_="performance-section")
    sub_div = main_div.find_all('div', class_="heading")
    dict1 = dict()
    dict2 = dict()
    for perf in main_div.find_all('div', class_="heading"):
        sector = perf.get_text().strip() + '.htm'
        dict1[perf.get_text()] = sectorwise_metrics(sector)
    ref_json['results'] = dict1
    return ref_json


# In[8]:


def sectorwise_metrics(sector):
    metric = dict()
    
    import requests
    from bs4 import BeautifulSoup
    
    with open(sector) as f1:
        file2 = f1.readlines()
    result = BeautifulSoup("".join(file2),"lxml")
    main_div = result.find('div', class_="sec-fundamentals")
    table = main_div.find('table').find('tbody')
    for met in main_div.find_all('th', class_="align-left"):
        if met.get_text() in 'Enterprise Value':
            metric['enterprise_value'] = float(table.find_all("td")[2].get_text().replace('\n','').replace('\t','').strip()[1:-1])
            continue
        elif met.get_text() in 'Return on Equity (TTM)':
            metric['return_on_equity'] = float(table.find_all("td")[6].get_text().replace('\n','').replace('\t','').strip()[:-1])
            continue
        elif met.get_text() in 'Dividend Yield':
            metric['dividend_yield'] = float(table.find_all("td")[9].get_text().replace('\n','').replace('\t','').strip()[:-1])
            break

    return metric


# In[9]:


fidelity_sector_report(file1)


# # Please answer the second part below!

# In[10]:


# If you were to invest in the highest ROE (return on equity) sector, that would be:
highest_roe_sector = "Information Technology" #e.g. "Utilities"

# If you were to invest in the highest dividend yield sector, that would be:
highest_dividend_sector = "Energy" #e.g. "Materials"

# CHANGE THE ABOVE STRINGS, DO NOT PUT SOLUTION BELOW THE FOLLOWING TAG
###
### YOUR CODE HERE
###


# In[ ]:


# Run this cell to get a grade!
###
### AUTOGRADER TEST - DO NOT REMOVE
###


# In[ ]:


# Run this cell to get a grade!
###
### AUTOGRADER TEST - DO NOT REMOVE
###


# In[ ]:


# Run this cell to get a grade!
###
### AUTOGRADER TEST - DO NOT REMOVE
###


# In[ ]:


# Run this cell to get a grade!
###
### AUTOGRADER TEST - DO NOT REMOVE
###


# In[ ]:


# Run this cell to get a grade!
###
### AUTOGRADER TEST - DO NOT REMOVE
###


# In[ ]:


# Run this cell to get a grade!
###
### AUTOGRADER TEST - DO NOT REMOVE
###

