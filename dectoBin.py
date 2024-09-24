num = int(input('Enter a decimal number : '))
rem = 0

binary = []
binary.append(num)
while(num>=1):
    rem = num % 2
    num = num // 2
    binary.append(rem)

print(f'Binary code of {binary[0]} is',end=' ')
for i in range(len(binary)-1,0,-1):
    print(binary[i],end='')
    