import random
import string

def lower_case():
    return random.choice(string.ascii_lowercase)
def upper_case():
    return random.choice(string.ascii_uppercase)
def numbers():
    return random.randint(0,9)
def special_characters():
    return random.choice(string.punctuation)

complexity = int(input("1 - only lowercase \n2 - lowercase and numbers\n3 - alphanumeic \n4 - alphanumeric and special characters   "))
lenth = int(input("Enter the password length.   "))

password = ""
for i in range(lenth):
    if complexity==1:
        print(random.choice([lower_case])() , end=' ')
    elif complexity==2:
        print(random.choice([lower_case, numbers])() , end=' ')
    elif complexity==3:
        print(random.choice([lower_case, upper_case, numbers])() , end=' ')
    else:
        print(random.choice([lower_case, upper_case, numbers, special_characters])() , end=' ')
