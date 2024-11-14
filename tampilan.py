print("Selamat datang di Xra kalkulator")
print("==============")

angka1 = int(input("masukan angka pertama untuk di hitung "))
angka2 = int(input("masukan angka kedua untuk di hitung "))

print("angka pertama adalah", angka1, "dan angka kedua adalah", angka2)
print("==============")
print("ketik 1 untuk tambah")
print("ketik 2 untuk kurang")
print("ketik 3 untuk kali")
print("ketik 4 untuk bagi")

hitung = int(input("masukan operasi hitung "))
print("\t\n")

def tambah(a,b):
    return a+b

def kurang(a,b):
    return a-b

def kali(a,b):
    return a*b

def bagi(a,b):
    return a/b

if hitung == 1:
    hasil = tambah(angka1, angka2)
    print(angka1, "+", angka2, "=", hasil)

elif hitung == 2:
    hasil = kurang(angka1, angka2)
    print(angka1, "-", angka2, "=", hasil)

elif hitung == 3:
    hasil = kali(angka1, angka2)
    print(angka1, "x", angka2, "=", hasil)

elif hitung == 4:
    hasil = bagi(angka1, angka2)
    print(angka1, ":", angka2, "=", hasil)

else:
    print("tolong masukan operasi hitung dengan benar")

print("\t\n")
print("==============")
print("terimakasih telah menggunakan Xra kalkulator, sampai jumpa lagi")