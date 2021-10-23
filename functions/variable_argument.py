def avg(number=[]):
    if number:
        return sum(number)/len(number)


#print(avg(12,34,56,123,45))
#print(avg())
#print(avg(2,4,5))


def stats(*val,action='max'):
    '''
    funtion for doing stats like min, max, sum,avg,count etc
    '''
    if val:
        if action=='max':
            return max(val)
        elif action=='min':
            return min(val)
        elif action=='sum':
            return sum(val)
        elif action=='avg':
            return avg(val)
        elif action=='count':
            return len(val)
        elif action=='all':
            return max(val),min(val),sum(val),avg(val),len(val)
print("calling stats")
print(stats(1,23,45,5,6,6,77,8))
print(stats(1,2,3,3,4,4,5,6,action='count'))   
print(stats(1,2,3,3,4,4,5,6,action='all'))              
