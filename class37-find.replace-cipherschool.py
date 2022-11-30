s1='she is very beautiful but she did not notice me i like her'

print(s1.replace(' ',''))
print(s1.replace('she','he',1))

print(s1.find('is'))#jaha se pehla word start he whi show krega
print(s1.find('she')) #0
print(s1.find('but')) #22

print(s1.find("she",3))

v='she is very beautiful but she did not notice me i like her'
a=v.find('she')
print(v.find('she',a+1))

