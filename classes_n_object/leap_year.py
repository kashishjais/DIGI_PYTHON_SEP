
    
def is_leap(year):
    if year%4==0 and year%100!=0  and year%400==0:
        return True
    elif year%100==0 and year%400!=0:
        return False

for i in range(1900,2021):
    if is_leap(i):
        print('leap year',i)

        
