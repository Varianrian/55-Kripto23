# Nama		: Varian Avila Faldi
# NPM		: 140810210055
# Kelas		: A
# Tanggal	: 24 September 2023
# Deskripsi	: Program enkripsi dan dekripsi dengan metode shift cipher

def enkripsi(teks, key):
    cipher = ''
    for karakter in teks:
        if karakter == ' ':
            cipher = cipher + karakter
        elif karakter.isupper():
            cipher = cipher + chr((ord(karakter) + key - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(karakter) + key - 97) % 26 + 97)
    return cipher
  
def dekripsi(cipher, key):
    plainteks = ''
    for karakter in cipher:
        if karakter == ' ':
            plainteks = plainteks + karakter
        elif karakter.isupper():
            plainteks = plainteks + chr((ord(karakter) - key - 65) % 26 + 65)
        else:
            plainteks = plainteks + chr((ord(karakter) - key - 97) % 26 + 97)
    return plainteks
  
def main():
    teks = input('Masukkan teks: ')
    key = int(input('Masukkan key: '))
    print('Teks: ', teks)
    print('Key: ', key)
    cipher = enkripsi(teks, key)
    print('Enkripsi: ', cipher)
    print('Dekripsi: ', dekripsi(cipher, key))
    
if __name__ == '__main__':
    main()
