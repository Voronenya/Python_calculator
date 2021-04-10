while True:
    def add(x, y):
        print(x + y)

    def  sub(x, y):
        print(x - y)

    def multi(x, y):
        print(x * y)

    def div(x, y):
        print(x / y)

    print('Put two numbers for operation:')
    x = int(input())
    y = int(input())

    print('Choose the operation:')
    print('1 - addition', '2 - subtraction', '3 - multiplication', '4 - division')
    i = int(input())

    if i == 1:
        add(x, y)
    elif i == 2:
        sub(x, y)
    elif i == 3:
        multi(x, y)
    elif i == 4:
        div(x, y)
    else:
        print('Operation is incorrect')

    while True:
        answer = str(input('Do you want to continue?\n'))
        if answer in ('yes', 'y', 'n', 'no'):
            break
        print('invalid input')
    if answer == 'yes' or answer == 'y':
        continue
    else:
        print('Goodbye')
        break


