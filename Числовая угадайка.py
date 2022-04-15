# -*- coding: utf-8 -*-
# Мини проект №1. "Числовая угадайка"
import random

def game():
    total = 0
    right = 100    
    print("Добро пожаловать в числовую угадайку")
    print('Если хотите ввести правую границу, то введите "Y"')
    print('Если не хотите задавать правую границу, то введите "N", правая граница будет использована по умолчанию "100"')
    YN = YN_valid()
    if YN == "Y":
        print("Для правой границы введите любое целое число")
        right = int(input())
        num = random.randint(1, right)  
        # генерируем случайное число в диапозоне от 1 до right включительно
        vvod(num, total, right)
    elif YN == "N":
        num = random.randint(1, 100)
        vvod(num, total, right)
        
def vvod(num, total, right):
    print("Введите любое целое число от 1 до,", right, "включительно")
    n = is_valid(right)
    while (n != num):
        if n < num:
            print("Ваше число меньше загаданного, попробуйте еще разок")
            total += 1
            n = is_valid(right)
        if n > num:
            print("Ваше число больше загаданного, попробуйте еще разок")
            total += 1
            n = is_valid(right)
        if n == num:
            print('Вы угадали, поздравляем! Это число', n)
            print("Колличество попыток:", total)
            print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
            print('Для повторной игры введите "Y", для выхода "N"')
            YN = YN_valid()
            if YN == "Y":
                game()
            elif YN == "N":
                break
                    
def YN_valid():
    Y_N = input()
    while Y_N.upper() not in "YN":
        print("Неккоректный ввод, попробуйте еще раз")
        Y_N = input()
    if Y_N.upper() == "Y":
        return "Y"
    elif Y_N.upper() == "N":
        return "N"

def is_valid(right):
    n = int(input())
    while n < 1 or n > right:
        print("А может быть все-таки введем целое число от 1 до",right, "?")
        n = int(input())
    else:
        return n
 
game()  
