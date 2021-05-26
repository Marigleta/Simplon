#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Case:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self,other):
        return (self.x == other.x) and (self.y == other.y)
    def __str__(self):
        return "Case: x="+str(self.x)+" , y="+str(self.y)
    def __repr__(self):
        return "("+str(self.x)+", "+str(self.y)+")"


# In[2]:


c1 = Case(1,1)
c2 = Case(1,1)
if c1 == c2:
    print("égal")


# In[3]:


class Créature:
    def __init__(self,nom,c):
        self.nom = nom
        self.position = c # c est une Case
    def __str__(self):
        return self.nom+" est sur "+str(self.position)
    def __repr__(self):
        return self.nom+" est sur "+str(self.position)


# In[4]:


# crea = Créature("Griffon",c)
# print(crea)


# In[14]:


class Jeu:
    def __init__(self, listeDesCréatures, dimensions):
        
        self.listeDesCases = []
        
        for i in range(dimensions[0]):
            for j in range(dimensions[1]):
                self.listeDesCases.append(Case(i,j))
                
        self.x = dimensions[0]
        self.y = dimensions[1]
        self.listeDesCréatures = listeDesCréatures
        self.tour = 1
        self.actif = 0 # index du monstre actif dans listeDesCréatures
    def __str__(self):
        s = ""
        for i in self.listeDesCréatures:
            print(i)
        s = "Tour: "+str(self.tour)+" actif: "+str(self.actif)
        return s
    def estOccupée(self,c):
        for i in self.listeDesCréatures:
            if i.position == c:
                return True
        return False
    


# In[12]:


def estOccupée(self,c):
   for i in self.listeDesCréatures:
       if i.position == c:
           return True
   return False


# In[17]:


damier = (4,4) # nb de cases pour le coté du damier
cr1 = Créature("Griffon",Case(1,1)) # positionner sur la case 1,1
cr2 = Créature("Pégase",Case(damier[0],damier[1])) # positionner à l'opposé
l =[cr1,cr2]

j = Jeu(l,damier) # création de l'objet j de type Jeu
print(j)
c=Case(2,2)
print(j.estOccupée(c))


# In[ ]:




