import random

number = random.randint(1, 10)
heal = 3
count = 0

while heal > 0:
    heal -= 1
    count += 1
    guess = int(input('guess: '))

    if number == guess:
        print(f'Tebrikler! {count}. defada anca bildin.')
    elif number > guess:
        print('Yukarı')
    else:
        print('Aşağı')

        if heal == 0:
            print(f"Hakkınız bitti. Tutulan sayı: {number}")
