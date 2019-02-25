# keybag
Small keylogger on python

So the main point of this keylogger is to make logfile more readable. ^^

Only for learning etc

Dont be evil.



***
psps
decoding:

import base64

data = base64.b64decode(open('not.note', 'r+').read())

print data
