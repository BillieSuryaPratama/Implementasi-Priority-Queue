import csv
import os
import pandas as pd
import datetime as dt

# Data csv
Login = "DataLogin.csv"
MenuMakanan = "MenuMakanan.csv"
Riwayat = "Riwayat.csv"

# Opsi Main Menu
OpsiAdmin = ["1", "2", "3", "4", "5", "6"]
OpsiUser = ["1", "2", "3", "4"]

# Kumpulan Function untuk Class Priority Queue
class PriorityQueue:
    def __init__(self):
        self.ListPesanan = []
        self.countPesanan = 1

    def enqueue(self, MakananPesanan, Prioritas):
        Angka = str(self.countPesanan)
        self.countPesanan += 1
        IDPesanan = "Pesanan " + Angka
        self.ListPesanan.append((Prioritas, (IDPesanan, MakananPesanan)))
        self.ListPesanan.sort(key=lambda x: x[0])

    def dequeue(self):
        if self.is_empty():
            print("Tidak ada Pesanan")
            return
        Prioritas, (IDPesanan, MakananPesanan) = self.ListPesanan.pop(0)
        return IDPesanan, MakananPesanan

    def peek(self):
        if self.is_empty():
            print("Tidak ada Pesanan")
            return -1
        Prioritas, (IDPesanan, MakananPesanan) = self.ListPesanan[0]
        return IDPesanan, MakananPesanan

    def is_empty(self):
        return len(self.ListPesanan) == 0
    
    def show_queue(self):
        if self.is_empty():
            print("Tidak ada Pesanan")
            return
        print("List Pesanan:")
        for idx, (Prioritas, (IDPesanan, MakananPesanan)) in enumerate(self.ListPesanan):
            if Prioritas == 1:
                prioritas_label = "Ekspres"
            elif Prioritas == 2:
                prioritas_label = "Standart"
            print(f"{idx+1}. Prioritas: {prioritas_label}, Order ID: {IDPesanan}, Items: {MakananPesanan}")

# Inisialisasi Priority Queue
Antrian = PriorityQueue()

# Function Clear Terminal
def clear():
    os.system('cls')

# Function Login
def login():
    clear()
    while True:
        role = input("masuk sebagai (admin/user): ")
        role = role.lower()
        if role == "admin":
            break
        elif role == "user":
            break
        else:
            clear()
            print("Role tidak terdefinisi")
    if role == "admin":
        while True:
            username = input("masukan username: ")
            username = username.lower()
            password = input("masukan password: ")
            password = password.lower()
            with open(Login,mode="r") as read:
                reader = csv.reader(read)   
                login_berhasil = False
                for i in reader:
                    if i[0] == role and i[1] == username and i[2] == password:
                        print("Berhasil login sebagai", role)
                        login_berhasil = True
                        break
                if login_berhasil:
                    clear()
                    program_admin()
                    break
                else:
                    clear()
                    print("Login gagal, silahkan ulangi")
                    print("Masuk sebagai",role)

    elif role == "user":
        while True:
            username = input("masukan username: ")
            password = input("masukan password: ")
            with open(Login,mode="r") as read:
                reader = csv.reader(read)   
                login_berhasil = False
                for i in reader:
                    if i[0] == role and i[1] == username and i[2] == password:
                        print("Berhasil login sebagai", role)
                        login_berhasil = True
                        break
                if login_berhasil:
                    clear()
                    program_user()
                    break
                else:
                    clear()
                    print("Login gagal, silahkan ulangi")
                    print("Masuk sebagai",role)


# Function Cek Menu Makanan
def cek_menu_makanan():
    clear()
    menu_makanan = pd.read_csv(MenuMakanan)
    menu_makanan.index = menu_makanan.index + 1
    print(menu_makanan)
    while True:
        btn = input("\nketik 'y' untuk kembali ke menu : ")
        if btn == "y":
            clear()
            break
        else:
            clear()
            menu_makanan = pd.read_csv(MenuMakanan)
            menu_makanan.index = menu_makanan.index + 1
            print(menu_makanan)

