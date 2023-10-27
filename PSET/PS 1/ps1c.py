
"""
annual_salary=float(input("insert annual salary: "))
total_cost=float(1000000)
portion_down_payment =float(0.25*total_cost)
current_savings=float(0)
semi_annual_raise=float(7/100)
r=float(4/100)
rm=float(r/12)
c=0
d=0
guess=float(0)
high=10000
low=0
epsilon=float(0.1)
p=portion_down_payment - current_savings


for c in range(36):
  while abs(p)>=epsilon:  

    guess=float((high+low)/2)
    d=d+1
    proc=float(guess/10000)
    portion_saved=float(proc*(annual_salary/12))
    current_savings=current_savings+portion_saved+current_savings*rm
    p=portion_down_payment - current_savings
    if c>1 and c%6==0:
            annual_salary=annual_salary*(1.0+semi_annual_raise)
       
    
       
   
    if abs(p)<epsilon :
             print("you will be saving  ", proc," monthly")
             break
             
    elif (p)>=epsilon :
             low=guess
    else:
             high=guess
   
    
   
    
   
else :
             print("sllary too small to safe")
             

print("d=",d) 

"""
"""
annual_salary=float(input("insert annual salary: "))
total_cost=float(1000000)
portion_down_payment =float(0.25*total_cost)
current_savings=float(0)
semi_annual_raise=float(7/100)
r=float(4/100)
rm=float(r/12)
c=0
d=0
guess=float(0)
high=10000
low=0
epsilon=float(0.1)
p=portion_down_payment - current_savings


for c in range(36):
    guess=float((high+low)/2)
    d=d+1
    proc=float(guess/10000)
    portion_saved=float(proc*(annual_salary/12))
    current_savings=current_savings+portion_saved+current_savings*rm
    p=portion_down_payment - current_savings
    
       
    
       
   
    if abs(p)<epsilon :
             print("you will be saving  ", proc," monthly")
             break
             
    elif (p)>=epsilon :
             low=guess
    else:
             high=guess
    if c>1 and c%6==0:
            annual_salary=annual_salary*(1.0+semi_annual_raise)
    
   
    
   
if abs(p)>=epsilon :
             print("sllary too small to safe")
             



"""
"""
annual_salary=float(input("insert annual salary: "))
total_cost=float(1000000)
portion_down_payment =float(0.25*total_cost)
current_savings=float(0)
semi_annual_raise=float(7/100)
r=float(4/100)
rm=float(r/12)
c=0
d=0
guess=float(0)
high=10000
low=0
epsilon=float(1000)
proc=0


for c in range(36):
    
    
   
    
    
    
       
    
       
   
    while float(abs(portion_down_payment - current_savings))>epsilon :
        
        d=d+1
        guess=float((high+low)/2)
    
        proc=float(guess/10000)
        portion_saved=float(proc*(annual_salary/12))
        current_savings=current_savings+portion_saved+current_savings*rm
        
        if float(abs(portion_down_payment - current_savings))<=epsilon:
            print("you will be saving  ", proc," monthly")
            break
             
        elif float(portion_down_payment - current_savings)>epsilon :
             low=guess
        else:
             high=guess
             
             
             
    if c>1 and c%6==0:
            annual_salary=annual_salary*(1.0+semi_annual_raise)
   
    
   
if float(abs(portion_down_payment - current_savings))>epsilon :
             print("sllary too small to safe")
    """
    
"""    
annual_salary=float(input("insert annual salary: "))
monthly_salary=float()
total_cost=float(1000000)
down_payment =float(0.25*total_cost)
current_savings=float(0)
semi_annual_raise=float(7/100)
semi_monthly_raise=float(semi_annual_raise/12)
r=float(4/100)
rm=float(r/12)

d=0


high=10000
low=0
guess=(high+low)/2
epsilon=float(1000)
proc=float(guess/10000)
portion_saved=float(proc*monthly_salary)
current_savings=float(current_savings+portion_saved+current_savings*rm)
p=float(down_payment - current_savings)


    
    
    
       
    
       
while p>epsilon and (-p)<(-epsilon) :
        d=d+1
        guess=(high+low)/2
        print("guess=",guess)
        proc=float(guess/10000)
        print("proc=",proc)
        for c in range(36):
          print("c=",c) 
           
          
          portion_saved=float(proc*monthly_salary)
          print("portion saved=", portion_saved)
          current_savings=float(current_savings+portion_saved+current_savings*rm)
          print("current savings=",current_savings)
          if c>1 and c%6==0:
            monthly_salary=monthly_salary*(1.0+semi_monthly_raise)
            print("monthly_salary=",monthly_salary)
       
        
       
        
    
        p=float(down_payment - current_savings)
        print("downpayment - current savings=",p)
        
        if p<= epsilon and (-p) >= epsilon:
                        break
             
        elif down_payment - current_savings>epsilon :
             low=guess
        else:
             high=guess
             
             
             

   
    
   
if p<= epsilon or (-p) >= (-epsilon):
    print("you will be saving  ", proc," monthly")
else:
    
    print("sllary too small to safe")
    
print(d)
"""    


