import random
import math

while True:
    guess_count = 0

    while True:
        try:
            numbers_count = int(input('Из скольки чисел я могу загадывать?\n'))
        except:
            print('Я ожидал увидеть число :(\nПопробуй ввести его снова\n')
            continue

        if numbers_count > 1000 or numbers_count < 5:
            print('Нууу, это слишком! Выбери число в пределах от 5 до 1000, а то не буду играть!\n')
            continue
        else:
            break

    guess_limit = math.floor(math.log(numbers_count, 2))
    number = random.randint(1, numbers_count)
    print('Я загадал число между 1 и {0}. Отгадай его! У тебя ровно {1} попыток.'.format(numbers_count, guess_limit))

    while guess_count < guess_limit:
        while True:
            try:
                guess = int(input('Попытка номер {0}. Ваше число: '.format(guess_count+1)))
                break
            except:
                print('Я ожидал увидеть число :(\nПопробуй ввести его снова\n')
                continue

        guess_count += 1
        if guess < number:
            print('Моё число больше, чем твоё.')

        if guess > number:
            print('Моё число меньше, чем твоё.')

        if guess == number:
            break

    if guess == number:
        print('Прямо в точку! Попыток использовано: {0}'.format(guess_count))
    else:
        print('Попытки закончились! Я загадал {0}'.format(number))

    reply = input('Сыграем снова? (y/n): '.format(number))
    if reply.lower() == 'y' or reply.lower() == 'yes' or reply.lower() == 'да':
        continue
    else:
        break

