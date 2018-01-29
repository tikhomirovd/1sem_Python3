import urllib
import  requests

p='https://stepic.org/media/attachments/course67/3.6.3/'
n='699991.txt'
f=True
while f:
    url=p+n
    webFile=requests.get(url)
    localFile=open(n,'wb')
    localFile.write(webFile.read())
    webFile.close()
    localFile.close()
    with open(n) as input_file:
        for line in input_file:
            if 'We' in line:
                f=False
            if not f:
                print(line.strip())
            if f:
                n=line