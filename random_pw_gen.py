import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'

all = lower + upper + numbers
length = 15
password = "".join(random.sample(all, length))
print('Output: ',password)