#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""


#%%

import numpy as np

#%%

sum1 = np.sum(np.arange(1, 101) ** 2)
sum2 = np.sum(np.arange(1, 101)) ** 2

print("Difference: {}".format(np.abs(sum1 - sum2)))
