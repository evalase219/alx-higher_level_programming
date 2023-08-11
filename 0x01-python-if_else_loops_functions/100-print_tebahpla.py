#!/usr/bin/python3
# 100-print_tebahpla.py

""""Print the alphabet in reverse order alternating upper- and lower-case."""
let = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - let)), end="")
    let = 32 if let == 0 else 0
