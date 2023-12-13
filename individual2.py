#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Индивидуальное задание №2
# Даны два слова. Определить, сколько начальных букв первого слова совпадает
# с начальными буквами второго слова. Рассмотреть два случая:
# - известно, что слова разные;
# - слова могут быть одинаковыми.

import sys

if __name__ == '__main__':
    word1 = input("Enter first word... ")
    word2 = input("Enter second word... ")

    if len(word1) == 0 or len(word2) == 0:
        print("Incorrect enter!", file=sys.stderr)
        exit(1)

    min_length = min(len(word1), len(word2))
    count = 0

    for i in range(min_length):
        if word1[i] == word2[i]:
            count += 1
        else:
            break
    if len(word1) == len(word2) and count == min_length:
        print("These words are the same!")
    else:
        print(f"The number of matching initial letters in words is {count}.")
