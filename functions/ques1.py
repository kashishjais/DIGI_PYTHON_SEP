import file_function as ff
def total(n):
    t=0
    for digit in str(n):
        t+=int(digit)
    ff.writer('totalfile.txt',str(t))

total(12345) 


