
# coding: utf-8

# # Project Description

# My project is a chatbox that will guess what color you're thinking. The colors you can choose from are: yellow, orange, red, purple, green, and blue. I tried to set up the chatbox in a way that will provide a variety of responses to answers, like a conversation with a real person. To begin the chatbox, type in 'pick_a_color()' at the bottom of the cell and type in any greeting in the input box. To exit the chat, type 'quit' in the input and the chatbox will end. 

# ## Project Code
# 
# If it makes sense for your project, you can have code and outputs here in the notebook as well.

# In[190]:


import Functions
from Functions import a_question, remove_punctuation, prepare_text, selector, end_chat


# In[191]:


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

#The following are a couple tests for the functions above.
assert callable(a_question)
assert isinstance(a_question('meow'), bool)
assert a_question('hello?') == True

assert callable(prepare_text)
assert isinstance(prepare_text('What is up?'), list)
assert prepare_text('What is up?') == ['what', 'is', 'up']

#These are the processed inputs and the corresponding outputs that the chatbox will show.
GREETINGS_IN = ['hello', 'hi', 'hey', 'hola', 'welcome', 'bonjour', 'greetings']
GREETINGS_OUT = ["Hello there! Think of a basic color (yellow, orange, red, purple, blue, green) Is it a warm or cold color?",                  "Hey! Let's play a game. Choose a color: yellow, orange, red, purple, blue, green. Is it a warm or cold color?"]
RESPONSE_1 = ["yes","yeah","ok","okay","sure", "youre right", "thats right", "right", "correct"]
RESPONSE_2 = ["no", "incorrect", "not", "wrong"]
RESPONSE_3 = ["warm","its a warm color"]
RESPONSE_4 = ["cold","its a cold color"]
QUESTION_1 = ['Is it considered light, medium, or dark?',               'Does the color remind you of lemons, oranges, or strawberries?',               'If it is a vegetable, would it be corn, squash, or chili pepper?']
QUESTION_2 = ['Would you say the color reminds you of grass, the sky, or tulips?',               'Does the color remind you of trees, water, or Justin Bieber?',               'If it was a fruit, would it be a lime, blueberry, or grape?']
RESPONSE_5 = ['light', 'lemon', 'lemons', 'corn']
RESPONSE_6 = ['medium', 'orange', 'oranges', 'squash']
RESPONSE_7 = ['dark', 'strawberries', 'strawberry', 'chili pepper']
RESPONSE_8 = ['grass','trees', 'lime']
RESPONSE_9 = ['sky','water', 'blueberry']
RESPONSE_10 = ['tulips', 'flowers','justin', 'bieber', 'justin bieber', 'grape']
ANSWER_7 = ["The color is yellow, am I right?", "You're definitely thinking of yellow, right?"]
ANSWER_8 = ["The color is orange, am I right?","Obviously, it's orange, right?"]
ANSWER_9 = ["The color is red, am I right?", "IT'S RED, don't tell me it's not red."] 
ANSWER_10 = ["The color is green, am I right?", "You're thinking of green! Right?"]
ANSWER_11 = ["The color is blue, am I right?", "Is the color you're thinking blue?"]
ANSWER_12 = ["The color is purple, am I right?", "You're definitely thinking of purple, am I right?"]
CORRECT_ANSWER = ['Awesome! Pick another color, is it warm or cold?',                   "Cool, let's play again! Is your new color warm or cold?"]
WRONG_ANSWER = ["I tried my best. Pick another color, is it warm or cold? or type 'quit' to quit",                 "Oh no! Let's try again. Is it warm or cold?",                 "Y = mx + it b like that sometimes. Pick another color or type 'quit' to quit"]
OTHER = ["This is all I can do, you have to pick another color or type 'quit'to quit",          "Did you type that right? Try again.",          "Wait what?",          "Huh?"]

#The following is the code for my chatbox. You can see there is a section that creates the appropriate output for a processed input.
def pick_a_color():
    chat = True
    while chat:
        msg = input('INPUT :\t')
        out_msg = None
        question = a_question(msg)
        msg = prepare_text(msg)
        if end_chat(msg):
            out_msg = 'Bye!'
            print(outs)
            chat = False
        if not out_msg:
            outs = []
            outs.append(selector(msg, GREETINGS_IN, GREETINGS_OUT))
            outs.append(selector(msg, RESPONSE_2, WRONG_ANSWER))
            outs.append(selector(msg, RESPONSE_1, CORRECT_ANSWER))
            outs.append(selector(msg, RESPONSE_3, QUESTION_1))
            outs.append(selector(msg, RESPONSE_5, ANSWER_7))
            outs.append(selector(msg, RESPONSE_6, ANSWER_8))
            outs.append(selector(msg, RESPONSE_7, ANSWER_9))
            outs.append(selector(msg, RESPONSE_4, QUESTION_2))
            outs.append(selector(msg, RESPONSE_8, ANSWER_10))
            outs.append(selector(msg, RESPONSE_9, ANSWER_11))
            outs.append(selector(msg, RESPONSE_10, ANSWER_12))
        options = list(filter(None, outs))
        if options:
            out_msg = random.choice(options)
        if not out_msg and question:
            out_msg = OTHER
        if not out_msg:
            out_msg = random.choice(OTHER)
        print('OUTPUT:', out_msg)
        
#To run the chatbox, run the cell and type in a greeting into the input box.   
pick_a_color()

