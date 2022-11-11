# DFPOS Tools
# Встроенные инструменты DFPOS
import random


# Import

import random
import time

# Code

chars = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ""

def pswdgen(type):
    global chars
    global password

    if type == 1:
        for i in range(8):
            password += random.choice(chars)
        return password
