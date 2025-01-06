import random
import string

def ElonMuskpassword():

    uppercase = string.ascii_uppercase  
    lowercase = string.ascii_lowercase  
    digits = string.digits             
    punctuation = string.punctuation   
    password = [ random.choice(uppercase) for Mita in range(2)
    ] + [
        random.choice(lowercase) for Mita in range(2)
    ] + [
        random.choice(digits) for Mita in range(2)
    ] + [
        random.choice(punctuation) for Mita in range(2)
    ]
   
    random.shuffle(password)

    
    return ''.join(password)


print("Your UWU password is:", ElonMuskpassword())