#Напишите программу для решения квадратного уравнения. 
# Коэффициенты квадратного уравнения пользователь вводит в консоли. 
# Решение уравнения программа должна также выводить в консоль.

def quadratic_equation ():
    print('''
Hello. We can help you solve an equation of the form "ax^2 + bx + c = 0"
Just enter the values of a, b and c below:
    ''')
    while True:
        try:
            a = float(input('Write the coefficients a (a ≠ 0):  '))
            if  a == 0:
                 print ('Error! If a = 0, then the equation is linear, not quadratic, as there is no ax^2 term.')
            else:  
                while True:
                    try:
                        b = float(input('Write the coefficients b:  '))
                        while True:
                            try:
                                c = float(input('Write the coefficients c:  '))
                                d = b**2 - 4*a*c
                                x1 = (-b+d**0.5)/(2*a)
                                x2 = (-b-d**0.5)/(2*a)
                                print (f'Roots: {x1} and {x2}')                               
                            except ValueError:
                                print("Error! This is not a number. Try again.")  
                            break    
                    except ValueError:
                        print("Error! This is not a number. Try again.")  
                    break    
        except ValueError:
            print("Error! This is not a number. Try again.")  
        break    
     

quadratic_equation ()