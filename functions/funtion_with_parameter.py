def prime_num(n):
    for i in range(2,n):
        if n%i==0:
            print("not prime")
            break
    else:
        print("prime")

print(prime_num(5))
print(prime_num(13))
print(prime_num(23))
print(prime_num(9))
            
