#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n//3 + (n % 6==2), dtype=bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]


# In[6]:


import time as t

start_time = t.time()
p = primesfrom2to(1449500000)
duration = t.time() - start_time
print('len: {}, Local execution time: {}'.format(len(p), duration))
# len: 72333789, Local execution time: 5.7807297706604, not bad


# In[7]:


def writing_primes():
    I = int(1449500000/500000)
    
    start_time = t.time()
    for i in range(I): 
        sf = f'C:/Users/Joe/Documents/batch_primes/PrimesTo_{(i+1)*500000}.txt'
        f = open(sf,'a')
        for j in p[np.where(np.logical_and(p>=0+i*500000, p<=i*500000 + 500000))[0]]:
            f.write(f'{j}')
            f.write('\n')
        f.close()
    duration = t.time() - start_time
    print('Local execution time: {}'.format(duration))


# In[ ]:


writing_primes()

