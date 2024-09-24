def calculator():

    num = float(input('What\'s your first number? '))
    off = False
    print('+\n-\n/\n*\n%')
    total = num
    while not off:
        operation = input('Pick an operation: ')
        next_num = float(input('What\'s your next number? '))

        def calcu_info():
            print(f'{total} {operation} {next_num} = ', end='')

        if operation == '+':
            calcu_info()
            total += next_num
            print(f'{total:.1f}')
        elif operation == '-':
            calcu_info()
            total -= next_num
            print(f'{total:.1f}')

        elif operation == '*':
            calcu_info()
            total *= next_num
            print(f'{total:.1f}')
        elif operation == '/':
            calcu_info()
            total /= next_num
            print(f'{total:.1f}')
        elif operation == '%':
            calcu_info()
            total %= next_num
            print(f'{total:.1f}')
        else:
            print('invalid operation!')

        next_calculation = input(
            f'Type \'y\' to continue calculating with {total:.1f}, or type \'n\' to stop calculation: ')

        if next_calculation.lower() == 'y':
            continue
        elif next_calculation.lower() == 'n':
            print('-----------------------')
            print(f'Output : {total}')
            print('-----------------------')
            off = True
        else:
            print('invalid choice!')
            exit()


if __name__ == '__main__':
    calculator()
