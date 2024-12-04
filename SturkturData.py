import csv
import os

data_login = "DataLogin.csv"

def clear():
    os.system('cls')

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
            with open(data_login,mode="r") as read:
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
            with open(data_login,mode="r") as read:
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
                    
def opsi_admin():
    print (' ')
    print (('=') * 50)
    print (' ')
    print("1. Antrian Pesanan ")
    print("2. Antrian Pengiriman ")
    print("3. Menu Makanan ")
    print("4. Tambah Menu ")
    print("5. Update Menu ")
    print("6. Hapus Menu ")
    print("7. Log Out")
    print (' ')
    print (('=') * 50)
    print (' ')

def program_admin():
    print("SELAMAT DATANG ADMIN")
    while True :
        opsi_admin()
        pilihan = input("Pilih opsi yang anda inginkan : ")
        if pilihan != "1" and pilihan != "2" and pilihan != "3" and pilihan != "4" and pilihan != "5" and pilihan != "6" and pilihan != "7":
            while True :
                clear()
                print("Opsi tidak tersedia, silakan pilih opsi lagi !")
                opsi_admin()
                pilihan = input("Pilih opsi yang anda inginkan : ")
                if pilihan == "1" or pilihan == "2" or pilihan == "3" or pilihan == "4" or pilihan == "5" or pilihan == "6" or pilihan == "7":
                    clear()
                    break
        if pilihan == "1" or pilihan == "2" or pilihan == "3" or pilihan == "4" or pilihan == "5" or pilihan == "6" or pilihan == "7":
            if pilihan == "7":
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
        
        
def program_user():
    print("SELAMAT DATANG USER")
    while True:
        print (' ')
        print (('=') * 50)
        print (' ')
        print("1. Pesan Makanan ")
        print("2. Menu Mkanan ")
        print("3. Pemesanan Terakhir ")
        print("4. Log Out ")
        print (' ')
        print (('=') * 50)
        print (' ')
        pilihan = input("Pilih opsi yang anda inginkan : ")
        if pilihan != "1" and pilihan != "2" and pilihan != "3" and pilihan != "4" :
            while True :
                print("Opsi tidak tersedia, silakan pilih opsi lagi !")
                pilihan = input("Pilih opsi yang anda inginkan : ")
                if pilihan == "1" or pilihan == "2" or pilihan == "3" or pilihan == "4":
                    clear()
                    break
        if pilihan == "1" or pilihan == "2" or pilihan == "3" or pilihan == "4":
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