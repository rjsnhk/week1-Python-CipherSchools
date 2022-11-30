name='    rajesh    '
d1='...........'   

# lstrip method
# SPACE REMOVE YE ONLY STRING SIDE KA NO BETWEEN STRING
a=d1+name+d1
print(a)
print(d1+name.lstrip()+d1)
print(d1+name.rstrip()+d1)
print(d1+name.strip()+d1)


n1=' RA   JE  SH  '
# all space remove
print(n1.replace(' ',''))