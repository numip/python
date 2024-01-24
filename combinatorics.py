"""Комбинаторика"""

import numpy as np
import pandas as pd


# Перестановки

def rearrangement(n: int):
    if n < 0:
        n = int(input('Введите число больше 0 '))
        return rearrangement(n)
    elif n <= 1:
        return 1
    else:
        return n * rearrangement(n - 1)


def func():
    try:
        n = int((input('Введите число ')))
        print(rearrangement(n))
    except ValueError:
        print('Попробуй ещё раз')
        func()
    except RecursionError:
        print('Попробуй ещё раз')
        func()


func()




