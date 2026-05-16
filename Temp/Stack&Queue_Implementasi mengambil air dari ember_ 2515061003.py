MAX_KAPASITAS = 5
ember_air = []

def push_air(volume_ml):
    """Fungsi untuk memasukkan air ke dalam ember (Push)"""
    n = len(ember_air)

    if n >= MAX_KAPASITAS:
        print(f"Gagal menambah! Air tumpah karena ember sudah mencapai batas {MAX_KAPASITAS} gayung.")
    else:
        ember_air.append(volume_ml)
        print(f"Berhasil memasukkan air sebanyak: {volume_ml} ml.")

def pop_air():
    """Fungsi untuk mengambil air teratas dari ember (Pop)"""
    n = len(ember_air)


    if n == 0:
        print("Gagal mengambil! Ember sudah benar-benar kosong.")
    else:

        air_keluar = ember_air.pop()
        print(f"Berhasil mengambil air lapisan teratas sebanyak: {air_keluar} ml")

def main():
    print("=== SIMULASI KAPASITAS AIR EMBER (STACK ARRAY) ===")

    while True:
        n = len(ember_air)
        print(f"\nKondisi Ember Saat Ini (Total: {n}/{MAX_KAPASITAS} Gayung): {ember_air}")
        print("1. Masukkan Satu Gayung Air (Push)")
        print("2. Ambil Satu Gayung Air (Pop)")
        print("3. Selesai")

        pilihan = input("Pilih tindakan (1/2/3): ").strip()

        if pilihan == "1":
            try:
                volume = int(input("Masukkan volume air gayung tersebut (dalam ml): "))
                if volume > 0:
                    push_air(volume)
                else:
                    print("Volume air harus lebih dari 0 ml!")
            except ValueError:
                print("Input tidak valid, masukkan angka untuk volume air!")

        elif pilihan == "2":
            pop_air()

        elif pilihan == "3":
            print("Simulasi selesai. Air di ember aman!")
            break
        else:
            print("Pilihan tidak valid, silakan pilih 1, 2, or 3!")

if __name__ == "__main__":
    main()
