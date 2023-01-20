# IPython log file

a = 2**65536
print(a)
import sys
sys.set_int_max_str_digits(20000)
print(a)
bin(1234567)
#[Out]# '0b100101101011010000111'
0b00110011 | 0b01000000
#[Out]# 115
bin(115)
#[Out]# '0b1110011'
a = 15
-10 <= a <= 100
#[Out]# True
a = 150
-10 <= a <= 100
#[Out]# False
a <= 100 and a >= -10
#[Out]# False
42 << 34
#[Out]# 721554505728
bin(42)
#[Out]# '0b101010'
0b101010 << 34
#[Out]# 721554505728
bin(0b101010 << 34)
#[Out]# '0b1010100000000000000000000000000000000000'
int(13.8)
#[Out]# 13
int(287.9)
#[Out]# 287
__ceil_(13.888)_
__ceil_(13.888)__
__ceil__(13.888)
import math
__ceil__(13.888)
a = 13.88
a = 13.888
a.__ceil__()
#[Out]# 14
a.__floor__()
#[Out]# 13
math.ceil(a)
#[Out]# 14
math.floor(a)
#[Out]# 13
round(a,2)
#[Out]# 13.89
bin(a)
b = int(a) if ((a - int(a) <= 0.5)) else (int(a) + 1)
b
#[Out]# 14
a = 13.444
b = int(a) if ((a - int(a) <= 0.5)) else (int(a) + 1)
b
#[Out]# 13
exit()
