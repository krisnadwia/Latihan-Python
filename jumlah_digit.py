from os import system as sistem
sistem("clear")

def countDigit(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count
n = int(input("Masukkan beberapa digit : "))
print("Jumlah digit di atas ada : % d" %(countDigit(n)))