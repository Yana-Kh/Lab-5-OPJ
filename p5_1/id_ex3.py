#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

if __name__ == '__main__':
    n = 0
    money = 100
    nb = 0
    nk = 0
    nt = 0
    while n < 100 and money > 0:
        while money > 80:
            money -= 10
            nb += 1
            n += 1
        while money > 50:
            money -= 5
            nk += 1
            n += 1
        money -= 0.5
        nt += 1
        n += 1
    print(f"You can bay {nb} bull(s), {nk} cow(s) and {nt} calve(s) {n}")