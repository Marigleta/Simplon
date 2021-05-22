#!/usr/bin/env python
# coding: utf-8

# mot= "alphonse"
# 
# s= "alphons et alponse sont de retour"
# 
# occurrences = "alphons", "alponse"
# 

# In[7]:


def comb(mot):
    combinaisons = []
    for i in range(len(mot)):
        combinaisons.append(mot[:i]+mot[i+1:])
    return combinaisons


# In[18]:


def almost(mot, s):
    occurrences = []
    mots = s.split()
    combinaisons = comb(mot)
    for i in mots:
        #mot trouvé:
        if i in combinaisons:
            occurrences.append(i)
    return occurrences


# In[19]:


if __name__ == "__main__":
    s = "alphons et alponse avec lphonse sont de retour"
    x = almost("alphonse",s)
combinaisons = comb("alphonse") 
print(combinaisons)


# In[ ]:


import math

def comb(mot):
    combinaisons = []
    for i in range(len(mot)):
        combinaisons.append(mot[:i]+mot[i+1:])
    return combinaisons

def almost(mot, s):
    occurrences = []
    mots = s.split()
    combinaisons = comb(mot)
    for i in mots:
        #mot trouvé:
        if i in combinaisons:
            occurrences.append(i)
    return occurrences

def lettre_ajoutee(mot, s):
    occurrences = []
    mots = s.split()
    for i in mots:
        #mot trouvé:
        combinaisons = comb(i)
        if mot in combinaisons:
            occurrences.append(i)
    return occurrences

def lettre_remplacee(mot, s):
    occurrences = []
    mots = s.split()
    combinaisons_mot = comb(mot)
    for i in mots:
        #mot trouvé:
        combinaisons = comb(i)
        for combi in combinaisons_mot:
            if combi in combinaisons:
                occurrences.append(i)
                break
    return occurrences

def pluslarge(mot, s):
    lett_enlevee = almost(mot,s)
    lett_ajoutee = lettre_ajoutee(mot, s)
    lett_remplacee = lettre_remplacee(mot, s)

    return lett_enlevee + lett_ajoutee + lett_remplacee

def sum(a,b):
	x = a+b
	return x

if __name__ == "__main__":
    #s = "alphons et alponse avec lphonse sont de retour"
    #x = almost("alphonse",s)

    #s = "maman et manma avec amama sont de retour mam maa"
    #x = lettre_ajoutee("mama",s)

    s = "maman manma mada et lama et mamb sont de retour et mam maa"
    x = pluslarge("mama",s)

    print(x)
    #print(comb("hello"))
    #print(s)
    #print(s.split())
    #print(x)
    #mot = "alphonse"
    #print(mot)

    #combinaisons = comb("alphonse") 
    #print(combinaisons)


# In[4]:


def score(p,s):
    score = 0

    s = s.replace(",","")
    s = s.replace(".","")

    p = p.replace(",","")
    p = p.replace(".","")

    p_liste = p.split()

    for word in p_liste:
        
        
        liste_found = pluslarge(word,s)

        for words in liste_found:
            if words == word:

                score += 5
            else:
                score += 1
    return score



print(score(phrase,search))
#print(score(mot,s))


# In[5]:


def score(p, s):
    sc = 0
    q = " "+sub("[,.]","", p)+" "
    z = " " + sub("[,.]","", s)
    for x in p.split():
        sc += len(pluslarge(x, s))
        sc += 4*z.count(" "+x+" ")
    return sc
p="Le petit bonhomme en mousse"
t = "Ce superbe matelas en mousse naturelle"
print(score("les trois gros", s))
print(score(p, t))


# In[ ]:




