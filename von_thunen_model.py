# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 09:58:58 2022

@author: leore
"""

import math as m
"""Soit i la production d'une unité de bien agricole"""
Ai=5 #unités de sols dont nécessite production de bien agricole
r=20 #distance entre ville et culture du bien agricole
t=2 #coût de transport par unité de distance et de poids, en unités monétaire
Pi=50 #prix auquel le B agricole est écoulé une fois arrivé en ville
Rm=Pi/Ai #rendement monétaire d'une unité de sol
def Si(r):
    return (Pi - t*r)/Ai
print("Le surplus agricole par unité de surface est :", Si(r))
print("Le rendement monétaire d'une unité de sol est :", Rm)
"""Attention, t*r représente le coût de transport x la distance à la ville,
il ne doit donc pas excéder le prix de revente car l agriculteur ne vend pas a perte"""