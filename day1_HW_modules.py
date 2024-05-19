#moody.py
#Problem Statement: Create a Python program using a custom module that asks the 
#user how they are feeling today and responds with a custom message based on the
# mood entered, Give responses for 'happy', 'sad', 'okay', and whatever else you 
#want.

def mood_response(mood ):
    
    mood = mood.lower()
    if mood == 'happy':
        return "That's great!"
    
    elif mood == 'sad':
        return "I'm sorry to hear that, I hope it changes for the better."
    
    elif mood == 'okay':
        return "It could always be worse, but half way to happy isnt bad."
    
    else:
        return "Not a valid response, please re-enter a valid response."