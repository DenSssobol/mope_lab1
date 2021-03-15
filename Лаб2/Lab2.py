#прошу вибачення за незручності, виникла якась технічна помилка і надіслався не тей код, але в протоколі
#засвідченно цей код та показані результати цієї програми, тому я надіслав пустий файл не для того, щоб встигнути в дедлайн.
from math import *
from random import *

while True:

    m = 5
    max_y = (30 - 18)*10
    min_y = (20 - 18)*10
    min_x_1 = -20
    max_x_1 = 30
    min_x_2 = -35
    max_x_2 = 15

    x_arr = [[-1, 1, -1], [-1, -1, 1]]
    y_arr = []
    for i in range(3):
        ex_arr=[]
        for j in range(m):
            ex_arr.append(randrange(min_y, max_y))
        y_arr.append(ex_arr)

    y_arr_avg = []
    for i in y_arr:
        y_arr_avg.append(sum(i)/len(i))

    sigma = []
    for i in range(3):
        sum_sigma = 0
        for j in range(m):
            sum_sigma += (y_arr[i][j] - y_arr_avg[i]) ** 2
        sigma.append(sum_sigma/m)

    main_sigma = sqrt(2 * (2 * m - 2) / (m * (m - 4)))

    func=[]
    for i in range(3):
        ex = [sigma[int((i + 3) / 2)], sigma[int(i / 2)]]
        func.append(max(ex) / min(ex))

    t=[]
    for i in func:
        t.append(i*(m-2)/m)

    ruv=[]
    for i in t:
        ruv.append(fabs(i-1)/main_sigma)

    m_x1 = sum(x_arr[0]) / 3
    m_x2 = sum(x_arr[1]) / 3
    M = sum(y_arr_avg)/len(y_arr_avg)

    a = [sum([x_arr[0][i]**2 for i in range(3)])/3,
         sum([x_arr[0][i]*x_arr[1][i] for i in range(3)])/3,
         sum([x_arr[1][i] **2 for i in range(3)]) / 3]

    aij = [sum([x_arr[j][i] * y_arr_avg[i] for i in range(3)]) / 3 for j in range(2)]


    def matrix(matr):
        return (matr[0][0] * matr[1][1] * matr[2][2] + matr[0][1] * matr[1][2] * matr[2][0] + matr[1][0] * matr[2][1] * matr[0][2])-\
               (matr[0][2] * matr[1][1] * matr[2][0] + matr[0][1] * matr[1][0] * matr[2][2] + matr[0][0] * matr[1][2] * matr[2][1])


    bz = matrix([[1, m_x1, m_x2], [m_x1, a[0], a[1]], [m_x2, a[1], a[2]]])

    b0ch = matrix([[M, m_x1, m_x2], [aij[0], a[0], a[1]], [aij[1], a[1], a[2]]])
    b1ch = matrix([[1, M, m_x2], [m_x1, aij[0], a[1]], [m_x2, aij[1], a[2]]])
    b2ch = matrix([[1, m_x1, M], [m_x1, a[0], aij[0]], [m_x2, a[1], aij[1]]])

    b0=b0ch/bz
    b1=b1ch/bz
    b2=b2ch/bz

    delta_x1 = fabs(max_x_1 - min_x_1) / 2
    delta_x2 = fabs(max_x_2 - min_x_2) / 2

    x10 = (max_x_1 + min_x_1) / 2
    x20 = (max_x_2 + min_x_2) / 2

    a0 = b0 - b1*x10/delta_x1 - b2*x20/delta_x2
    a1 = b1/delta_x1
    a2 = b2/delta_x2

    b11 = b0 - b1 - b2
    b22 = b0 + b1 - b2
    b33 = b0 - b1 + b2

    a11 = a0 + a1*min_x_1 + a2*min_x_2
    a22 = a0 + a1*max_x_1 + a2*min_x_2
    a33 = a0 + a1*min_x_1 + a2*max_x_2
    if ruv[0] < 2 and ruv[1] < 2 and ruv[2] < 2:break

print("Y(max) = ", round(max_y, 2),"\nY(min) =  ", round(min_y, 2), "\n")

print("Y:", y_arr)
print("Y(сер):", y_arr_avg, "\n")

print("σ²:", [round(sigma[0], 2), round(sigma[1], 2), round(sigma[2], 2)], "\n")

print("F(uv): ", func)
print("O(uv): ", t)
print("R(uv): ", ruv, "\n")

print("mx1 =", round(m_x1, 2), ", mx2 =", round(m_x2, 2), "\n")

print("a:", [round(a[0], 2), round(a[1], 2), round(a[2], 2)])
print("aij:", [round(aij[0], 2), round(aij[1], 2)])
print("b0 = ", round(b0, 2), ", b1 = ", round(b1, 2), ", b2 = ", round(b2, 2), "\n")

print("Нормоване рівняння регресії виглядає так: y = ",round(b0, 2),"+", round(b1, 2),"*x1 +", round(b2, 2), "*x2 \n")


print("Перевірка отриманих результатів:")
print(round(b0, 2), "-", round(b1, 2), "-",round(b2, 2), "=", round(b11, 2))
print(round(b0, 2), "+", round(b1, 2), "-",round(b2, 2), "=", round(b22, 2))
print(round(b0, 2), "-", round(b1, 2), "+",round(b2, 2), "=", round(b33, 2), "\n")

print("a0 = ", round(a0, 2), ", a1 = ", round(a1, 2), ", a2 = ", round(a2, 2), "\n")

print("Натуралізоване рівняння регресії: y = ", round(a0, 2), "+", round(a1, 2), "*x1 +", round(a2, 2), "*x2")
print(round(a0, 2), "+", round(a1, 2), "*", round(min_x_1, 2), "+", round(a2, 2), "*", round(min_x_2, 2), "= ", round(a11, 2))
print(round(a0, 2), "+", round(a1, 2), "*", round(max_x_1, 2), "+", round(a2, 2), "*", round(min_x_2, 2), "= ", round(a22, 2))
print(round(a0, 2), "+", round(a1, 2), "*", round(min_x_1, 2), "+", round(a2, 2), "*", round(max_x_2, 2), "= ", round(a33, 2), "\n")
