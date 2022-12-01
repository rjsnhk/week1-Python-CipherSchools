n=input('enter a number: ')
sum=0
i=0
while i<=len(n)-1:
    sum=int(n[i])+sum
    i+=1
print(sum)