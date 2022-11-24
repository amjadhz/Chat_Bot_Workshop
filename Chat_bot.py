# Import libraries 
import random

# Define chat bot answers
greeting = ['Hello', 'Hi', 'Good morning!']

# Key words of user input
good_feeling = ['happy', 'ok','okay','good','fine']
bad_feeling = ['sad','angry','down','bad']
yes = ['yes','yep','yea']
no = ['no','nope', 'nah']

# Functions to define the user answer
def good_mood(st):
    if any(element in st.lower().split() for element in good_feeling):
        return True     
def bad_mood(st):
    if any(element in st.lower().split() for element in bad_feeling):
        return True 
def answer_yes(st):
    if any(element in st.lower().split() for element in yes):
        return True 
def answer_no(st):
    if any(element in st.lower().split() for element in no):
        return True 
        
# Start conversation
print(random.choice(greeting))
print('How are you today?')
user_input = input()
 
# The chat scienario      
while  user_input:

    if not (good_mood(user_input) or bad_mood(user_input)) :
        print("I don't understand! Do you feel good or bad? ")
        user_input = input()
        
    elif good_mood(user_input):
        print('That is amazing, I wish you always be happy!')
        break
        
    elif bad_mood(user_input):
        print('Awww that so bad to hear!')
        break
        
# While the user answer is about having good feelings         
while good_mood(user_input):
    print('Do you like chocolate?')
    user_input1 = input()
    if answer_yes(user_input1):
        print('Then you can buy it from the canteen')
        break
    if answer_no(user_input1):
        print('That is fine too, drink alot of water it is hot day.')
        print ('Wish you great day! 😊✌️')
        break
    else :
        print ('Please answer with yes or no')
        user_input1 = ''
        continue

# While the user answer is about having bad feeling
while bad_mood(user_input):
    print('Do you like to hear some music?')
    user_input2 = input()
    
    if answer_yes(user_input2):
        print('You can put some songs on youtube')
        break
    
    if answer_no(user_input2):
        print('Maybe relaxing could be good.')
        print('Be optimistic! life is too short 😊')
        break
    
    else :
        print ('Please answer with yes or no')
        user_input2 = ''
        continue



    
