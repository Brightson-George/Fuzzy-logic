# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 01:05:25 2021

@author: brigh
"""

import numpy as np
import fuzzylab as fuzzy
from matplotlib.pyplot import *
import matplotlib.pyplot as plt

num = int(10 / 0.5)
# service = np.linspace(0, 10, num + 1)
# food = np.linspace(0, 10, num + 1)
service = np.arange(0, 10.1, 0.5)
service = np.expand_dims(service, 0);
food = np.arange(0, 10.1, 0.5)
food = np.expand_dims(food, 0)

servRatio = 0.8

S, F = np.meshgrid(service, food)
# tip = (servRatio * ((0.20 / 10) * S + 0.05)) + ((1 - servRatio) * ((0.20 / 10) * F + 0.05)) 
# tip = tip.reshape((1, len(tip)))
tip = np.zeros(S.shape)
# tip = np.array([[(0.10/3) * S[i, j] + 0.05] if S[i, j] < 3 else [tip[i, j]] for i in range(len(service[0])) for j in range(len(service[0])) ])
# tip = np.array([[0.15] if S[i, j] >= 3 and S[i, j] < 7 else [tip[i, j]] for i in range(len(service[0])) for j in range(len(service[0]))])
# tip = np.array([[(0.10/3) * (S[i, j] - 7) + 0.15] if S[i, j] >=7 and S[i, j] <= 10 else [tip[i, j]] for i in range(len(service[0])) for j in range(len(service[0]))])
# tip = np.array(tip[0])
tip = np.where((S < 3), ((0.10/3) * S + servRatio + (1 - servRatio) * (0.20 / 10) * F + 0.05), tip)
tip = np.where((S >= 3) & (S < 7), servRatio * 0.15 + (1 - servRatio) * (0.20 / 10 * F + 0.05), tip)
tip = np.where((S >= 7) & (S <= 10), ((0.10/3) * (S-7) + 0.15) * servRatio + (1 - servRatio) * (0.20 / 10 * F + 0.05), tip)

fig = plt.figure()
# ax = fig.add_subplot(1, 2, 2, aspect='equal')
ax = fig.gca(projection='3d')
ax.set_xlabel('service')
ax.set_ylabel('food')

ax.plot_surface(S, F, tip, cmap=cm.coolwarm)
ax.azim = 0
ax.elev = 0
# plot((service, food), tip)
# xlabel('service')
# ylabel('tip')
# ylim((0.05, 0.25))
# xlim((0, 10))