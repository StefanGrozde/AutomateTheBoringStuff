#! python3
# pigLatin.py is a program that transforms your message in Pig Latin

print('Enter the English message you want to translate into Pig Latin:')
message = input()
words = message.split(' ')
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
for i in range(len(words)):
    consonants = ''
    if words[i].isdecimal() == True:
        continue
    elif words[i][0] in vowels:
        words[i] += 'yay'
    else:
        for l in words[i]:
            if l not in vowels:
                consonants += l
            else:
                break      
        words[i] = words[i][len(consonants):]
        words[i] += consonants.lower() + 'ay'   
message = ' '.join(words)
print(message)