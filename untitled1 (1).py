# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1q60ehXRsBF9E2Ipec39PPEB5EdBChxgB
"""

import matplotlib.pyplot as plt
celsius = [[-67.0],[-34.0],[0],[34.0],[54.0],[67.0],[100]]
fahrenheit = [[-88.6],[-29.2],[32.0],[93.2],[129.2],[152.6],[212.0]]
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(celsius, fahrenheit)
lr.predict([[256],[123]])
lr.coef_
lr.intercept_
celsius_test = [[-50],[10],[30],[20],[10],[70],[87]]
fahrenheit_test = lr.predict(celsius_test)
fahrenheit_test
for c,f in zip(celsius_test, fahrenheit_test):
  print(f'цельсия {c} фаренгейта {f}')
import numpy as np
x_range = np.arange(70,120)
y_range = x_range*1.8+32
plt.figure(figsize=(15,8), dpi=280)
plt.plot(x_range, y_range, label='уравнение', linewidth='1')
plt.scatter(celsius, fahrenheit, label='входные данные', color='green')
plt.scatter(celsius_test, fahrenheit_test, label='предсказанное значение', color='blue')
plt.xlabel('Цельсия')
plt.ylabel('Фаренгейта')
plt.legend()
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
kelvin = [[-67.0],[-34.0],[0],[34.0],[54.0],[67.0],[100]]
fahrenheit = [[-88.6],[-29.2],[32.0],[93.2],[129.2],[152.6],[212.0]]
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(kelvin, fahrenheit)
lr.predict([[256],[123]])
lr.coef_
lr.intercept_
kelvin_test = [[-50],[10],[30],[20],[10],[70],[87]]
fahrenheit_test = lr.predict(celsius_test)
fahrenheit_test
for k,f in zip(kelvin_test, fahrenheit_test):
  print(f'кельвина {k} фаренгейта {f}')
import numpy as np
x_range = np.arange(70,120)
y_range = x_range+459.67*5/9
plt.figure(figsize=(15,8), dpi=280)
plt.plot(x_range, y_range, label='уравнение', linewidth='1')
plt.scatter(kelvin, fahrenheit, label='входные данные', color='green')
plt.scatter(kelvin_test, fahrenheit_test, label='предсказанное значение', color='blue')
plt.xlabel('Кельвина')
plt.ylabel('Фаренгейта')
plt.legend()
plt.grid(True)
plt.show()

import math
print(math.e,math.pi,math.nan,math.factorial(14),math.gcd(14,200))