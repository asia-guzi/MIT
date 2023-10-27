# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 09:43:56 2023

@author: Joanna.Guziwelakis
"""

"""
Ćwiczenie z palcem: Napisz program, który poprosi użytkownika o podanie 
liczby całkowitej i wypisze dwie liczby całkowite, root i pwr, takie, że 
1 < pwr < 6 oraz root**pwr jest równy irrtegerze wpisanej przez użytkownika. 
Jeśli taka para liczb całkowitych nie istnieje, to powinien wypisać 
komunikat komunikat o tym fakcie.

"""
"""poniższe nie działało, bo podczas gdy root wynosił 2 do pwr 5, to przekroczyło k i nie poleciało dalej, ale miało być przy 9 3 do pot. 2 wiec na root 3 juz nie weszło - próba z while zamiast for   

k=int(input("please insert an integer"))
root=0
pwr=1

    
while root**pwr<k: #tutaj nie może być większe równe bo dla równego dalej jechał pente i podwyższał wartoci8
     root=root+1
     for pwr in range(2,6): 
         
         print(pwr)
         print(root)
         
         if root**pwr==k:
            print("root = ", root)
            print("pwr = ", pwr)
            break
         #else: 
           # root=root+1 #dlaczego zadziałało dopiero gdy root rósł pod pętlą for,a nie while??
         
if root**pwr!=k:
        print("such a tandem of integres does not exist")
        
"""
k=int(input("please insert an integer"))
x=0
pwr=0
root=0
      

for pwr in range(2,6): 
      while root**pwr<k: #tutaj nie może być większe równe bo dla równego dalej jechał pente i podwyższał wartoci8
        root=root+1
        
        if root**pwr==k:
            print("root = ", root)
            print("pwr = ", pwr)
            break 
        
            
             # root=root+1 #dlaczego zadziałało dopiero gdy root rósł pod pętlą for,a nie while??
           
if not root**pwr==k:
     
     print("such a tandem of integres does not exist")  