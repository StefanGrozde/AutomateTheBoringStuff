import pyperclip,re

text = pyperclip.paste()

def findPhoneNumbers(texts):
    phoneNumber = re.compile('\d{3}-\d{3}-\d{4}')
    mo = phoneNumber.findall(texts)
    return mo
def findEmails(texts):
    email = re.compile('\w+@\w+\\.\w+')
    mo = email.findall(texts)
    return mo

phoneNumbers = findPhoneNumbers(text)
emails = findEmails(text)

print(emails)