worked_hours = int(input("enter the numbers of worked hours : "))
if (worked_hours < 40):
    pay = 10*worked_hours
if(worked_hours > 40):    
        pay = (10*worked_hours + 5*(worked_hours-40))
print(f"the employee worked for {worked_hours} hours and earned {pay} $ ")        
   