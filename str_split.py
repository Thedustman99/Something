import random
import string

def lower_case():
    return random.choice(string.ascii_lowercase)
def upper_case():
    return random.choice(string.ascii_uppercase)
def alphabets():
    return random.choice(string.ascii_letters)
def numbers():
    return random.randint(0,9)
def special_characters():
    return random.choice(string.punctuation)

functions_list = [lower_case, upper_case, alphabets, numbers, special_characters]

random_function = random.choice(functions_list)
print(random.choice(functions_list[lower_case, upper_case, alphabets, numbers, special_characters])())



#print(random_function())

