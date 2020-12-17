

def days_power_2(n: int):
    day = 1
    sum = 2
    while sum < n:
        day += 1
        sum += 2 ** day
    return day


def days_next_prime(n: int):
    day = 1
    kilometers = 2
    sum = kilometers
    while sum < n:
        day += 1
        while True:
            kilometers +=1
            if isPrime(kilometers):
                break
        sum += kilometers
    return day


def sportsman_progression_sum(dist: int, increase: int, days: int):
    day = 1
    sum = dist
    if days == 0:
        return 0
    while day<days:
        dist *= 1+increase/100
        day += 1
        sum += dist
    return sum


def sportsman_progression_day(dist: int, increase: int, sum: int):
    day = 1
    while dist < sum:
        dist *= 1 + increase / 100
        day += 1
    return day


def sportsman_progression_all_days(dist: int, increase: int, sum: int):
    day = 1
    c_sum = dist
    while c_sum < sum:
        dist *= 1 + increase / 100
        day += 1
        c_sum += dist
    return day



def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True


def slide_2_1(n: int):
    if n <= 2:
        return 1
    else:
        p1 = 1
        p2 = 1
        for _ in range(3, n+1):
            temp = p1 + p2
            p1 = p2
            p2 = temp
        return p2


def slide_2_2(n: int):
    if n <= 3:
        return 1
    else:
        p1 = 1
        p2 = 1
        p3 = 1
        for _ in range(4, n+1):
            temp = p1 + p2 + p3
            p1 = p2
            p2 = p3
            p3 = temp
        return p3


def slide_2_3(n: int):
    return [i**2 for i in range(1, n+1) if i % 2 == 1]


def slide_2_4(a: int, b: int):
    if a < 1 or b < 1 or b < a:
        return 0, 0
    else:
        sum = 0
        p = 1
        for temp in range(a, b+1):
            sum += temp
            p *= temp
            temp += 1
        return sum, p


def slide_2_5(a: int, b: int):
    if a < 1 or b < 1 or b < a:
        return [], []
    else:
        return [i for i in range(a, b + 1) if i % 2 == 0], [i for i in range(a, b + 1) if i % 2 == 1]


def slide_2_6(old: []):
    return [i for i in old if i > 0], [i for i in old if i < 1]


def draw_rect (w: int, h: int, f: int, c: chr):
    if w<=f*2 or h<=f*2:
        print("Некорректные параметры рамки")
        return
    for _ in range(f):
        print(w*c, end="\n")
    for _ in range(h-2):
        print(f*c+(w-f*2)*" "+f*c, end="\n")
    for _ in range(f):
        print(w*c, end="\n")


if __name__ == '__main__':
    print("Задачи с первого слайда:")
    print("Задача 1")
    print("Я в сумме пробежал более 1000 км, прошло " + str(days_power_2(1000)) + " дней.")
    print("Я в сумме пробежал более 10000 км, прошло " + str(days_power_2(10000)) + " дней.")
    print("Задача 2")
    print("Я в сумме пробежал более 1000 км, прошло " + str(days_next_prime(1000)) + " дней.")
    print("Я в сумме пробежал более 10000 км, прошло " + str(days_next_prime(10000)) + " дней.")
    print("Задача 3")
    print("Я в первый день пробежал 10 км, увеличиваю объём тренировок на 15%, за 30 дней пробегу " + str(sportsman_progression_sum(10, 15, 30)) + " км.")
    print("Задача 4а")
    print("Я в первый день пробежал 10 км, увеличиваю объём тренировок на 10%, буду пробегать больше 20 "
          "км в день через " + str(sportsman_progression_day(10, 10, 20)) + " дней.")
    print("Задача 4б")
    print("Я в первый день пробежал 10 км, увеличиваю объём тренировок на 10%, пробегу суммарно 100 км через " + str(
        sportsman_progression_all_days(10, 10, 100)) + " дней.")

    print("\nЗадачи со второго слайда:")
    print("Задача 1")
    print("7 член последовательности: " + str(slide_2_1(7)))
    print("Задача 2")
    print("10 член последовательности: " + str(slide_2_2(10)))
    print("Задача 3")
    print("Квадраты нечётных чисел до 16: " + str(slide_2_3(16)))
    print("Задача 4")
    print("Дан отрезок от 5 до 12\nСумма всех чисел из отрезка: " + str(slide_2_4(5, 12)[0]) + "\nСумма всех чисел из отрезка: " + str(slide_2_4(5, 12)[1]))
    print("Задача 5")
    print("Дан отрезок от 10 до 55\nВсе чётные числа из отрезка: " + str(slide_2_5(10, 55)[0]) + "\nВсе нечётные числа из отрезка: " + str(slide_2_5(10, 55)[1]))
    old = [5, 70, -8, 9, -7, -12, 10, 1, -1]
    print("Задача 6")
    print("Дан список: " + str(old) + "\nПоложительные элементы списка: " + str(slide_2_6(old)[0]) + "\nОтрицательные элементы списка: " + str(slide_2_6(old)[1]))

    print("\nЗадачи с третьего слайда:")
    print("Задача 1")
    print("Рамка шириной 7 и высотой 8 символов: ")
    draw_rect(7, 8, 1, '#')
    print("Задача 2")
    print("Рамка из символов '^' шириной 10 и высотой 5: ")
    draw_rect(10, 5, 1, '^')
    print("Задача 3")
    print("Рамка из символов '+' толщиной 5 шириной 15 и высотой 13: ")
    draw_rect(15, 13, 5, '+')





