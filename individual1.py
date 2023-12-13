#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Индивидуальное задание №1
# Дано слово. Добавить к нему в начале и конце
# столько звездочек, сколько букв в этом слове.

if __name__ == '__main__':
    word = input("Enter word... ")
    star = len(word)

    star_word = '*' * star + word + '*' * star
    print(star_word)
