# Fungsi input data
def input_data(data):
    try:
        nilai = float(input("Masukkan nilai: "))
        data.append(nilai)
        print("Data berhasil ditambahkan.")

    except ValueError:
        print("Input tidak valid. Harus angka.")


# Fungsi hitung rata-rata
def hitung_rata(data):
    try:
        rata = sum(data) / len(data)
        print("Rata-rata:", rata)

    except ZeroDivisionError:
        print("Data kosong.")


# Fungsi tampilkan data
def tampilkan_data(data):
    print("Data:", data)


# Fungsi menu
def menu():
    data = []

    while True:
        print("\n=== MENU ===")
        print("1. Input Nilai")
        print("2. Hitung Rata-rata")
        print("3. Tampilkan Data")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            input_data(data)

        elif pilihan == "2":
            hitung_rata(data)

        elif pilihan == "3":
            tampilkan_data(data)

        elif pilihan == "4":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid.")


# Menjalankan program
menu()