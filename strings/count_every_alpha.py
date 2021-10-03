from string import ascii_lowercase
print (ascii_lowercase)
content='''in publishing, art, and communication, content is the information and experiences
 that are directed toward an end-user or audience. Content is something that is to be expressed 
through some medium, as speech, writing or any of various arts'''
num_of_a=content.count('a')
print(f'a occurs {num_of_a} times ')
in_count=content.count('in')
print(f'in  occurs {in_count} times ')

# counting all alphabets in content
max_freq=0
max_freq_letter=''
for letter in ascii_lowercase:
    counter=content.casefold().count(letter)
    print(f'{letter} found {counter} times ')
    if max_freq<counter:
        max_freq=counter
        max_freq_letter=letter
print(f'{max_freq_letter} is found to occur most ie {max_freq} times')


