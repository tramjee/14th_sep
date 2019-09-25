import re
fileToOpen=input('Enter the file to Open')
fd=open(fileToOpen)
numlist = list()
for line in fd:
   line = line.rstrip()

   y = re.findall('[0-9]+',line)
   if y != []:
       numlist.extend(y)

total = 0
for x in numlist:
    total = total + int(x)

print(total)





