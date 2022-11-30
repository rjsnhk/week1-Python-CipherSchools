n=int(input('guess a number'))

num=9

if num==n:
    print('YOU WIN !!!!')
else:
    if num<n:
        print('TOO HIGH')
    else:
        print('TOO LOW')