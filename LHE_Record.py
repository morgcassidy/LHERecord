#!/usr/bin/env python
# coding: utf-8

# ## Import Packages

# In[1]:


import ROOT 
import pylhe
import math
import matplotlib.pyplot as plt
import numpy as np


# ## Define Mass Function

# In[ ]:


def invariant_mass(p1,p2):
    return math.sqrt(sum((1 if index=='e' else -1)*(getattr(p1,index)+getattr(p2,index))**2 for index in ['e','px','py','pz']))
def transvers_mass(p1):
    return math.sqrt(sum((1 if index=='e' else -1)*(getattr(p1,index))**2 for index in ['e','pz']))


# ## Create a Event List and Mass List

# In[ ]:


process_path_MZ_1500 = '/root/MG5_aMC_v2_7_2/sig_schannel/Events/run_01/unweighted_events.lhe' 

sig_schannel_MZ_1500 = pylhe.readLHE(process_path_MZ_1500)

m, mT, event_list = [], [], []

for event in sig_schannel_MZ_1500:
    m.append(invariant_mass(event.particles[-1],event.particles[-2]))
    mT.append(transvers_mass(event.particles[-3]))
    event_list.append(event)
    
m, mT = np.array(m), np.array(mT)


# ## Check variables stored in particle

# In[ ]:


dir(event_list[0].particles[0]) 


# ## Print Information for First Event

# In[ ]:


print("{:^12}{:^9}{:^12}{:^12}{:^12}{:^12}{:^12}{:^12}{:^12}".format("#","id","mother1","mother2","e","px","py","pz","status"))

for i, element in  enumerate(event_list[0].particles):
    print("{:^12}{:^9.0f}{:^12.0f}{:^12.0f}{:^12.3f}{:^12.3f}{:^12.3f}{:^12.3f}{:^12.0f}".format(i, element.id,element.mother1,element.mother2,element.e,element.px,element.py,element.pz,element.status))



# In[ ]:


[i.event for i in event_list[0].particles]


# In[10]:


[i.status for i in event_list[0].particles] #particle status for first event (Parton level)


# In[87]:


[i.mothers for i in event_list[0].particles] #particle id for first event (Parton level)


# ## Make a Plot for $M_{xd, \bar{xd}}$

# In[56]:


plt.figure(figsize=(8,8)) # plotsize

bin_size = np.linspace(800,2000,121)
hist, bins = np.histogram(m, bins=bin_size)
plt.step(bins[:-1], hist.astype(np.float32)/10,color = "green", where='mid',linewidth=2, alpha=0.7,label="$M_{xd,\\bar{xd}}$") 

plt.legend(bbox_to_anchor=(1, 1),ncol=2,fontsize=20) # plot label tag
plt.yscale('log') 
plt.xlabel("$M_{xd,\\bar{xd}}$ [GeV]" , fontsize=20, horizontalalignment='right',x=1)  # plot x-axis label
plt.ylabel("dN/d$M_{xd,\\bar{xd}}$", fontsize=20, horizontalalignment='right',y=1)  # plot y-axis label
plt.xticks(fontsize=15)   # set x-ticks size
plt.yticks(fontsize=15)   # set y-ticks size 
# plt.savefig("./invariant_mass_SVJ.png")  #save figure as png
plt.show()


# In[ ]:




