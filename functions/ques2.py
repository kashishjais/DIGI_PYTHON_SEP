'''use the file from gutenberg to read and count the words and then store the answer 
in a new file '''

from string import punctuation
def occurrence(read_file_path,save_file_path='results.txt'):
    file=open(read_file_path,encoding="utf-8")
    content=file.read()
    file.close()


    for puncs in punctuation:
        content=content.replace(puncs,'')

    words=content.casefold().split()
    print(f"total words-->{len(words)}")



    with open(save_file_path,'w') as file2:
        for i,word in enumerate(set(words)):
            print(f'step{i}')
            count=words.count(word)
            file2.write(f'{word}\t{count}\n')


occurrence('franki.txt')            