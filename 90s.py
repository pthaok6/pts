import os
os.system('clear')
print('================================================')
os.system('git pull')
print('================================================')
choose=input('1-web || 0-app => ')
os.system('clear')
if (choose):
 os.system('python 90app.py')
else: 
 os.system('python 90.py')
