#ja       
s=0        
x=int(input("wprowaź liczbę całkowitą: "))
for z in range(1,abs(x)):
    while z*z*z==abs(x):
        if x>0:
            print(z)
            s=z
            break
        else:
            print(-z)
            s=z
            break
if  s==0:
   print("idealny szescian nieistnieje") 
   
#książka

x = int(input("Enter an integer: "))
ans=O
while ans**3 < abs(x):
    ans = ans + 1
    if ans**3 abs(x):
        print(x, is not a perfect cube’)
    else:
        if x < 0:
            ans = -ans
            print(’Cube root of, x,is, ans)