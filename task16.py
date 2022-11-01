def F(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return n + F(n - 1)
    elif (n > 1) and (n % 2 == 1):
        return 2 * F(n - 2)

print(F(26))







































'''
answer = 0

for n10 in range(4096, 32767 + 1):
    n8  = oct(n10)[2:]
    cnt = n8.count('6')
    f = True
    if cnt == 1:
        ind = n8.find('6')        
        if ind == 0:
            if int(n8[1]) % 2 == 1:
                f = False                
        elif ind == 4:
            if int(n8[3]) % 2 == 1:
                f = False
        else:
            if int(n8[ind-1]) % 2 == 1 or int(n8[ind+1]) % 2 == 1:
                f = False
        if f:
            answer += 1

print(answer)
'''    
