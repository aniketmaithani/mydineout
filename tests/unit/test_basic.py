# -*- coding: utf-8 -*-
# @Author: Aniket Maithani
# @Date:   2020-06-14 14:45:46
# @Last Modified by:   Aniket Maithani
# @Last Modified time: 2020-06-14 14:46:34
def add(a, b):
    c = a + b
    return c


def test_add_function():
    addition_output = add(3, 4)
    assert addition_output == 7
