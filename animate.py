# importing the necessary packages
import time
import sys
import os
  
# Function for implementing the loading animation
def load_animation():
    os.system("clear")
    # String to be displayed when the application is loading
    load_str = "preparing the realm for your epic adventure. please hold on while we gather our magical forces..."
    ls_len = len(load_str)
  
  
    # String for creating the rotating line
    animation = "|/-\\"
    anicount = 0
      
    # used to keep the track of
    # the duration of animation
    counttime = 0        
      
    # pointer for travelling the loading string
    i = 0                     
  
    while (counttime != 100):
          
        # used to change the animation speed
        # smaller the value, faster will be the animation
        time.sleep(0.090) 
                              
        # converting the string to list
        # as string is immutable
        load_str_list = list(load_str) 
          
        # x->obtaining the ASCII code
        x = ord(load_str_list[i])
          
        # y->for storing altered ASCII code
        y = 0                             
  
        # if the character is "." or " ", keep it unaltered
        # switch uppercase to lowercase and vice-versa 
        if x != 32 and x != 46:             
            if x>90:
                y = x-32
            else:
                y = x + 32
            load_str_list[i]= chr(y)
          
        # for storing the resultant string
        res =''             
        for j in range(ls_len):
            res = res + load_str_list[j]
              
        # displaying the resultant string
        sys.stdout.write("\r"+res + animation[anicount])
        sys.stdout.flush()
  
        # Assigning loading string
        # to the resultant string
        load_str = res
  
          
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len
        counttime = counttime + 1
      
    # for windows OS
    if os.name =="nt":
        os.system("cls")
          
    # for linux / Mac OS
    else:
        os.system("clear")
  
def animate_text(text):
    number_of_characters=1
    while True:
        print("\n")
        print(text[0:number_of_characters])
        number_of_characters += 1
        if number_of_characters > len(text):
            number_of_characters = 0
            time.sleep(0.2)
            os.system('clear')  

def stream_text_horizontal(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print() 

def flash(text):
    while True:
        print(text)
        time.sleep(0.5) # pause for half a second
        os.system('clear') # clears the console window again
        time.sleep(0.5) # pause for half a second
        if input() == "":
            break