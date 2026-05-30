# Program Menu Nilai

def input_data(data):
    try:
        nilai = float(input("Masukkan nilai: "))
        data.append(nilai)
        print("Nilai berhasil ditambahkan.")
    except ValueError:
        print("Input tidak valid.")

def hitung_rata(data):
    if len(data) == 0:
        print("Data kosong.")
    else:
        rata = sum(data) / len(data)
        print("Rata-rata:", rata)

def tampilkan_data(data):
    if len(data) == 0:
        print("Data kosong.")
    else:
        print("Data:", data)

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