# n=input('user name : ')
# i=0
# while i<len(n):
#     print(n[i],':',n.count(n[i]))
#     i+=1

empty=''
n=input('user name : ')
i=0
while i<len(n):
    if n[i] not in empty:
        empty+=n[i]
        print(n[i],':',n.count(n[i]))
    i+=1