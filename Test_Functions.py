
# coding: utf-8

# In[1]:


import Functions
from Functions import a_question, remove_punctuation, prepare_text, selector, end_chat

assert callable(a_question)
assert isinstance(a_question('meow'), bool)
assert a_question('hello?') == True

assert callable(prepare_text)
assert isinstance(prepare_text('What is up?'), list)
assert prepare_text('What is up?') == ['what', 'is', 'up']

