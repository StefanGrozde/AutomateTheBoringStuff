import re

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

phoneNumber = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumber.findall(message)
for i in range(len(mo)):
    print('Phone number found: ' + mo[i])