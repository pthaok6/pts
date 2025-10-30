import os
os.system('clear')
print('================================================')
os.system('git pull')
print('================================================')
choose=input('1-web || 0-app => ')
choose=1
os.system('clear')
if (choose==1):
 os.system('python 90app.py')
else: 
 os.system('python 90.py')
