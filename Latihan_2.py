# Program pembagian dengan penanganan error

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

# Memanggil fungsi
print("=== Program Pembagian ===")
pembagian()