# importing python regex library
import re
k = str(raw_input('enter the raw data containing mail addresses:'))
#simple comments:ignore
#k = re.sub(r" .[a-zA-Z0-9]+. ",' ',k)
#k = re.sub(r" .[a-z]+. ",' ',k)
#k = re.sub(r" .[-+=!@#$%^&*\(\)\[\]\'\":;\.]+. ",' ',k)
#k = re.sub(r" [a-zA-Z0-9]+ ",' ',k)
#k = re.sub(r" .[a-zA-Z0-9]+$",' ',k)
#k = re.sub(r"^[a-zA-Z0-9]+. ",' ',k)

#making list by using split
k = list(k.split())
print('extracted mail addresses are:')
for i in range(0,len(k)):
    #checking the regex of email pattern like alphanumeric@alphabets.domain
    if(re.match(r"^[a-zA-Z0-9]+.[@].[a-z]+\..[a-z]+$",k[i])):
        print(k[i])
