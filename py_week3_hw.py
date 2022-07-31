#!/usr/bin/env python
# coding: utf-8

# In[124]:


from scipy.stats import norm
from scipy.stats import binom as b
from scipy.stats import t 
import matplotlib.pyplot as plt
import numpy as np


# In[ ]:


#q1
#The weights of steers in a herd are distributed normally.  The variance is 40,000 and the mean steer weight is 1300 lbs.  Find the probability that the weight of a randomly selected steer is greater than 979 lbs. (Round your answer to 4 decimal places)


# In[2]:


# X = weigh of a steer
#P(X>979 | Mu = 1300, V = 40000)

print(1-norm.cdf(979, loc=1300, scale=200)) #upper tail
print(norm.cdf(979, loc=1300, scale=200)) #lower tail


# In[ ]:


#q2. SVGA monitors manufactured by TSI Electronics have life spans that have a normal distribution with a variance of 1,960,000 and a mean life span of 11,000 hours. If a SVGA monitor is selected at random, find the probability that the life span of the monitor will be more than 8340 hours. (Round your answer to 4 decimal places)


# In[22]:


m = 11000
v = 1960000
sd = np.sqrt(v)
sd


# In[28]:


round(1-norm.cdf(8340, 11000, sd),4)


# In[ ]:


#Q3

#Suppose the mean income of firms in the industry for a year is 80 million dollars with a standard deviation of 3 million dollars.  If incomes for the industry are distributed normally, what is the probability that a randomly selected firm will earn between 83 and 85 million dollars? (Round your answer to 4 decimal places)


# In[7]:


round((norm.cdf(85, loc=80, scale=3) - norm.cdf(83, loc=80, scale=3)), 4)


# In[ ]:


#q4
#Suppose GRE Verbal scores are normally distributed with a mean of 456 and a standard deviation of 123.  A university plans to offer tutoring jobs to students whose scores are in the top 14%.  What is the minimum score required for the job offer?  Round your answer to the nearest whole number, if necessary


# In[32]:


round(norm.ppf(0.14, 456, 123))


# In[ ]:


#q5
#The lengths of nails produced in a factory are normally distributed with a mean of 6.13 centimeters and a standard deviation of 0.06 centimeters.  Find the two lengths that separate the top 7% and the bottom 7%.  These lengths could serve as limits used to identify which nails should be rejected.  Round your answer to the nearest hundredth, if necessary.


# In[10]:


print(round(norm.ppf(0.07, 6.13, 0.06), 4), "\n", round(norm.ppf(.93,6.13,0.06), 4))


# In[ ]:


#q6 An English professor assigns letter grades on a test according to the following scheme. A: Top 13% of scores B: Scores below the top 13% and above the bottom 55% C: Scores below the top 45% and above the bottom 20% D: Scores below the top 80% and above the bottom 9% F: Bottom 9% of scores Scores on the test are normally distributed with a mean of 78.8 and a standard deviation of 9.8. Find the numerical limits for a C grade. Round your answers to the nearest whole number, if necessary.


# In[34]:


print(round(norm.ppf(0.20, 78.18, 9.8)), "\n", round(norm.ppf(.55,78.8,9.8)))


# In[ ]:


#q7 Suppose ACT Composite scores are normally distributed with a mean of 21.2 and a standard deviation of 5.4. A university plans to admit students whose scores are in the top 45%. What is the minimum score required for admission? Round your answer to the nearest tenth, if necessary.


# In[37]:


print(round(norm.ppf(0.45, 21.2, 5.4),2))


# In[ ]:


#q8 Consider the probability that less than 11 out of 151 students will not graduate on time. Assume the probability that a given student will not graduate on time is 9%. Approximate the probability using the normal distribution. (Round your answer to 4 decimal places.)


# In[40]:


round(b.cdf(10,151,0.09), 4)


# In[ ]:


#q9 


# In[44]:


sd = 7/np.sqrt(147)
round(sd, 4)


# In[56]:


1-norm.cdf(48.83,  48,  0.5774)
#the answer should be 0.075


# In[52]:


#q10


# In[54]:


sd = 10/np.sqrt(68)
sd


# In[57]:


1-norm.cdf(93.54, 91, 1.212)


# In[58]:


#q11


# In[74]:


print(round((b.cdf(0.10*540, 540, 0.07)-b.cdf(.04*540, 540, 0.07)),4))


# In[75]:


#q12


# In[76]:


print(round((b.cdf(0.27*602, 602, 0.23)-b.cdf(.19*602, 602, 0.23)),4))


# In[ ]:


#q13


# In[79]:


print(round(norm.ppf(.1, 3.9, .8/np.sqrt(208)), 1), "\n", round(norm.ppf(.9, 3.9, .8/np.sqrt(208)), 1))


# In[80]:


#q14


# In[84]:


print(round(norm.ppf(.01, 16.6, 11/np.sqrt(7472)), 1), "\n", round(norm.ppf(.99, 16.6, 11/np.sqrt(7472)), 1))


# In[85]:


#q15


# In[117]:


print(round(t.ppf(0.05, 26) , 1))


# In[87]:


#q16


# In[108]:


data = [383.6, 347.1, 371.9, 347.6, 325.8, 337]


# In[109]:


#step 1
mean = round(np.mean(data),2)
print(mean)


# In[111]:


#step 2
sd = round(np.std(data),2)
print(sd)


# In[125]:


#step 3
t = round(t.ppf(0.05, 5) , 3)
upper = round(mean - (sd/np.sqrt(6)) * t, 2)
upper


# In[126]:


#step 4
lower = round(mean + (sd/np.sqrt(6)) * t, 2)
lower


# In[127]:


#q17


# In[130]:


print(round(norm.ppf(.1, 16, .8/np.sqrt(16)), 1), "\n", round(norm.ppf(.9, 16, .8/np.sqrt(16)), 1))


# In[ ]:


#q18


# In[140]:


z = np.abs(norm.ppf(0.05, 0, 1))
z


# In[145]:


np.ceil((np.power(z, 2) * np.power(1.9, 2)) / np.power(0.13,2))


# In[ ]:


#q19


# In[146]:


z = np.abs(norm.ppf(0.025, 12.6, np.sqrt(3.61)))
np.ceil((np.power(z, 2) * 3.61) / np.power(0.19,2))


# In[147]:


#q20


# In[148]:


p = 1 - (1734/2089)
p


# In[149]:


z = np.abs(norm.ppf(0.01,  0,  1))
z


# In[151]:


lower = round(p - (z * np.sqrt((p * (1-p)) / 2089)), 3)
lower


# In[152]:


upper = round(p + (z * np.sqrt((p * (1-p)) / 2089)), 3)
upper


# In[153]:


#q21


# In[154]:


p = 156 / 474
p


# In[155]:


z = np.abs(norm.ppf(0.025,  0,  1))
z


# In[156]:


lower <- round(p - (z * np.sqrt((p * (1-p)) / 474)), 3)
lower


# In[157]:


upper <- round(p + (z * np.sqrt((p * (1-p)) / 474)), 3)
upper

