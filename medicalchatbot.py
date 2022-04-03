#!/usr/bin/env python
# coding: utf-8

# In[1]:
# pip install nltk
# # In[2]:
# pip install newspaper3k
# # In[3]:
# pip install sklearn

# In[4]:

#Import the libraries

from newspaper import Article
import random
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings
warnings.filterwarnings('ignore')


# In[5]:
#in case nltk causes problems
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
    
#Download the punkt package
nltk.download('punkt', quiet=True)
# In[6]:
#Get the corpus
urls = ['https://www.health.harvard.edu/a-through-c', 'https://www.health.harvard.edu/d-through-i', 'https://www.health.harvard.edu/j-through-p', 'https://www.health.harvard.edu/q-through-z']
corpus = ''

for url in urls:
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    corpus += article.text


# In[7]:


#Print the articles text
# print(corpus)


# In[8]:


from nltk.tokenize import regexp_tokenize
#Tokenization
text = corpus
term_list = nltk.regexp_tokenize(text, '\n', gaps=True) # A list of sentence fragments


# In[9]:


# Print the list of sentences
# print(term_list)


# In[10]:


med_term_list = []
for definition in term_list:
   term = definition.split(':', 1)[0]
   med_term_list.append(term)
# print(med_term_list)


# In[11]:


# A function to return a random greeting response to a users greeting

import re 

def greeting_response(text):
  text = text.lower()

  #Users greeting
  user_greetings = ['hi', 'hey', 'hello', 'hola', 'greetings', 'good afternoon', 'good morning', 'good evening']

  #bots greeting response
  bot_greetings = ['Hello', 'Hi', 'Ask me anything']

  for word in re.split('; |: |, |. |\*|\n', text):
    if word in user_greetings:
      return random.choice(bot_greetings)
      
# In[12]:


# A function to sort the list indices (to be used later for comparing similarity scores)
def index_sort(list_in):
  list_index = list(range(0, len(list_in)))

  x = list_in
  for i in range(len(list_in)):
    for j in range(len(list_in)):
      if x[list_index[i]] > x[list_index[j]]:
        #Swap
        temp = list_index[i]
        list_index[i] = list_index[j]
        list_index[j] = temp

  return list_index


# In[13]:


""" #Create the bots response
def bot_response_org(user_input):
  user_input = user_input.lower()
  bot_response = ''
  med_term_list.append(user_input)
  cm = CountVectorizer().fit_transform(med_term_list)  #Use CountVectorizer to convert text to numerical data
  similarity_scores = cosine_similarity(cm[-1], cm) #cm[-1] refers to user_input element
  similarity_scores_list = similarity_scores.flatten()
  similarity_scores_list = np.array(similarity_scores_list.tolist().remove(1.00))
 # similarity_scores_li = similarity_scores_list[:-1]
  index = index_sort(similarity_scores_list)
  
  index = index[1:]
  hasResponse = False

  j = 0
  for i in range(len(index)):
    if similarity_scores_list[index[i]] > 0.0:
      # print(index[i])
      bot_response = bot_response + ' ' + term_list[index[i]]
      hasResponse = True
      j += 1
    if j > 2:
      break
    
    med_term_list.remove(user_input)

    if hasResponse == False:
      bot_response = bot_response + ' ' + "I apologize, I don't understand."

    return bot_response


# In[1]: """


#Create the bots response using tfidf
def bot_response(user_input):
  user_input = user_input.lower()
  bot_response = ''
  term_list.append(user_input)
  cm = TfidfVectorizer().fit_transform(term_list)  #Use CountVectorizer to convert text to numerical data
  similarity_scores = cosine_similarity(cm[-1], cm) #cm[-1] refers to user_input element
  similarity_scores_list = similarity_scores.flatten()
 # similarity_scores_li = similarity_scores_list[:-1]
  index = index_sort(similarity_scores_list)
  
  index = index[1:]
  hasResponse = False

  j = 0
  for i in range(len(index)):
    if similarity_scores_list[index[i]] > 0.0:
      bot_response = bot_response + ' ' + term_list[index[i]]
      hasResponse = True
      j += 1
    if j > 2:
      break
    
    term_list.remove(user_input)

    if hasResponse == False:
      bot_response = bot_response + ' ' + "I apologize, I don't understand."

    return bot_response


# In[ ]:


""" #Start the chat
print('Doc Bot: I am Doc Bot. I can help answer any of your medical queries. If you want to exit, type bye')

exit_list = ['exit', 'see you later', 'bye', 'quit', 'break']
while(True):
  user_input = input()
  if user_input.lower() in exit_list:
    print('Doc Bot: Chat with you later!')
    break
  else:
    if greeting_response(user_input) != None:
      print('Doc Bot: ' + greeting_response(user_input))
    else:
      print('Doc Bot: ' + bot_response(user_input)) """

def get_bot_response(user_input): 
  exit_list = ['exit', 'see you later', 'bye', 'quit', 'break']
  if user_input.lower() in exit_list:
    print('Doc Bot: Chat with you later!')
  else:
    if greeting_response(user_input) != None:
      print('Doc Bot: ' + greeting_response(user_input))
    else:
      print('Doc Bot: ' + bot_response(user_input))





