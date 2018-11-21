#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 08:07:14 2018

@author: domi
"""
from sympy import Symbol, exp, log, lambdify
import matplotlib.pyplot as plt 
import numpy as np

Te = Symbol('Te') # Electron temperature in eV
nn = Symbol('nn') # Neutral particles density in 1/m**-3
x = Symbol('x') # Position

# Collision frequency for ionization in 1/s
nu_ioniz = nn*1e-6*exp(-35.3071744514+16.9033721249*log(Te)**1+-7.81316801032*log(Te)**2+2.47737696605*log(Te)**3+-0.62396194653*log(Te)**4+0.145044251711*log(Te)**5+-0.0286523207942*log(Te)**6+0.00352120706732*log(Te)**7+-0.000181868246303*log(Te)**8)
# Collision frequency for elastic collisions between electrons and neutral background in 1/s
nu_en = nn * 1e-6*exp(-16.0325527377+0.412023668827*log(Te)**1+-0.193551110298*log(Te)**2+-0.0247678479005*log(Te)**3+0.0105040269085*log(Te)**4+-0.000152726360717*log(Te)**5+-0.000538801463715*log(Te)**6+9.70545683084e-05*log(Te)**7+-5.10345827257e-06*log(Te)**8)
# Collision frequency for elastic collisions between ions and neutral background in 1/s
nu_in = nn * 1e-15
# External power power source term in eV/m^3 
P_RF = 6e24*exp(-(2e3)*(x-0.045)**2)

# Neutral background density is fixed; unit 1/m^3
nn_val = 1e20

# plot the functions to check
plt.close()
plt.figure(1)
Te_x = np.linspace(0, 25)
nu1 = lambdify([Te, nn], nu_ioniz)
plt.semilogy(Te_x, nu1(Te_x, nn_val), color='red')
nu2 = lambdify([Te, nn], nu_en)
plt.semilogy(Te_x, nu2(Te_x, nn_val), color='blue')
plt.figure(2)
x_x = np.linspace(0, 0.045)
P = lambdify(x, P_RF)
plt.plot(x_x, P(x_x))
plt.show()
