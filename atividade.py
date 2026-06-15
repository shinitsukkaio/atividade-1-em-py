count = 0
divide = []
num = int(input("Digite um numero: "))

for i in range(1, num + 1):
    if num % i == 0:
        print('\033[32m', end='')
        count += 1
        divide.append(i)

    else:
        print('\033[33m', end='')
    print(f'{i} ', end='')
print(f'\n\033[m0 numero {num} foi divisivel {count}.')

print(f'divisores de {num}: {divide}')

print(f'{num} é primo. ' if len(divide) == 2 else f'{num} não é primo. ')