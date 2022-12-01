start_condition = 0
while start_condition != 1:
    print('How many pencils would you like to use:')
    try:
        number = int(input())
    except ValueError:
        print('The number of pencils should be numeric')
    else:
        if number == 0:
            print('The number of pencils should be positive')
        elif number < 0:
            print('The number of pencils should be numeric')
        else:
            start_condition += 1

while start_condition != 2:
    print('Who will be the first (John, Jack):')
    name = input()
    if name != 'John' and name != 'Jack':
        print('Choose between *Name1* and *Name2*')
    else:
        start_condition += 1

while number > 0:
    print('|' * number)
    print(f"{name}'s turn:")
    if name == 'John':
        start_condition = 0
        while start_condition != 1:
            try:
                get = int(input())
            except ValueError:
                print("Possible values: '1', '2' or '3'")
            else:
                if 1 > get or get > 3:
                    print("Possible values: '1', '2' or '3'")
                elif get > number:
                    print('Too many pencils were taken')
                else:
                    number -= get
                    start_condition += 1
        name = 'Jack'
    else:
        b = number / 4
        if b != int(b):
            b = int(b)
            c = 4 * b + 1
        else:
            c = number - 3
        if number - 1 == c or number - 2 == c or number - 3 == c or number in {2, 3, 4}:
            if number == 2:
                number -= 1
                print(1)
            elif number == 3:
                number -= 2
                print(2)
            elif number == 4:
                number -= 3
                print(3)
            else:
                print(number - c)
                number = c
        else:
            number -= 1
            print(1)
        name = 'John'

print(f'{name} won!')
