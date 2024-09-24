binCode = input('Enter binary code of a number : ') # 101
decNum = 0
power = 0

for i in range(len(binCode)-1,-1,-1):
    if int(binCode[i])==0:
        power += 1
        continue
    else:
        decNum = decNum + (2 ** power)
        power += 1

print(f'The decimal number of {binCode} is {decNum}.')