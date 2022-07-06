#!/bin/python3
import random

psswd = ""
lenn = input('lenght of the password:')
for i in range(0,int(lenn)):
    char = random.randint(41, 126)
    psswd = "".join(psswd+chr(char))
print(psswd)
