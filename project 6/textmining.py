
# coding: utf-8

# ## There are some instructions you need to follow:
# <li> You only need to write your code in the comment area "Your Code Here".</li>
# <li>Do not upload your own file. Please make the necessary changes in the Jupyter notebook file already present in the server.</li>
# <li>Please note, there are several cells in the Assignment Jupyter notebook that are empty and read only. Do not attempt to remove them or   edit them. They are used in grading your notebook. Doing so might lead to 0 points.</li>

# In[2]:


import nltk
import os
import _sqlite3
from nltk.corpus import PlaintextCorpusReader
from nltk import sent_tokenize,word_tokenize 
from gensim import corpora, models, similarities
from gensim.models.ldamodel import LdaModel
from gensim.parsing.preprocessing import STOPWORDS
from gensim.similarities.docsim import Similarity


# # Question 1

# In[3]:


"""
Question 1

Write a function that takes the file name of the Wikipedia page containing all Greek ancient
philosophers (saved as "Index.html" in your workspace) and returns a list tuples containing 
the name of the philosopher and the path to its individual article file.

Example of use: get_philosophers("Index.html")

The output should be a list of tuples:

[('Acrion', 'Philosophers/Acrion.html'),
 ('Adrastus of Aphrodisias', 'Philosophers/Adrastus of Aphrodisias.html'),
 ('Aedesia', 'Philosophers/Aedesia.html'),
 ('Aedesius', 'Philosophers/Aedesius.html'),
 ('Aeneas of Gaza', 'Philosophers/Aeneas of Gaza.html'),
 ('Aenesidemus', 'Philosophers/Aenesidemus.html'),
 ...]
 
  
NOTE: For processing speed purposes, the table in "Index.html" has been shortened compared
to the one online on wikipedia.org. Do not worry if you do not find some philosophers in 
your results, this is made on purpose. 

"""

def get_philosophers(filename):
    
    import codecs
    from bs4 import BeautifulSoup
    f = codecs.open(filename, 'r', 'utf-8')
    soup = BeautifulSoup(f.read(),'lxml')
    table = soup.find('table', class_='wikitable sortable').find('tbody')
    i=0
    phil_list = []
    name = ''
    link = ''
    for philosophers in table.find_all('tr'):
        try:
            if i != 0:
                name = philosophers.find('a').get('title')
                link = 'Philosophers/'+name+'.html'
                final = (name, link)
                phil_list.append(final)
            i = 1
        except:
            continue
    return phil_list

# Once done, try this:
filenames = get_philosophers("Index.html")
filenames


# # Question 2

# In[9]:


"""
Question 2


Write a function that scrapes the text on a philosophers’s page and returns it as a text 
string. The input is the name of the file that contains the philosoph's page.

Example of use: get_text('Philosophers/Acrion.html')
should output the text of the page.
'Acrion was a Locrian and a Pythagorean philosopher...'
"""

def get_text(file):
    
    import codecs
    from bs4 import BeautifulSoup
    f = codecs.open(file, 'r', 'utf-8')
    soup = BeautifulSoup(f.read(),'lxml')
    text_string = ''
    for each in soup.find_all('p'):
        text_string += each.get_text()
    return text_string

# Once done, try this:
get_text("Philosophers/Acrion.html")


# # Question 3

# In[10]:


"""
Question 3

Use the files under "Philosophers" folder to construct an LSI model.
Then, use the LSI model to find the most similar philosopher for each of the philosophers
found in Question 1, based on the content of their Wikipedia articles. You should not go
online to scrape the data; everything you need is in your Jupyter notebook working directory.

The function should have as input the list of tuples created in Question 1.

The output format should be a list of tuples too. Each tuple should contain a philosopher's name
and its most similar other philosopher. Please note both names can't be the same.

The output should look like that:

[('Acrion', 'Athenodoros Cananites'),
 ('Adrastus of Aphrodisias', 'Andronicus of Rhodes'),
 ('Aedesia', 'Ammonius of Athens'),
 ('Aedesius', 'Arete of Cyrene'),
 ('Aeneas of Gaza', 'Ammonius Hermiae'),
 ...]


"""

def run(filenames):
    
    doc_list = []
    all_text = ''
    documents = []
    for i in filenames:
        doc_list.append(i[1])
        all_text = all_text + get_text(i[1])
        documents.append(get_text(i[1]))
    
    texts = [[word for word in document.lower().split()
            if word not in STOPWORDS and word.isalnum()]
            for document in documents]
    
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    
    lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=10) #Actual model with topics as 10
    
    final_list = [] # To store values
    
    i=0
    for doc in documents:
        #print(doc)
        vec_bow = dictionary.doc2bow(doc.lower().split())
        vec_lsi = lsi[vec_bow]
        index = similarities.MatrixSimilarity(lsi[corpus])
        sims = index[vec_lsi]
        sims = sorted(enumerate(sims), key=lambda item: -item[1])
        similar = sims[1] #Highest probability
        authors = doc_list[documents.index(doc)].replace('Philosophers/','').replace('.html','') #Phil of each for loop
        similar_authors = doc_list[similar[0]].replace('Philosophers/','').replace('.html','') #Similar phil
        combined = (authors, similar_authors) #tuple
        print(combined)
        final_list.append(combined) #Adding tuple to the list
        i = i + 1
        
    return final_list
# Once done, try this:
run(filenames)


# In[ ]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# In[144]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# In[145]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# In[ ]:





# In[ ]:




