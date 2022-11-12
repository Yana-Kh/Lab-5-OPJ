#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

if __name__ == '__main__':
    c = float(input("Value of с? "))
    if math.fabs(c) < 9:
        if c < 0:
            print("Минус")
        elif c == 0:
            print("Ноль")
        else:
            print("Плюс")
    if math.fabs(c) == 1:
        print("один")
    elif math.fabs(c) == 2:
        print("два")
    elif math.fabs(c) == 3:
        print("три")
    elif math.fabs(c) == 4:
        print("четыре")
    elif math.fabs(c) == 5:
        print("пять")
    elif math.fabs(c) == 6:
        print("шесть")
    elif math.fabs(c) == 7:
        print("семь")
    elif math.fabs(c) == 8:
        print("восемь")
    elif math.fabs(c) == 9:
        print("девять")
    else:
        print("Ошибка")
