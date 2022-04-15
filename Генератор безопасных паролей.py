# -*- coding: utf-8 -*-
# Мини проект №3. "Генератор безопасных паролей"
import random

def chars(digit, uppercase_letters, lower_letters, punctuation, letters_del):  # функция в которую запихиваем символы, которые будут для текущего пароля
    if digit == True:
        digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if digit == False:
        digits = []
    if lower_letters == True:
        lower_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    if lower_letters == False:
        lower_letters = []
    if uppercase_letters == True:
        uppercase_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    if uppercase_letters == False:
        uppercase_letters = []
    if punctuation == True:
        punctuation = ["!", "#", "$", "%", "&", "*", "+", "-", "=", "?", "@", "^", "_"]
    if punctuation == False:
        punctuation = []
    if letters_del == True:
        letters_del = ["i", "l", "1", "L", "o", "0", "O"]
        chars = digits + lower_letters + uppercase_letters + punctuation
        for i in range(len(letters_del)):
            if letters_del[i] in chars:
                chars.remove(letters_del[i])
            else:
                continue
        return chars
    if letters_del == False:
        chars = digits + lower_letters + uppercase_letters + punctuation
        return chars    
            
def valid(vopros):
    while vopros != "ДА" and vopros != "НЕТ":
        print('Введите корректный ответ "ДА"/"НЕТ"')
        vopros = input().upper()
    if vopros == "ДА":
        return True
    elif vopros == "НЕТ":
        return False

def valid2(length):
    while length < 5:
        print("Длинна пароля должна быть не менее 5 симвлов")
        print("Длина пароля", "Введите целое число", sep = "\n")
        length = int(input())
    return length
        
def generate_password(length, chars1, parol_nomer):
    parol = list()
    for i in range(length):
        num = random.randint(0, len(chars1) - 1)
        parol.append(chars1[num])
    print("Ваш пароль №", parol_nomer, ":", sep="")
    print(*parol, sep="")
    return parol
  
def vvod(parol_nomer, parol_col):
    print("Вводные параметры для пароля №", parol_nomer, sep="")
    print("Длина пароля", "Введите целое число", sep = "\n") 
    length = valid2(int(input()))
    print('Включать ли цифры: "0123456789"', '"ДА"/"НЕТ"') 
    digit = valid(input().upper())
    print('Включать ли прописные буквы: "ABCDEFGHIJKLMNOPQRSTUVWXYZ"', '"ДА"/"НЕТ"')    
    uppercase_letters = valid(input().upper())
    print('Включать ли строчные буквы буквы: "abcdefghijklmnopqrstuvwxyz"', '"ДА"/"НЕТ"')
    lower_letters = valid(input().upper())
    print('Включать ли символы: "!#$%&*+-=?@^_?"', '"ДА"/"НЕТ"')
    punctuation = valid(input().upper())
    print('Исключать ли неоднозначные символы: "il1Lo0O"', '"ДА"/"НЕТ"')
    letters_del = valid(input().upper())
    chars1 = chars(digit, uppercase_letters, lower_letters, punctuation, letters_del)
    generate_password(length, chars1, parol_nomer)
    if parol_nomer <= parol_col:
        parol_nomer += 1
        return parol_nomer
    elif parol_nomer > parol_col:
        return False


def start():
    print("Добро пожаловать в Генератор безопасных паролей")
    print("Количество паролей для генерации?", "Введите целое число", sep="\n")
    parol_col = int(input())
    parol_nomer = 1
    total = 0
    while parol_nomer <= parol_col:   
        parol_nomer = vvod(parol_nomer, parol_col)
    print("Программа Генератор безопасных паролей, закончила свою работу")

start()