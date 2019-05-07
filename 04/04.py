# Patrick Canny
# EECS 700 H4
# Miller-Rabin Primality Test Implementation

import os
import math
import random

def miller_rabin(q):
    # if q even != 2 then composite
    if(q % 2 == 0):
        if (q == 2):
            return "Prime"
        return "Composite"
    else:
        r = 0
        s = q-1
        while s % 2 == 0:
            r += 1
            s //= 2
        for _ in range(5):
            a = random.randrange(2, q-1)
            x = pow(a, s, q)
            if x != 1:
                i = 0
                while (x != q-1):
                    if i == r-1:
                        return "Composite"
                    else:
                        i += 1
                        x = (x ** 2) % q
        return "Prime"

print("Ex 1: {}".format(miller_rabin(10601)))
print("Ex 2: {}".format(miller_rabin(101101)))
print("Ex 3: {}".format(miller_rabin(15841)))

