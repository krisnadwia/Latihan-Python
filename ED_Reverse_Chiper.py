pesan = input('Masukkan Kata: ')
translated = '' #cipher text is stored in this variable
i = len(pesan) - 1

while i >= 0:
    translated = translated + pesan[i]
    i = i - 1
print('Hasil Reverse Chiper: ', translated)