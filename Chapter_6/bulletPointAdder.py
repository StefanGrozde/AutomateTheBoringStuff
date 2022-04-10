#! python3
#bulletPointerAddrer.py - Adds Wikipedia bullet points to the starts
# of each new line of text on the clipboard

import pyperclip
text = pyperclip.paste()
text = text.split('\n')
print(text)
for i in range(len(text)):
    text[i] = '* ' + text[i]
text = '\n'.join(text)
pyperclip.copy(text)


