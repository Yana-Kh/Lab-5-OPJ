#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

if __name__ == '__main__':
    n = 0
    while n < 3:
        x = float(input("Enter x: "))
        if x % 2 == 0:
            print(f"{x} is even")
        n = n + 1

