# Program input angka dengan penanganan error

def input_angka():
    while True:
        try:
            angka = float(input("Masukkan angka: "))
            return angka
        except ValueError:
            print("Input tidak valid. Harus berupa angka.")

# Program utama
print("=== Program Input Angka ===")

nilai = input_angka()

print("Input berhasil")
print("Angka yang dimasukkan:", nilai)