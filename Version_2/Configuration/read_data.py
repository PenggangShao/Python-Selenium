#encoding = utf-8
import os
file_name = os.getcwd() + '\data.txt'
content = open(file_name,'r')
file_content = content.readlines()
for x in file_content:
    if x.startswith('#'):
        continue
    else:
        print x.split()
        print 'url------>',x.split()[0]
        print 'username->',x.split()[1]
        print 'password->',x.split()[2]
