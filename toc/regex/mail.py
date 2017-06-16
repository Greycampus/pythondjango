import re
k = str(raw_input('enter the raw data containing mail addresses:'))
#k = re.sub(r" .[a-zA-Z0-9]+. ",' ',k)
#k = re.sub(r" .[a-z]+. ",' ',k)
#k = re.sub(r" .[-+=!@#$%^&*\(\)\[\]\'\":;\.]+. ",' ',k)
#k = re.sub(r" [a-zA-Z0-9]+ ",' ',k)
#k = re.sub(r" .[a-zA-Z0-9]+$",' ',k)
#k = re.sub(r"^[a-zA-Z0-9]+. ",' ',k)
k = list(k.split())
print('extracted mail addresses are:')
for i in range(0,len(k)):
    if(re.match(r"^[a-zA-Z0-9]+.[@].[a-z]+\..[a-z]+$",k[i])):
        print(k[i])
