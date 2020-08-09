
# https://drive.google.com/file/d/161LFGnOEMykS_NvC9KPaqRCvjw2eqlAk/view?usp=sharing

#Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

n = int(input("Введите трехзначное число: "))

c = n % 10
n = n // 10
b = n % 10
n = n //10

print (f'Сумма натуральных чисел: {n+b+c}\nПроизведение натуральных чисел: {n*b*c}')