#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Индивидуальное задание повышенной сложности
# Даны два слова. Для каждой буквы первого слова (в том числе
# для повторяющихся в этом слове букв) определить, входит ли
# она во второе слово. Например, если заданные слова информация
# и процессор, то для букв первого из них ответом должно быть:
# нет нет нет да да нет нет да нет нет.

import sys

if __name__ == '__main__':
    word1 = input("Enter first word... ")
    word2 = input("Enter second word... ")

    if len(word1) == 0 or len(word2) == 0:
        print("Incorrect enter!", file=sys.stderr)
        exit(1)

    for char in word1:
        if char in word2:
            print("да", end=' ')
        else:
            print("нет", end=' ')
