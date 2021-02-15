string = 'The lyrics is not that poor!'

notStr = string.find('not')  
poorStr = string.find('poor')  

if poorStr > notStr and notStr > 0 and poorStr > 0:
    string = string.replace(string[notStr:(poorStr+4)], 'good')  
print(string)  
