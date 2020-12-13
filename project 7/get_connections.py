
# coding: utf-8

# ## There are some instructions you need to follow:
# <li> You only need to write your code in the comment area "Your Code Here".</li>
# <li>Do not upload your own file. Please make the necessary changes in the Jupyter notebook file already present in the server.</li>
# <li>Please note, there are several cells in the Assignment Jupyter notebook that are empty and read only. Do not attempt to remove them or   edit them. They are used in grading your notebook. Doing so might lead to 0 points.</li>

# In[1]:


"""
Modify the following get_max_neighbor function so that it takes a network and a node as
arguments, and  returns a list containing the name of the neighboring station with most 
trips and the number of trips.

Example of use:
get_max_neighbor(G,'Newport Pkwy')
should return the following list:

['Lafayette Park', 74]

"""

#Here's the grph to look at-
# import networkx as nx
# G = nx.Graph()
# nodes = ['Newport Pkwy', 'Lafayette Park', 'JCBS Depot', 'Fairmount Ave',
#          'Liberty Light Rail', 'Jackson Square', 'City Hall', 'Sip Ave']
# edges = [('Newport Pkwy', 'Lafayette Park', {'count': 74}),
#          ('Newport Pkwy', 'JCBS Depot', {'count': 50}),
#          ('Newport Pkwy', 'Liberty Light Rail', {'count': 11}),
#          ('Lafayette Park', 'Fairmount Ave', {'count': 97}),
#          ('Lafayette Park', 'Sip Ave', {'count': 87}),
#          ('JCBS Depot', 'Sip Ave', {'count': 69}),
#          ('JCBS Depot', 'City Hall', {'count': 6}),
#          ('JCBS Depot', 'Fairmount Ave', {'count': 71}),
#          ('JCBS Depot', 'Liberty Light Rail', {'count': 4}),
#          ('Fairmount Ave', 'Liberty Light Rail', {'count': 2}),
#          ('Liberty Light Rail', 'Jackson Square', {'count': 59}),
#          ('Liberty Light Rail', 'City Hall', {'count': 52}),
#          ('Jackson Square', 'City Hall', {'count': 38})]
# G.add_nodes_from(nodes)
# G.add_edges_from(edges)

def get_max_neighbor(graph,node):
    c = 0
    value = ''
    final = []
    for each in G.edges(nbunch=node,data=True):
        if each[2]['count'] > c:
            c = each[2]['count']
            value = each[1]
    final.append(value)
    final.append(c)
    return final


# In[2]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# In[3]:


###
### AUTOGRADER TEST - DO NOT REMOVE
###


# In[ ]:




