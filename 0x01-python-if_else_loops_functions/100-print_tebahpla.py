#!/usr/bin/python3
for tebah in range(0, 26):
    char = ord('z') - tebah
    if tebah % 2 == 1:
        char = chr(char + ord("A") - ord("a"))
    else:
        char = chr(char)
    print("{}".format(char), end="")
