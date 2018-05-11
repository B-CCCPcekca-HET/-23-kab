import os
from os.path import isfile
from os.path import join as joinpath
import sys
import pathlib
import time


#input('Press Enter.....')


######################################################
dirfile= os.path.dirname(os.path.abspath(__file__))
allfiles = os.listdir(dirfile)


for q in allfiles:
    #print(os.path.exists(dirfile))
    ff= dirfile+'\\'+q
    print(ff)#all file abs  patch

#######################################################
print("\n")
print("time sort \n")

#### sort ######
fulllist = [os.path.join(q ) for q in allfiles]
timesort = sorted(fulllist, key = os.path.getmtime)

print(timesort)

print('\n')
for r in timesort:
    res= os.path.join(dirfile,r)
    print(res)#time  sort

    
####### all pdf
print('\n')    
pd = 'pdf'
#pd = input('Расширение файла: ')
pdcorrect = '.' + pd
print(' print only: ' + pdcorrect + '  files')
mypdf = filter(lambda x: x.endswith(pdcorrect), timesort)
for d in mypdf:
  print(d)
  time.sleep(1)
  os.startfile(d,'print')  

