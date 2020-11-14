
# coding: utf-8

# ## There are some instructions you need to follow:
# <li> You only need to write your code in the comment area "Your Code Here".</li>
# <li>Do not upload your own file. Please make the necessary changes in the Jupyter notebook file already present in the server.</li>
# <li>Please note, there are several cells in the Assignment Jupyter notebook that are empty and read only. Do not attempt to remove them or   edit them. They are used in grading your notebook. Doing so might lead to 0 points.</li>
# <li>Do not use python input function (e.g. word = input("Enter a word: ") ). Use parameters in your self-defined function otherwise it code will not pass the grader</li>

# In[ ]:


"""
Modify the following reverse function so that where the first occurrence of 
reverse_word in sentence is replaced by the same word but spelled backwards.

Tests:

reverse("Python improves my mood very much", "mood") should return "Python improves my doom very much"

reverse("We are reaching the next level", "level") should return "We are reaching the next level"
"""
 
def reverse(sentence, reverse_word):
  """start_index = index of the reverse word in the sentence
     return sliced string till the start index + reversed word + remaining sentence
  """
  return (sentence[0:sentence.find(reverse_word)]+reverse_word[::-1]+sentence[sentence.find(reverse_word)+len(reverse_word):])
    


# In[ ]:


reverse("The end is near", "end")


# In[ ]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# In[ ]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# In[ ]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###

