# Fungsi pembagian
def pembagian():
    try:
        a = float(input("Masukkan pembilang: "))
        b = float(input("Masukkan penyebut: "))

        hasil = a / b
        print("Hasil:", hasil)

    except ValueError:
        print("Input harus berupa angka.")

    except ZeroDivisionError:
        print("Tidak boleh membagi dengan nol.")


# Program menu
while True:
    print("\n=== MENU ===")
    print("1. Pembagian")
    print("2. Keluar")

    try:
        pilih = int(input("Pilih menu: "))

        if pilih == 1:
            pembagian()

        elif pilih == 2:
            print("Program selesai.")
            break

        else:
            print("Menu tidak tersedia.")

    except ValueError:
        print("Input menu harus berupa angka.")