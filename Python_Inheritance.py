#!/usr/bin/env python
# coding: utf-8

# ## inheritance

# In[1]:


class BitkiTurleri():
    def __init__(self):
        print("Burası BitkiTurleri init fonksiyonundan gelmektedir.")
    def Meyveler(self):
        print("Meyve türleri buradan gelmektedir.")
    def Sebzeler(self):
        print("Sebze türleri buradan gelmektedir.")


# In[2]:


class Domates(BitkiTurleri):
    def __init__(self):
        BitkiTurleri.__init__(self)
        print("BitkiTurleri sınıfından init fonksiyonu çağrıldı.")


# In[3]:


domates = Domates()


# In[ ]:




