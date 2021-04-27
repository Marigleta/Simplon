#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 1. ecrire une fonction hascap 

def hascap(s) :
    mots = s.split()
    majs = []
    for m in mots:
        if ord(m[0]) in range(65, 91):
            majs.append(m)
    return majs
print(hascap("Il Est venu Le Divine Enfant"))


# In[3]:


# 2. fonction inflation

def inflation(s):
    mots = s.split(" ")
    for count, value in enumerate(mots):
        if value.isnumeric():
            mots[count] = str(int(value)*2)
    new_s = " ".join(mots)
    return new_s
s1 = "Le prix est de 27 euros"
print(inflation(s1))


# In[5]:


#3. fonction lignes

def lignes(s):
    mots = s.split()
    lignes = ['']
    for m in mots:
        m += " "
        if len(lignes[-1])+len(m)<24:
            lignes[-1] += (m)
        else:
            lignes.append(m)
    return lignes
s = "Onze ans déjà que cela passe vite Vous"
s += "vous étiez servis simplement de vos armes la"
s += "mort n'eblouit pas les yeux des partisans Vous"
s += "aviez vos portraits sur les murs de nos villes"
print(lignes(s))


# In[11]:


# 4. programme qui renvoie la liste de tous les nombres

def renvoienombre(s):
    l=findall('-?[0-9]+[.,]?[0-9]*',s)
    print(l)

s="Les 2 maquereaux valent 6.50 euros"
print(s)


# In[15]:


#5. proposer une fonction arrondie

from re import *

des tronc(s):
    motif = r"(-?)([0-9]+)[,.]?[0-9]*"
    return sub(motif,r"\1\2", s)
s = "L'evolution sur 3,5 jours est de 7,23 points"
print(tronc(s))


# In[ ]:




