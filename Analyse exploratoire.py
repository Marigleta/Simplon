#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
fandango=pd.read_csv("fandango_scores.csv")
fandango


# In[5]:


norm_reviews=fandango[["FILM", "RT_user_norm", "Metacritic_user_nom", "IMDB_norm", "Fandango_Ratingvalue", "Fandango_Stars"]]


# In[6]:


norm_reviews.head()


# In[4]:


norm_reviews.isna()


# In[2]:


norm_reviews.head()


# In[6]:


norm_reviews.isna().sum()


# In[7]:


import matplotlib.pyplot as plt
from numpy import arange

fig =plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.show()


# In[8]:


import matplotlib.pyplot as plt
ax.plot(fandango["FILM"], fandango["RT_user_norm"], fandango["Metacritic_user_nom"], fandango["IMDB_norm"], fandango["Fandango_Ratingvalue"], fandango["Fandango_Stars"])
plt.show()
                        


# In[9]:


pyplot.hist[]


# In[ ]:


# graph avec barres


# In[23]:


import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm','Fandango_Ratingvalue', 'Fandango_Stars']
bar_heights = norm_reviews.loc[norm_reviews["FILM"]=='Avengers: Age of Ultron (2015)'][num_cols].values
#print(bar_heights)
#print(bar_heights[0])

bar_positions = np.array([1,2,3,4,5])  # the label locations
width = 0.50  # the width of the bars

rects1 = ax.bar(bar_positions, bar_heights[0], width)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Note moyenne')
ax.set_xlabel('Sources de notation')
ax.set_title('Moyenne des notes utilisateurs pour le film Avengers: Age of Ultron(2015)')
plt.xticks(bar_positions,num_cols, rotation=90)
#ax.set_xticklabels(num_cols) 
ax.legend()


fig.tight_layout()

plt.show()


# In[ ]:


import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm','Fandango_Ratingvalue', 'Fandango_Stars']
bar_heights = norm_reviews.loc[norm_reviews["FILM"]=='Avengers: Age of Ultron (2015)'][num_cols].values
#print(bar_heights)
#print(bar_heights[0])

bar_positions = np.array([1,2,3,4,5])  # the label locations
width = 0.50  # the width of the bars

rects1 = ax.bar(bar_positions, bar_heights[0], width)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Note moyenne')
ax.set_xlabel('Sources de notation')
ax.set_title('Moyenne des notes utilisateurs pour le film Avengers: Age of Ultron(2015)')
plt.xticks(bar_positions,num_cols, rotation=90)
#ax.set_xticklabels(num_cols) 
ax.legend()


fig.tight_layout()

plt.show()


# In[31]:


import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm','Fandango_Ratingvalue', 'Fandango_Stars']
bar_heights = norm_reviews.loc[norm_reviews["FILM"]=='Avengers: Age of Ultron (2015)'][num_cols].values
#print(bar_heights)
#print(bar_heights[0])

bar_positions = np.array([1,2,3,4,5])  # the label locations
width = 0.50  # the width of the bars

rects1 = ax.barh(bar_positions, bar_heights[0], width)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Note moyenne')
ax.set_xlabel('Sources de notation')
ax.set_title('Moyenne des notes utilisateurs pour le film Avengers: Age of Ultron(2015)')
plt.xticks(bar_positions,num_cols, rotation=90)
#ax.set_xticklabels(num_cols) 
ax.legend()


fig.tight_layout()

plt.show()


# In[39]:


import matplotlib.pyplot as plt
import numpy as np

figure_=plt.figure(figsize=[15,10])
ax1=figure_.add_subplot(1,2,1)
ax1.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['RT_user_norm'] )
ax1.set_xlabel( 'Fandango_Ratingvalue ')
ax1.set_ylabel( 'RT_user_norm ')

ax2=figure_.add_subplot(1,2,2, sharey=ax1)
ax2.scatter(norm_reviews['RT_user_norm'], norm_reviews['Fandango_Ratingvalue'] )
ax2.set_xlabel(  'RT_user_norm ')
ax2.set_ylabel( 'Fandango_Ratingvalue')


plt.show()


# In[41]:


import matplotlib.pyplot as plt
import numpy as np


figure_=plt.figure(figsize=[15,10])
ax1=figure_.add_subplot(1,2,1)
ax1.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['RT_user_norm'] )
ax1.set_xlabel( 'Fandango_Ratingvalue ')
ax1.set_ylabel( 'RT_user_norm ')

figure_=plt.figure(figsize=[15,10])
ax1=figure_.add_subplot(1,2,2)
ax1.scatter(fandango['Fandango_Ratingvalue'], fandango['RottenTomatoes'] )
ax1.set_xlabel( 'Fandango ')
ax1.set_ylabel( 'RottenTomatoes')




# In[26]:


#intervertir les axes (question 4)

figure_=plt.figure(figsize=[15,10])
ax1=figure_.add_subplot(1,2,1)
ax1.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['RT_user_norm'] )
ax1.set_xlabel( 'Fandango_Ratingvalue ')
ax1.set_ylabel( 'RT_user_norm ')

ax2=figure_.add_subplot(1,2,2, sharey=ax1)
ax2.scatter(norm_reviews['RT_user_norm'], norm_reviews['Fandango_Ratingvalue'] )
ax2.set_xlabel(  'RT_user_norm ')
ax2.set_ylabel( 'Fandango_Ratingvalue')


plt.show()


# In[27]:


#comparaison des correlations

fig = plt.figure(figsize=(15,10))

ax1 = fig.add_subplot(3,3,1)
ax2 = fig.add_subplot(3,3,2)
ax3 = fig.add_subplot(3,3,3)

ax1.scatter(fandango["Fandango_Ratingvalue"], fandango["RT_user_norm"],color="red")
ax1.set_xlabel("Fandango")
ax1.set_ylabel("RottenTomatoes")
ax1.set_xlim(0,5)

ax2.scatter(fandango["Fandango_Ratingvalue"], fandango["Metacritic_user_nom"],color="green")
ax2.set_xlabel("Fandango")
ax2.set_ylabel("Metacritic")
ax2.set_xlim(0,5)

ax3.scatter(fandango["Fandango_Ratingvalue"],fandango["IMDB_norm"],color="blue")
ax3.set_xlabel("Fandango")
ax3.set_ylabel("IMDB")
ax3.set_xlim(0,5)

plt.show()


# comparaison des correlations: de ces graphs nous pouvons deduire que la correlation des evaluations entre 
# fandango et rotten tomatoes est la plus forte.

# In[28]:


# comparaison des histogrammes
fig=plt.figure('fig')
ax1=fig.add_subplot(2,2,1)
ax2=fig.add_subplot(2,2,2)
ax3=fig.add_subplot(2,2,3)
ax4=fig.add_subplot(2,2,4)

ax1.hist(norm_reviews['Fandango_Ratingvalue'],bins=20,range=(0,5))

ax2.hist(norm_reviews['RT_user_norm'],bins=20,range=(0,5))

ax3.hist(norm_reviews['Metacritic_user_nom'],bins=20,range=(0,5))

ax4.hist(norm_reviews['IMDB_norm'],bins=20,range=(0,5))

ax4.set_ylim(0,50)
ax3.set_ylim(0,50)
ax2.set_ylim(0,50)
ax1.set_ylim(0,50)

ax1.set_title('Fandango_Ratingvalue')
ax2.set_title('RT_user_norm')
ax3.set_title('Metacritic_user_nom')
ax4.set_title('IMDB_norm')

fig.subplots_adjust(wspace=None,hspace=0.5)

plt.show


# dans ces graphs, on remarque des ressemblances entre les evaluation que nous pouvons trouver dans ces
# differents sites: les piques pour les quatres sites se situent autour de "quatre".
# 

# In[29]:


#diagrames à boites

import matplotlib.pyplot as plt

num_cols=['RT_user_norm','Metacritic_user_nom','IMDB_norm','Fandango_Ratingvalue']
fig.ax = plt.subplots
plt.boxplot(norm_reviews[num_cols])
ax.set_xticklabels(num_cols, rotation=90)
ax.set_ylim(0,50)

plt.show()


# # nous pouvons voir de ce graph que les reviews dans le cas de la colonne 'RT_user_norm' de 2,5 jusqu'à 4, 
# #ce qui est le cas des autres websites

# In[ ]:




