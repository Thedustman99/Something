user_string = input("Write a sentence.      ")
characters = user_string.split()
print(characters[-1])
count=0
for words in characters[-1]:
    count+=1

print(f"The last word is '{characters[-1]}' with length {count}")
