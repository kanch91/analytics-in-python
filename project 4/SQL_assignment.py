
# coding: utf-8

# ## There are some instructions you need to follow:
# <li> You only need to write your code in the comment area "Your Code Here".</li>
# <li>Do not upload your own file. Please make the necessary changes in the Jupyter notebook file already present in the server.</li>
# <li>Please note, there are several cells in the Assignment Jupyter notebook that are empty and read only. Do not       attempt to remove them or   edit them. They are used in grading your notebook. Doing so might lead to 0 points.</li>
# <li>IMPORTANT: You only need to use SQL for the entire assignment. Please don't use Python anywhere for the assignment. </li>
# <li> Write the SQL code code in the MySQL workbench and then copy the queries in the notebook. </li>

# 
# 
# For the following questions, you need to create two database tables and their respective columns:
# 1. exhibits: id (INT), name (VARCHAR), start_date (DATE), end_date (DATE), curator_id 
# 2. curators: id (INT), name (VARCHAR), bio (TEXT)
# 
# You then need to insert all the records into the database tables as shown below:
# 
# - table name: `exhibits`
# 
# id (INT) | name (VARCHAR) | start_date (DATE) | end_date (DATE) | curator_id (INT) [FK to curator.id]
# -|-|-|-|-
# 3| Free The Fishes | 2018-01-01 | 2018-06-30 | 5
# 17| Space, What Lies Above | 2018-02-01 | 2018-05-30 | 11
# 23| Bears Bears Bears | 2018-02-14 | 2018-02-24 | 5
# 46| Humans? Aliens? | 2019-03-14 | 2019-10-21 | 11
# 
# 
# - table name: `curators`
# 
# id (INT) | name (VARCHAR) | bio (TEXT)
# -|-|-
# 5| Rebecca Votea | Esteemed naturalist
# 11| Simon Strauss | Space man
# 71| Rick Sanchez | Grandfather
# 
# 
# SQL solutions will be graded on their simplicity as well as on whether or not they would return the correct answer from the database.

# **Q1**: Write a function that returns a string containing the SQL necessary to create the two tables shown above.
# 

# In[5]:


def create_tables_sql() -> str:
    string = 'CREATE TABLE curators (id int NOT NULL, name varchar(30), bio TEXT);' + 'CREATE TABLE exhibits (id int NOT NULL, name varchar(30), start_date DATE, end_date DATE, curator_id int);'
    return (string)


# In[6]:


### # Run this cell to get a grade!
###
### AUTOGRADER TEST - DO NOT REMOVE
###


# **Q2**: Write a function that returns a string containing the SQL necessary to insert the data exactly as it is shown above.
# 
# Hint: Use INSERT into statement

# In[ ]:


def insert_data_sql() -> str:
    string = 'INSERT into curators VALUES ("5", "Rebecca Votea", "Esteemed naturalist"), ("11", "Simon Strauss", "Space man"), ("71", "Rick Sanchez", "Grandfather");'+'INSERT into exhibits VALUES ("3", "Free The Fishes", "2018-01-01", "2018-06-30", "5"), ("17", "Space, What Lies Above", "2018-02-01", "2018-05-30", "11"), ("23", "Bears Bears Bears", "2018-02-14", "2018-02-24", "5"), ("46", "Humans? Aliens?", "2019-03-14", "2019-10-21", "11");'
    return (string)


# In[ ]:


### # Run this cell to get a grade!
###
### AUTOGRADER TEST - DO NOT REMOVE
###


# In[ ]:


### # Run this cell to get a grade!
###
### AUTOGRADER TEST - DO NOT REMOVE
###


# **Q3**: Create a function that will return the SQL to find all the names of all the exhibits ordered by their id. IDs should be in descending order. Do not use an alias for the table name.
# 
# The result should be:
# 
# ```
# Humans? Aliens?
# Bears Bears Bears
# Space, What Lies Above
# Free The Fishes
# ```

# In[ ]:


def get_sql():
    string = 'SELECT name FROM exhibits ORDER BY id DESC;'
    return (string)


# In[ ]:


# Run this cell to get a grade!
###
### AUTOGRADER TEST - DO NOT REMOVE
###


# **Q4**: Create a function that will return the SQL to find all the names of all exhibts and the names of their associated curators. If an exhibit does not have a curator, the exhibit should not be in the result. Even if a curator does not have an exhibit, the curator should be present in the final result. The first letter of the table name should be used as its alias.
# 
# For example:
# 
# ```
# Rebecca Votea, Free The Fishes
# Rebecca Votea, Bears Bears Bears
# Rick Sanchez, 
# Simon Strauss, Humans? Aliens?
# Simon Strauss, Space, What Lies Above
# 
# ```

# In[ ]:


def get_sql():
    string = 'SELECT c.name, e.name FROM curators c LEFT JOIN exhibits e ON c.id = e.curator_id ORDER BY c.name, length(e.name);'
    return (string)


# In[ ]:


# Run this cell to get a grade!
###
### AUTOGRADER TEST - DO NOT REMOVE
###


# In[ ]:





# In[ ]:




