content='''in publishing, art, and communication, content is the information and experiences
 that are directed toward an end-user or audience. Content is something that is to be expressed 
through some medium, as speech, writing or any of various arts
in publishing, art, and communication, content is the information and experiences
 that are directed toward an end-user or audience. Content is something that is to be expressed 
through some medium, as speech, writing or any of various arts'''
vowels='aeiou'
for vowel in vowels:
    c=content.casefold().count(vowel)
    print(f'{vowel}-->{c} times')
    