# Function Tambah Menu
def tambah_menu():
    clear()
    print("=== Tambah Menu Baru ===")

    try:
        with open(MenuMakanan, mode="r") as file:
            reader = csv.reader(file)
            data = list(reader)
            if len(data) > 1:
                last_id = int(data[-1][0])
            else:
                last_id = 0
    except FileNotFoundError:
        print(f"File {MenuMakanan} tidak ditemukan. Membuat file baru...")
        last_id = 0
    
    new_id = str(last_id + 1).zfill(2)

    nama_menu = input("Masukkan nama menu: ")
    harga_menu = input("Masukkan harga menu: ")

    try:
        harga_menu = float(harga_menu)
    except ValueError:
        clear()
        print("Harga menu harus berupa angka!")
        return
    
    with open(MenuMakanan, mode="a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([new_id, nama_menu, harga_menu])
    
    clear()
    print(f"Menu '{nama_menu}' berhasil ditambahkan dengan ID {new_id} dan harga {harga_menu}.\n")


# Function Update Menu
def update_menu():
    clear()
    print("=== Update Menu Makanan ===")

    menu_makanan = []
    with open(MenuMakanan, mode="r") as file:
        reader = csv.reader(file)
        menu_makanan = list(reader)
    
    if len(menu_makanan) <= 1:
        print("Tidak ada menu untuk diupdate.")
        return

    print("Daftar Menu Makanan:")
    for i, menu in enumerate(menu_makanan):
        if i == 0:  
            print(f"{menu[0]} - {menu[1]} - {menu[2]}")  
            continue
        print(f"{menu[0]} - {menu[1]} - Rp {menu[2]}")
    
    print("\nMasukkan ID menu yang ingin diupdate.")
    id_menu = input("ID Menu: ")
    menu_ditemukan = False  

    for i, menu in enumerate(menu_makanan):
        if i == 0: 
            continue
        if menu[0] == id_menu:
            menu_ditemukan = True  
            print(f"Menu ditemukan: {menu[1]} - Rp {menu[2]}")
            print("1. Update Nama")
            print("2. Update Harga")
            print("3. Update Nama dan Harga")
            pilihan = input("Pilih opsi update (1/2/3): ")

            if pilihan == "1":
                # Update nama menu
                new_name = input("Masukkan nama baru: ")
                menu[1] = new_name
                print(f"Nama menu berhasil diupdate menjadi: {new_name}")
            elif pilihan == "2":
                # Update harga menu
                new_price = input("Masukkan harga baru: ")
                try:
                    menu[2] = str(float(new_price))
                    print(f"Harga menu berhasil diupdate menjadi: Rp {new_price}")
                except ValueError:
                    print("Harga harus berupa angka!")
                    return
            elif pilihan == "3":
                # Update nama dan harga menu
                new_name = input("Masukkan nama baru: ")
                new_price = input("Masukkan harga baru: ")
                try:
                    menu[1] = new_name
                    menu[2] = str(float(new_price))
                    print(f"Nama menu berhasil diupdate menjadi: {new_name}")
                    print(f"Harga menu berhasil diupdate menjadi: Rp {new_price}")
                except ValueError:
                    print("Harga harus berupa angka!")
                    return
            else:
                print("Opsi tidak valid!")
                return

            with open(MenuMakanan, mode="w", newline='') as file:
                writer = csv.writer(file)
                writer.writerows(menu_makanan)
            print("\nMenu berhasil diupdate!")
            break

    if not menu_ditemukan:
        print("\nID menu tidak ditemukan! Pastikan Anda memasukkan ID yang benar.\n")


# Function hapus Menu
def hapus_menu():
    clear()
    print("=== Hapus Menu Makanan ===")

    try:
        with open(MenuMakanan, mode="r") as file:
            reader = csv.reader(file)
            menu_makanan = list(reader)
    except FileNotFoundError:
        print(f"File {MenuMakanan} tidak ditemukan.")
        return

    if len(menu_makanan) <= 1:
        print("Tidak ada menu untuk dihapus.")
        return

    print("Daftar Menu Makanan:")
    for i, menu in enumerate(menu_makanan):
        if i == 0:  
            print(f"{menu[0]} - {menu[1]} - {menu[2]}")
            continue
        print(f"{menu[0]} - {menu[1]} - Rp {menu[2]}")

    print("\nMasukkan ID menu yang ingin dihapus.")
    id_menu = input("ID Menu: ")
    menu_ditemukan = False

    for i, menu in enumerate(menu_makanan):
        if i == 0: 
            continue
        if menu[0] == id_menu:
            menu_ditemukan = True
            print(f"Menu ditemukan: {menu[1]} - Rp {menu[2]}")
            konfirmasi = input("Apakah Anda yakin ingin menghapus menu ini? (y/n): ").lower()
            if konfirmasi == "y":
                menu_makanan.pop(i) 
                print(f"Menu dengan ID {id_menu} berhasil dihapus.")
            else:
                print("Penghapusan dibatalkan.")
            break

    if menu_ditemukan:
        with open(MenuMakanan, mode="w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(menu_makanan)  
        print("\nMenu Makanan Berhasil dihapus.")
    else:
        print("\nID menu tidak ditemukan! Pastikan Anda memasukkan ID yang benar.\n")

# Function UI Main Menu Admin     
def MainMenuAdmin():
    print (' ')
    print (('=') * 50)
    print (' ')
    print("1. Cek Pesanan ")
    print("2. Cek Menu Makanan ")
    print("3. Tambah Menu ")
    print("4. Update Menu ")
    print("5. Hapus Menu ")
    print("6. Log Out")
    print (' ')
    print (('=') * 50)
    print (' ')

# Function UI Main Menu User   
def MainMenuUser():
    print (' ')
    print (('=') * 50)
    print (' ')
    print("1. Pesan Makanan ")
    print("2. Cek Menu Makanan ")
    print("3. Pemesanan Terakhir ")
    print("4. Log Out ")
    print (' ')
    print (('=') * 50)
    print (' ')

# Function Program Admin
def program_admin():
    print("SELAMAT DATANG ADMIN")
    while True :
        MainMenuAdmin()
        pilihan = input("Pilih opsi yang anda inginkan : ")
        if pilihan not in OpsiAdmin:
            while True :
                clear()
                print("Opsi tidak tersedia, silakan pilih opsi lagi !")
                MainMenuAdmin()
                pilihan = input("Pilih opsi yang anda inginkan : ")
                if pilihan in OpsiAdmin:
                    clear()
                    break

        if pilihan in OpsiAdmin:

            if pilihan == "1":
                clear()
                print("Pesanan Saat ini:")
                ID_Pesanan, Makanan = Antrian.peek()
                print(f"{ID_Pesanan}, {Makanan}\n")
                Antrian.show_queue()
                print("\nPilih Opsi Fitur (Masukkan angka sesuai pilihan)")
                while True:
                    print("1. Selesaikan Pesanan")
                    print("2. Kembali\n")
                    input_Antrian = input("Input: ")
                    if input_Antrian == "1":
                        CekAntrian = Antrian.is_empty()
                        if CekAntrian is True:
                            clear()
                            print("Pesanan Saat ini:")
                            ID_Pesanan, Makanan = Antrian.peek()
                            print(f"{ID_Pesanan}, {Makanan}\n")
                            Antrian.show_queue()
                            print("\nPilih Opsi Fitur (Masukkan angka sesuai pilihan)")
                            pass
                        else:
                            clear()
                            IDPesanan, MakananPesanan = Antrian.dequeue()
                            print(f"Pesanan Selesai: {IDPesanan}, Items: {MakananPesanan}\n")
                            print("Pesanan Saat ini:")
                            ID_Pesanan, Makanan = Antrian.peek()
                            print(f"{ID_Pesanan}, {Makanan}\n")
                            Antrian.show_queue()
                            print("\nPilih Opsi Fitur (Masukkan angka sesuai pilihan)")
                    elif input_Antrian == "2":
                        clear()
                        break
                    else: 
                        clear()
                        print("Pesanan Saat ini:")
                        ID_Pesanan, Makanan = Antrian.peek()
                        print(f"{ID_Pesanan}, {Makanan}\n")
                        Antrian.show_queue()
                        print("\nInput Salah")
                        print("\nPilih Opsi Fitur (Masukkan angka sesuai pilihan)")


            if pilihan == "2":
                clear()
                cek_menu_makanan()

            if pilihan == "3":
                clear()
                while True:
                    print (' ')
                    print (('=') * 50)
                    print (' ')
                    print('1. Lanjutkan')
                    print('2. Kembali ke menu utama')
                    print (' ')
                    print (('=') * 50)
                    print (' ')
                    opsi_fitur = input('Pilih opsi yang anda inginkan : ')
                    if opsi_fitur == '1' or opsi_fitur == '2':
                        clear()
                        break
                    else: 
                        clear()
                        print('Opsi tidak tersedia')
                        continue
                if opsi_fitur == '1':
                    tambah_menu()
                elif opsi_fitur == '2':
                    continue

            if pilihan == "4":  
                clear()
                while True:
                    print (' ')
                    print (('=') * 50)
                    print (' ')
                    print('1. Lanjutkan')
                    print('2. Kembali ke menu utama')
                    print (' ')
                    print (('=') * 50)
                    print (' ')
                    opsi_fitur = input('Pilih opsi yang anda inginkan : ')
                    if opsi_fitur == '1' or opsi_fitur == '2':
                        clear()
                        break
                    else: 
                        clear()
                        print('Opsi tidak tersedia')
                        continue
                if opsi_fitur == '1':
                    update_menu()
                elif opsi_fitur == '2':
                    continue

            if pilihan == "5":
                clear()
                while True:
                    print (' ')
                    print (('=') * 50)
                    print (' ')
                    print('1. Lanjutkan')
                    print('2. Kembali ke menu utama')
                    print (' ')
                    print (('=') * 50)
                    print (' ')
                    opsi_fitur = input('Pilih opsi yang anda inginkan : ')
                    if opsi_fitur == '1' or opsi_fitur == '2':
                        clear()
                        break
                    else: 
                        clear()
                        print('Opsi tidak tersedia')
                        continue
                if opsi_fitur == '1':
                    hapus_menu()
                elif opsi_fitur == '2':
                    continue

            
            if pilihan == "6":
                clear()
                print('1. Login')
                print('2. Keluar')
                opsi_akhir = input("Pilih opsi yang anda inginkan : ")
                if opsi_akhir == "1":
                    clear()
                    login()
                    break
                elif opsi_akhir == "2":
                    clear()
                    break
                else:
                    continue
        
# Function Main Menu User    
def program_user():
    print("SELAMAT DATANG USER")
    while True:
        MainMenuUser()
        pilihan = input("Pilih opsi yang anda inginkan : ")
        if pilihan not in OpsiUser:
            while True :
                clear()
                print("Opsi tidak tersedia, silakan pilih opsi lagi !")
                MainMenuUser()
                pilihan = input("Pilih opsi yang anda inginkan : ")
                if pilihan in OpsiUser:
                    clear()
                    break
        if pilihan in OpsiUser:
            if pilihan == "1":
                clear()
                df = pd.read_csv(MenuMakanan)
                pesanan = []
                EksekusiAntrian = []
                print(df.to_string(index=False))
                print("\nPilih Opsi Fitur (Masukkan angka sesuai pilihan)")
                while True:
                    print("1. Tambah Pesanan")
                    print("2. Pembayaran")
                    print("3. Kembali\n")
                    input_Transaksi = input("Input: ")
                    if input_Transaksi == "1":
                        while True:
                            clear()
                            print(df.to_string(index=False))
                            MenuPilihan = int(input("\nPilih ID makanan yang ingin anda pesan (Masukkan ID): "))
                            if MenuPilihan > len(df):
                                pass
                            else:
                                MenuPilihan = MenuPilihan - 1
                                Kuantitas = int(input("Masukkan Kuantitas Pesanan: "))
                                Data = df.iloc[MenuPilihan]
                                RincianNama = Data.iloc[1]
                                RincianHarga = Data.iloc[2]
                                pesanan.append([RincianNama, RincianHarga, Kuantitas])
                                clear()
                                print(df.to_string(index=False))
                                print("")
                                print("Pesanan Saat ini:")
                                print(pesanan)
                                print("\nPilih Opsi Fitur (Masukkan angka sesuai pilihan)")
                                break
                                
                    elif input_Transaksi == "2":
                        if len(pesanan) == 0:
                            clear()
                            print(df.to_string(index=False))
                            print("")
                            print("Belum ada makanan/minuman yang dipesan")
                            print("\nPilih Opsi Fitur (Masukkan angka sesuai pilihan)")
                        else:
                            while True:
                                clear()
                                print("Pesanan Saat ini:")
                                print(pesanan)
                                print("\nPilih Opsi Pelayanan:")
                                print("1. Pelayanan Reguler")   
                                print("2. Pelayanan Ekspres (Tambahan biaya Rp10.000)")
                                print("3. Kembali\n")
                                input_Pembayaran = input("Input: ")
                                if input_Pembayaran == "1":
                                    clear()
                                    Prioritas = 2
                                    Harga = 0
                                    print("Pesanan Saat ini: ")
                                    print(pesanan)
                                    for items in pesanan:
                                        Harga += items[1] * items[2]
                                    print(f"\nBiaya Pembayaran: {Harga}")
                                    print("\nKonfirmasi Pembayaran:")
                                    print("1. Lanjutkan")
                                    print("2. Batal\n")
                                    input_Reguler = input("Input: ")
                                    if input_Reguler == "1":
                                        clear()
                                        for items in pesanan:
                                            NamaMakanan = items[0]
                                            KuantitasMakanan = items[2]
                                            KuantitasMakanan = int(KuantitasMakanan)
                                            EksekusiAntrian.append((NamaMakanan, KuantitasMakanan))
                                        Antrian.enqueue(EksekusiAntrian, Prioritas)
                                        for items in pesanan:
                                            print(items)
                                        pesanan = []
                                        EksekusiAntrian = []
                                        inputPesananBerhasil = input("\nTerimakasih telah memesan, Pesananmu akan segera diproses")
                                        clear()
                                        break
                                    if input_Reguler == "2":
                                        clear()
                                        print(df.to_string(index=False))
                                        print("")
                                        print("Pesanan Saat ini:")
                                        print(pesanan)
                                        print("\nPilih Opsi Fitur (Masukkan angka sesuai pilihan)")
                                        break
                                if input_Pembayaran == "2":
                                    clear()
                                    Prioritas = 1
                                    Harga = 10000
                                    print("Pesanan Saat ini: ")
                                    print(pesanan)
                                    for items in pesanan:
                                        Harga += items[1] * items[2]
                                    print(f"\nBiaya Pembayaran: {Harga}")
                                    print("\nKonfirmasi Pembayaran:")
                                    print("1. Lanjutkan")
                                    print("2. Batal\n")
                                    input_Ekspres = input("Input: ")
                                    if input_Ekspres == "1":
                                        clear()
                                        for items in pesanan:
                                            NamaMakanan = items[0]
                                            KuantitasMakanan = items[2]
                                            KuantitasMakanan = int(KuantitasMakanan)
                                            EksekusiAntrian.append((NamaMakanan, KuantitasMakanan))
                                        Antrian.enqueue(EksekusiAntrian, Prioritas)
                                        for items in pesanan:
                                            print(items)
                                        pesanan = []
                                        EksekusiAntrian = []
                                        inputPesananBerhasil = input("\nTerimakasih telah memesan, Pesananmu akan segera diproses")
                                        clear()
                                        break
                                    if input_Ekspres == "2":
                                        clear()
                                        print(df.to_string(index=False))
                                        print("")
                                        print("Pesanan Saat ini:")
                                        print(pesanan)
                                        print("\nPilih Opsi Fitur (Masukkan angka sesuai pilihan)")
                                        break
                                if input_Pembayaran == "3":
                                    clear()
                                    print(df.to_string(index=False))
                                    print("")
                                    print("Pesanan Saat ini:")
                                    print(pesanan)
                                    print("\nPilih Opsi Fitur (Masukkan angka sesuai pilihan)")
                                    break

                    elif input_Transaksi == "3":
                        clear()
                        pesanan = []
                        break
                    else:
                        if len(pesanan) == 0:
                            clear()
                            df = pd.read_csv(MenuMakanan)
                            print (df.to_string(index=False))
                            print("\nInput Salah\n")
                            print("Pilih Opsi Fitur (Masukkan angka sesuai pilihan)")
                        else:
                            clear()
                            print(df.to_string(index=False))
                            print("")
                            print("Pesanan Saat ini:")
                            print(pesanan)
                            print("\nPilih Opsi Fitur (Masukkan angka sesuai pilihan)")

            if pilihan == "2":
                clear()
                cek_menu_makanan()

            if pilihan == "3":
                pass

            if pilihan == "4":
                clear()
                print('1. Login')
                print('2. Keluar')
                opsi_akhir = input("Pilih opsi yang anda inginkan : ")
                if opsi_akhir == "1":
                    clear()
                    login()
                    break
                elif opsi_akhir == "2":
                    clear()
                    break
                else:
                    continue  

login()