# DFPOS Tools
# Встроенные инструменты DFPOS
import random


# Import

import random
import time

# Code

chars = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ""

print("Вы не можете использовать dfpos_tools без dfpos!")
time.sleep(30)

def pswdgen(type):
    global chars
    global password

    if type == 1:
        for i in range(8):
            password += random.choice(chars)
        return password
