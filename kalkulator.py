# Fungsi untuk menjumlahkan dua angka
def tambah(x, y):
    return x + y

# Fungsi untuk mengurangi dua angka
def kurang(x, y):
    return x - y

# Fungsi untuk mengalikan dua angka
def kali(x, y):
    return x * y

# Fungsi untuk membagi dua angka
def bagi(x, y):
    return x / y

# Tampilan menu untuk pengguna
print("Pilih operasi:")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")

# Input dari pengguna
pilihan = input("Masukkan pilihan (1/2/3/4): ")

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

if pilihan == '1':
    print(f"Hasil: {tambah(angka1, angka2)}")
elif pilihan == '2':
    print(f"Hasil: {kurang(angka1, angka2)}")
elif pilihan == '3':
    print(f"Hasil: {kali(angka1, angka2)}")
elif pilihan == '4':
    print(f"Hasil: {bagi(angka1, angka2)}")
else:
    print("Pilihan tidak valid!")
