#!/usr/bin/env python3
import fractions


def is_it_true(anything):
    if anything:
        print(anything, "\t\t= yes, it's true")
    else:
        print(anything, "\t\t= no, it's false")

is_it_true(1)
is_it_true(-1)
is_it_true(0)
is_it_true(fractions.Fraction(1, 2))