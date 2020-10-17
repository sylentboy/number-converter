numberList = []

for i in range(5):
    numberList.append((int(input(str(i+1) + '-е число> '))))

print('\nДесятичная|Двоичная|Восьмеричная|Шестнадцатеричная')
for item in numberList:
    print(item, bin(item)[2:], oct(item)[2:], hex(item)[2:].upper())
