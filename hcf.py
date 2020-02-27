def hcf(a,b):
    if a>b:
        small=a
    else:
        small=b
    for i in range(1,small+1):
        if(a%i==0) and (b%i==0):
            hcf=i
    return hcf
a=int(input())
b=int(input())
print(hcf(a,b))