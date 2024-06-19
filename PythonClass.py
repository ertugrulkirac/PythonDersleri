#!/usr/bin/env python
# coding: utf-8

# In[7]:


class Ogrenci():
    def __init__(self, ad, soyad, ogrenciNo):
        self.ad = ad
        self.soyad = soyad
        self.ogrenciNo = ogrenciNo


# In[8]:


ogrenci = Ogrenci("Ertuğrul", "Kıraç", 2317)


# In[9]:


ogrenci.ad


# In[10]:


ogrenci.soyad


# In[11]:


ogrenci.ogrenciNo


# In[27]:


class Islemler():
    def __init__(self, sayi1, sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2
    def toplama(self):
        return self.sayi1 + self.sayi2
    def cikarma(self):
        return self.sayi1 - self.sayi2
    def carpma(self):
        return self.sayi1 * self.sayi2
    def bolme(self):
        return self.sayi1 / self.sayi2


# In[33]:


islemler = Islemler(13,5)
print(f"Toplama işleminin sonucu:{islemler.toplama()}")
print(f"Çıkarma işleminin sonucu: {islemler.cikarma()}")
print(f"Çarpma işleminin sonucu:{islemler.carpma()}")
print(f"Bölme işleminin sonucu: {islemler.bolme()}")


# In[ ]:





# In[ ]:




