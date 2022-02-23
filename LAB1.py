import math

def main():
    coef = input('Введите коэффициенты квадратного уравнения через пробел: ').split()
    l = [int(item) for item in coef]
    D = l[1]**2-4*l[0]*l[2]
    if D >= 0:
        d = round(math.sqrt(D),2)
        x1 = round((-l[1] + d) / (2 * l[0]), 2)
        x2 = round((-l[1] - d) / (2 * l[0]), 2)

        print (f'Решение:\n'
              f'D = b^2-4ac = {l[1]**2}+({-4 * l[0] * l[2]})={D}\n'
              f'Корень из дискриминанта:{d}\n'
              f'x = ({-l[1]}+{d})/(2*{l[0]})\n'
              f'x = ({-l[1]}-{d})/(2*{l[0]})\n'
              f'Корни квадратного уравнения:\nx1:{x1}\nx2:{x2}')
    else:
        print('Дискриминант меньше нуля')
        main()

if __name__== '__main__':
    main()




