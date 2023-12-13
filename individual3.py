#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Индивидуальное задание №2
# Дано предложение. Удалить из него все буквы с.


if __name__ == '__main__':
    s = input("Введите предложение: ")
    r = s.replace('c', '').replace('с', '').replace('C', '').replace('С', '')

    print(f"Your sentence whithout 'c' is {r}")