"""
annual_salary=float(input("insert annual salary: "))
monthly_salary=float(annual_salary/12)
total_cost=float(1000000)
down_payment =float(0.25*total_cost)
current_savings=float(0)
semi_annual_raise=float(7/100)
semi_monthly_raise=float(semi_annual_raise/12)
r=float(4/100)
rm=float(r/12)

d=0


high=10000
low=0
guess=(high+low)/2
epsilon=float(1000)
proc=float(guess/10000)
portion_saved=float(proc*monthly_salary)
current_savings=float(current_savings+portion_saved+current_savings*rm)
p=float(down_payment - current_savings)


    
    
    
       
    
       
while p>epsilon and (-p)<(-epsilon) :
        d=d+1
        guess=(high+low)/2
        print("guess=",guess)
        proc=float(guess/10000)
        print("proc=",proc)
        for c in range(36):
          print("c=",c) 
           
          
          portion_saved=float(proc*monthly_salary)
          print("portion saved=", portion_saved)
          current_savings=float(current_savings+portion_saved+current_savings*rm)
          print("current savings=",current_savings)
          if c>1 and c%6==0:
            monthly_salary=monthly_salary*(1.0+semi_monthly_raise)
            print("monthly_salary=",monthly_salary)
       
        
       
        
    
        p=float(down_payment - current_savings)
        print("downpayment - current savings=",p)
        print("down_payment=",down_payment)
        
        if p<= epsilon and (-p) >= epsilon:
                        break
             
        elif down_payment - current_savings>epsilon :
             low=guess
        else:
             high=guess
             
             
             

   
    
   
if p<= epsilon or (-p) >= (-epsilon):
    print("you will be saving  ", proc," monthly")
else:
    
    print("sllary too small to safe")
    
print(d)
"""

"""
annual_salary=float(input("insert annual salary: "))
monthly_salary=float(annual_salary/12)
total_cost=float(1000000)
down_payment =float(0.25*total_cost)
current_savings=float(0)
semi_annual_raise=float(7/100)
semi_monthly_raise=float(semi_annual_raise/12)
r=float(4/100)
rm=float(r/12)

d=0


high=10000
low=0
guess=(high+low)/2
epsilon=float(1)
proc=float(guess/10000)
portion_saved=float(proc*monthly_salary)
current_savings=float(current_savings+portion_saved+current_savings*rm)
p=float(down_payment - current_savings)


    
    
    
       
    
       
while p>epsilon and (-p)<(-epsilon) :
        d=d+1
        guess=(high+low)/2
        print("guess=",guess)
        proc=float(guess/10000)
        print("proc=",proc)
        for c in range(36):
          print("c=",c) 
           
          
          portion_saved=float(proc*monthly_salary)
          print("portion saved=", portion_saved)
          current_savings=float(current_savings+portion_saved+current_savings*rm)
          print("current savings=",current_savings)
          if c>1 and c%6==0:
            monthly_salary=monthly_salary*(1.0+semi_monthly_raise)
            print("monthly_salary=",monthly_salary)
       
        
       
        
    
        p=float(down_payment - current_savings)
        print("downpayment - current savings=",p)
        print("down_payment=",down_payment)
        
        if p<= epsilon and (-p) >= (-epsilon):
                        break
             
        elif down_payment - current_savings>epsilon :
             low=guess
        else:
             high=guess
             
             
             

   
    
   
if p<= epsilon or (-p) >= (-epsilon):
    print("you will be saving  ", proc," monthly")
else:
    
    print("sllary too small to safe")
    
print(d)

"""

