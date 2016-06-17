#!/usr/bin/env python3

a_tuple = ("a", "b", "mpilgrim", "z", "example")
print(a_tuple)

print(a_tuple.index("example"))
print("z" in a_tuple)


v = ('a', 2, True)
(x, y, z) = v
print(x, y, z)

(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7)
print(SUNDAY)