#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("world")


# In[9]:


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:

        def build(S):
            ans = []
            for x in S:
                if x != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return build(S) == build(T)


# In[ ]:





# In[ ]:





# In[7]:


n_a = "wha do you want?"
print ("Jack",n_a )


# In[10]:


class Solution(object):
    def shortestToChar(self, S, C):
        prev = float('-inf')
        ans = []
        for i, x in enumerate(S):
            if x == C: prev = i
            ans.append(i - prev)

        prev = float('inf')
        for i in xrange(len(S) - 1, -1, -1):
            if S[i] == C: prev = i
            ans[i] = min(ans[i], prev - i)

        return ans


# In[11]:


import collections


# In[13]:


import collections 
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List(str)) -> str:


# In[14]:


paragraph.replace


# In[16]:


string1 = []
string2 = []
for char in S:
    if char != "#"
      if len(string1)>=1:
        string1.append(char)
 
else: 
        string1.pop()
for char in T:
    if len(string2)>=1:
    if char != "#"
    string2.append(char)
     
else:
        string2.pop()
        
    return string1 == string2


# In[ ]:




