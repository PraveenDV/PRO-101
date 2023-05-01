import random

response=input('press y to roll the dice: ')
no=random.randint(1,6)

while response=='y':
    if(no==1):
        print('[---]')
        print('[   ]')
        print('[ 0 ]')
        print('[   ]')
        print('[---]')
        break
        
    elif(no==2):
        print('[---]')
        print('[0  ]')
        print('[   ]')
        print('[  0]')
        print('[---]')
        break

    elif(no==3):
        print('[---]')
        print('[0  ]')
        print('[ 0 ]')
        print('[  0]')
        print('[---]')
        break

    elif(no==4):
        print('[---]')
        print('[0 0]')
        print('[   ]')
        print('[0 0]') 
        print('[---]')
        break

    elif(no==5):
        print('[---]')
        print('[0 0]')
        print('[ 0 ]')
        print('[0 0]') 
        print('[---]')
        break

    elif(no==6):
        print('[---]')
        print('[000]')
        print('[   ]') 
        print('[000]')
        print('[---]')
        break