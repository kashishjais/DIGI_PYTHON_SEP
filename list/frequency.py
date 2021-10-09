text='''I felt happy because I saw the others were happy and because I knew I should feel happy,
 but I wasn’t really happy.'''
words=text.split()
print(words)

max_freq=0
max_occ=''
for item in words:
    count=words.count(item)
    print(f'{item}->{count}')
    if count>max_freq:
        max_freq=count
        max_occ=item
print(f'{max_occ}==>>{max_freq}')        
