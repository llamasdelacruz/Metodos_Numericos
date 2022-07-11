#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import matplotlib .pyplot as plt

def fx(x):
    return np.exp(-x)-x
def gx(x):
    return np.exp(-x)

Tolerancia = 0
xi = 0
Error = np.abs(gx(xi)-xi)
i = 0

while(Error > Tolerancia and i <= 100):
    
    if(i>0):
        
        Error = np.abs(gx(xi)-xi)
        
    xi = gx(xi)
    i = i + 1
    
print("el valor x tal que f(x) = 0 es :",xi)
    
x = np.linspace(0,1.5, 100)
plt.title("Metodo del punto fijo ")
plt.plot(x, fx(x), label="f(x)")
plt.plot(x,gx(x), label = "g(x)")
plt.plot(x,x,label = "f(x) = x")
plt.axvline(xi, label="f(x) = 0, x = (xi: .6f)", color = "k")
plt.axhline(0, color = "k")
plt.legend(loc='upper right')

plt.grid()
plt.show()


# In[ ]:




