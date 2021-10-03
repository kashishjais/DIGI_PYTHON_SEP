#str find() funtion allows us to pass starting index and end index for use
data='''what are the codes for safe.
how safe is the safe
Is the safe really safe?'''
start_idx=0
for i in range(5):    # use str.count() method for better output
    idx=data.find('safe',start_idx)
    print(f'start found at index {idx}')
    start_idx=idx+1

# or 
start_idx=0
while True:
    idx=data.find('safe',start_idx)
    if idx==-1:
        break
    print(f'start found at index {idx}')
    start_idx=idx+1
    
