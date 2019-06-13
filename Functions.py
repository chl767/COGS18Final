
# coding: utf-8

# In[ ]:


import string
import random

input_string=''
#This function will test if the input is a question and there will be an appropriate output for questions in this chatbox.
def a_question(input_string):
    for value in input_string:
        if '?' in input_string:
            output = True
        else:
            output = False
    return output

#This function will help prepare the input text for processing by removing all punctuation.
def remove_punctuation(input_string):
    out_string=[]
    for value in input_string:
        if value not in string.punctuation:
            out_string.append(value)
    out_string = ''.join(out_string)
    return out_string

#This function will prepare input text for processing.
def prepare_text(input_string):
    temp_string=input_string.lower()
    temp_string = remove_punctuation(temp_string)
    out_list=temp_string.split(" ")
    return out_list

#This function will randomly choose from a list of the appropriate output for a processed input.
def selector(input_list,check_list,return_list):
    output= None
    for value in input_list:
        if value in check_list:
            output= random.choice(return_list)
    return output

#This function is used to end the chatbox when 'quit' is typed into the input.
def end_chat(input_list):
    if 'quit' in input_list:
        output = True
    else:
        output = False
    return output

