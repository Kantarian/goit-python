#Домашнее задание#
#Напишите программу, которая будет выполнять простейшие математические операции с числами последовательно принимая от пользователя операнды (числа) и оператор.
# Условия приёмки#
# Приложение работает с целыми и дробными числами.
# Приложение умеет выполнять такие математические операции:
# СЛОЖЕНИЕ (+)
# ВЫЧИТАНИЕ (-)
# УМНОЖЕНИЕ (*)
# ДЕЛЕНИЕ (/)
# Приложение принимает один операнд или один оператор за один цикл запрос-ответ.
# Все операции приложение выполняет по мере поступления одну за одной.
# Приложение выводит результат вычислений когда получает от пользователя =.
# Приложение заканчивает свою работу после того, как выведет результат вычисления.
# Пользователь по очереди вводит числа и операторы.
# Если пользователь вводит оператор два раза подряд, то он получает сообщение об ошибке и может ввести повторно.
# Если пользователь вводит число два раза подряд, то он получает сообщение об ошибке и может ввести повторно.
# Приложение корректно обрабатывает ситуацию некорректного ввода.
class LoginException(Exception):
  pass
c = 1
while c == 1:
    try:
        b = 1
        num_1 = float(input("Please enter the number: ").strip().replace(',','.').replace(' ',''))
        while b == 1:
            try:
                operation = input('''
                Please type in the math operation you would like to complete:
                + for addition
                - for subtraction
                * for multiplication
                / for division
                = for finis
                ''').strip()
                standard_operation = ['+','/','-','*','=']
                if operation not in standard_operation:
                    raise LoginException
                if operation == '=':
                    print(f'Result: {num_1}')
                    a = 0
                    b = 0
                    c = 0
                else:
                    a = 1
                    while a == 1:
                        try:
                            num_2 = float(input('Please enter the number: ').strip().replace(',','.'))
                            if operation == '+':
                                print('{} + {} = '.format(num_1, num_2))
                                print(float(num_1 + num_2))
                                num_1 = num_1 + num_2
                                a = 0

                            elif operation == '-':
                                print('{} - {} = '.format(num_1, num_2))
                                print(float(num_1 - num_2))
                                num_1 = num_1 - num_2
                                a = 0

                            elif operation == '*':
                                print('{} * {} = '.format(num_1, num_2))
                                print(float(num_1 * num_2))
                                num_1 = num_1 * num_2
                                a = 0

                            elif operation == '/':
                                print('{} / {} = '.format(num_1, num_2))
                                print(num_1 / num_2)
                                num_1 = num_1 / num_2
                                a = 0
                        except ValueError:
                            print('Incorrect number')
                        except ZeroDivisionError:
                            print('You can\'t divide by zero')
            except LoginException:
                print('Incorrect operation')
    except ValueError:
        print('Incorrect number')




