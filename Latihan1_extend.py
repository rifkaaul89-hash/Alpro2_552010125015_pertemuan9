# Fungsi input angka dengan exception
def input_angka():
    while True:
        try:
            angka = float(input("Masukkan angka: "))
            return angka
        except ValueError:
            print("Input tidak valid. Harus berupa angka.")

# Program menu sederhana
while True:
    print("\n=== MENU ===")
    print("1. Input angka")
    print("2. Pembagian dua angka")
    print("3. Keluar")

    try:
        pilihan = int(input("Pilih menu: "))

        if pilihan == 1:
            angka = input_angka()
            print("Angka yang dimasukkan:", angka)

        elif pilihan == 2:
            try:
                a = float(input("Masukkan angka pertama: "))
                b = float(input("Masukkan angka kedua: "))

                hasil = a / b
                print("Hasil pembagian =", hasil)

            except ZeroDivisionError:
                print("Error: Tidak bisa dibagi dengan nol.")

            except ValueError:
                print("Error: Input harus angka.")

        elif pilihan == 3:
            print("Program selesai.")
            break

        else:
            print("Menu tidak tersedia.")

    except ValueError:
        print("Input menu harus berupa angka.")