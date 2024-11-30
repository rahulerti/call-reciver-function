# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 12:48:13 2024

@author: Rahul Debnath
"""
i=('vivek','akash','amal','subrata','akshay','unknown number')
import random
item=random.choice(i)
print(item)
if item=='akash':
     print('''call disconnect
           good day sir''')
elif item=='unknown number':
     print('''call disconnect
           good day sir''')           
elif item=='vivek':
     print('''call disconnect
           good day sir''')
elif item=='amal':
     type=(input('calling:'))
     if type=='yes':
         print('start calling')
     else:
         print('disconnected')
elif item=='subrata':
     type=(input('calling:'))
     if type=='yes':
         print('start calling')
     else:
            print('disconnected')
elif item=='akshay':
     type=(input('calling:'))
     if type=='yes':
         print('start calling')
     else:
         print('disconnected')
        


    
    
    
    
    