"""
annual_salary=float(input("insert annual salary: "))
monthly_salary=float(annual_salary/12)
total_cost=float(1000000)
down_payment =float(0.25*total_cost)
current_savings=float(0)
semi_annual_raise=float(7/100)
semi_monthly_raise=float(semi_annual_raise/12)
r=float(4/100)
rm=float(r/12)

d=0


high=10000
low=0
guess=(high+low)/2
epsilon=float(100)
proc=float(guess/10000)
portion_saved=float(proc*monthly_salary)
current_savings=float(current_savings+portion_saved+current_savings*rm)
p=float(down_payment - current_savings)


    
    
    
       
    
       
while p>epsilon or p<(-epsilon) :
        d=d+1
        
        print("guess=",guess)
        proc=float(guess/10000)
        print("proc=",proc)
        for c in range(36):
          print("c=",c) 
           
          
          portion_saved=float(proc*monthly_salary)
          print("portion saved=", portion_saved)
          current_savings=float(current_savings+portion_saved+current_savings*rm)
          print("current savings=",current_savings)
          if c>1 and c%6==0:
            monthly_salary=monthly_salary*(1.0+semi_monthly_raise)
            print("monthly_salary=",monthly_salary)
       
        
       
        
    
        p=float(down_payment - current_savings)
        print("downpayment - current savings=",p)
        print("down_payment=",down_payment)
        print("p=",p)
        print("downpayment'",down_payment)
        if p<= epsilon and p >= (-epsilon):
            break
             
        elif down_payment - current_savings>epsilon :
             low=guess
        else:
             high=guess
        guess=(high+low)/2     
             
             

   
    
   
if p<= epsilon and p >= (-epsilon):
    print("you will be saving  ", proc," monthly")
else:
    
    print("sllary too small to safe")
    
print(d)

"""
"""
annual_salary=float(input("insert annual salary: "))
monthly_salary=float(annual_salary/12)
total_cost=float(1000000)
down_payment =float(0.25*total_cost)
current_savings=float(0)
semi_annual_raise=float(7/100)
semi_monthly_raise=float(semi_annual_raise/12)
r=float(4/100)
rm=float(r/12)

d=0


high=10000
low=0
guess=0
epsilon=100
proc=float(guess/10000)
portion_saved=float(proc*monthly_salary)
current_savings=float(0)
p=float(down_payment - current_savings)


    
    
    
       

       
while abs(p)>epsilon :
        d=d+1
        monthly_salary=float(annual_salary/12)
        current_savings=float(0)
        portion_saved=float(proc*monthly_salary)
        
        guess=int((high+low)/2)  
        print("guess=",guess)
        proc=float(guess/10000)
        print("proc=",proc)
        for c in range(36):
          print("c=",c) 
           
          
          portion_saved=float(proc*monthly_salary)
          print("portion saved=", portion_saved)
          current_savings=float(current_savings+portion_saved+current_savings*rm)
          print("current savings=",current_savings)
          if c>1 and c%6==0:
            monthly_salary=monthly_salary*(1.0+semi_monthly_raise)
            print("monthly_salary=",monthly_salary)
       
        
       
        
    
        p=float(down_payment - current_savings)
        print("downpayment - current savings=",p)
        print("down_payment=",down_payment)
        print("p=",p)
        print("downpayment'",down_payment)
        
        
        if p<= epsilon and p >= (-epsilon):
            break
             
        elif p>epsilon :

             low=guess
        else:
             high=guess
           
             
             

   
    
   
if p<= epsilon and p >= (-epsilon):
    print("you will be saving  ", proc," monthly",guess)
else:
    
    print("sllary too small to safe")
    
print(d)


#test

current_savings=float(0)

monthly_salary=float(annual_salary/12)
portion_saved=float(proc*monthly_salary)

for t in range(36):
    portion_saved=float(proc*monthly_salary)
    current_savings=float(current_savings+portion_saved+current_savings*rm)
    if t>1 and t%6==0:
      monthly_salary=monthly_salary*(1.0+semi_monthly_raise)
      
print("down_payment=",down_payment)
print("current savings=",current_savings)
print("delta=",down_payment-current_savings)
"""
annual_salary=float(input("insert annual salary: "))
monthly_salary=float(annual_salary/12)
total_cost=float(1000000)
down_payment =float(0.25*total_cost)
current_savings=float(0)
semi_annual_raise=float(7/100)
semi_monthly_raise=float(semi_annual_raise/12)
r=float(4/100)
rm=float(r/12)

d=0


high=10000
low=0
guess=0
epsilon=100
proc=float(guess/10000)
portion_saved=float(proc*monthly_salary)
current_savings=float(0)
p=float(down_payment - current_savings)


    
    
    
       

       
while abs(p)>epsilon :
        d=d+1
        monthly_salary=float(annual_salary/12)
        current_savings=float(0)
        portion_saved=float(proc*monthly_salary)
        
        guess=int((high+low)/2)  
        print("guess=",guess)
        proc=float(guess/10000)
        print("proc=",proc)
        for c in range(36):
          print("c=",c) 
           
          
          portion_saved=float(proc*monthly_salary)
          print("portion saved=", portion_saved)
          current_savings=float(current_savings+portion_saved+current_savings*rm)
          print("current savings=",current_savings)
          if c>1 and c%6==0:
            monthly_salary=monthly_salary*(1.0+semi_monthly_raise)
            print("monthly_salary=",monthly_salary)
       
        
       
        
    
        p=float(down_payment - current_savings)
        print("downpayment - current savings=",p)
        print("down_payment=",down_payment)
        print("p=",p)
        print("downpayment'",down_payment)
        
        
        if p<= epsilon and p >= (-epsilon):
            break
             
        if p>epsilon and low!=guess:
            
            low=guess
        elif p>epsilon and low==guess:
            break
        elif p<-epsilon and high!=guess:
            high=guess
        else:
             break
             
           
             
             

   
    
   
if p<= epsilon and p >= (-epsilon):
    print("you will be saving  ", proc," monthly",guess)
else:
    
    print("sllary too small to safe")
    
print(d)


#test

current_savings=float(0)

monthly_salary=float(annual_salary/12)
portion_saved=float(proc*monthly_salary)

for t in range(36):
    portion_saved=float(proc*monthly_salary)
    current_savings=float(current_savings+portion_saved+current_savings*rm)
    if t>1 and t%6==0:
      monthly_salary=monthly_salary*(1.0+semi_monthly_raise)
      
print("down_payment=",down_payment)
print("current savings=",current_savings)
print("delta=",down_payment-current_savings)