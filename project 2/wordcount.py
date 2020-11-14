
# coding: utf-8

# ## There are some instructions you need to follow:
# 
# <li> You only need to write your code in the comment area "Your Code Here".
# <li> Do not upload your own file. Please make the necessary changes in the Jupyter notebook file already present in the server.
# <li> Please note, there are several cells in the Assignment Jupyter notebook that are empty and read only. Do not attempt to remove them or edit them. They are used in grading your notebook. Doing so might lead to 0 points

# In[4]:


"""
Modify the following word_distribution function so that
it returns a dictionary with the count of each word in 
the input string.

Don't forget to put the words in lowercase.

If there's a punctuation sign at the end of a word, you should remove it.
You should remove only one punctuation sign if there are multiple signs.

Tests:

word_distribution("Hello. How are you? Please say hello if you don’t love me!") 
should return {‘hello’: 2, ‘how’:1, ‘are’:1, ‘you’:2, ’please’:1, “don’t”: 1, 'say':1, 'if':1, 'love':1,'me':1}

word_distribution("That's when I saw Jane (John's sister)!")
should return {"that's":1, "when":1,"i":1,"saw":1,"jane":1, "(john's":1, "sister)":1}
"""


# In[3]:


def word_distribution(s):
  word = s.split()
  punctuations = '''!-;:'"\,<>./?@#$%^&*_~'''
  word_dict = {}
  for i in word:
    if i[0] in punctuations:
      i = i[1:]
    if i[-1] in punctuations:
      i = i[:-1]
    i = i.lower()
    if i not in word_dict:
      word_dict.update({i:1})
    else:
      word_dict[i] = word_dict.get(i) + 1
  return word_dict


# In[4]:


#testing
word_distribution("Monica is coming to the city tomorrow!")
word_distribution("That's when I saw Jane (John's sister)!")
word_distribution("Why are all these people here?")


# In[5]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# In[6]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# In[ ]:





# In[ ]:




