#!/usr/bin/env python
# coding: utf-8

# In[2]:


import iaml01cw2_helpers
import numpy as np


# In[3]:


def preprocessing(Xtrn, Ytrn, Xtst, Ytst):
    Xtrn_orig=Xtrn
    Xtst_orig=Xtst
    Xtrn=Xtrn/255
    Xtst=Xtst/255
    X_mean=np.mean(Xtrn,axis=0)
    X_mean.shape
    Xtrn_nm=Xtrn-X_mean
    Xtst_nm=Xtst-X_mean
    return X_mean, Xtrn_nm, Xtst_nm

