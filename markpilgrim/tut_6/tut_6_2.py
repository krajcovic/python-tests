#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re

def base():
    print(re.sub('y$', 'ies', 'vacancy'))
    print(re.sub('y$', 'ies', 'agency'))
    print(re.sub('([^aeiou])y$', r'\1ies', 'vacancy'))


def match_sxz(noun):
    return re.search('[sxz]$', noun)


def apply_sxz(noun):
    return re.sub('$', 'es', noun)


def match_h(noun):
    return re.search('[^aeioudgkprt]h$', noun)


def apply_h(noun):
    return re.sub('$', 'es', noun)


def match_y(noun):
    return re.search('[^aeiou]y$', noun)


def apply_y(noun):
    return re.sub('y$', 'ies', noun)


def match_default(noun):
    return True


def apply_default(noun):
    return noun + 's'


def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)

    def apply_rule(word):
        return re.sub(search, replace, word)

    return matches_rule, apply_rule


# rules = ((match_sxz, apply_sxz), (match_h, apply_h), (match_y, apply_y), (match_default, apply_default))
# patterns = \
#     (
#         ('[sxz]$', '$', 'es'),
#         ('[^aeioudgkprt]h$', '$', 'es'),
#         ('(qu|[^aeiou])y$', 'y$', 'ies'),
#         ('$', '$', 's')
#     )
# rules = [build_match_and_apply_functions(pattern, search, replace) for (pattern, search, replace) in patterns]
rules = []


def rules(rules_filename):
    with open(rules_filename, encoding='utf-8') as pattern_file:
        for line in pattern_file:
            pattern, search, replace = line.split(None, 3)
            # rules.append(build_match_and_apply_functions(pattern, search, replace))
            yield build_match_and_apply_functions(pattern, search, replace)


def plural(noun, rules_filename='plural4-rules.txt'):
    for matches_rule, apply_rule in rules(rules_filename):
        if matches_rule(noun):
            return apply_rule(noun)
    raise ValueError('no matching rule for {0}'.format(noun))


def make_counter(x):
    print('entering make_counter')
    while True:
        yield x
        print('increment x = ', x)
        x += 1


def test_make_counter():
    counter = make_counter(2)
    print(counter)
    next(counter)
    next(counter)
    next(counter)


def fib(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    for n in fib(10000):
        print(n, end=' ')

    print(end='\n')
    print(list(fib(1000)))

    # print(plural('vacancy'))
