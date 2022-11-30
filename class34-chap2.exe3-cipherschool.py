a=input('users name : ')
b=input('enter a character : ')
print(len(a))
print(a.lower().count(b.lower())) #incasesensitive
print(a.strip().lower().count(b.strip().lower()))