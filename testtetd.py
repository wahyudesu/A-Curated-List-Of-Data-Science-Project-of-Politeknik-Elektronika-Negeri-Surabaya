data_buku = [
    {
    "Kode Buku" : 8000,
    "judul" : "Laskar Pelangi",
    "penulis" : "Andrea Hirata",
    "tahun terbit" : "2005",
    "harga" : 75000,
    "stok_buku" : 80
    },
    {
    "Kode Buku" : 8001,
    "judul" : "Harry Potter and the Philosopher's Stone",
    "penulis" : "J.K. Rowling",
    "tahun terbit" : "1997",
    "harga" : 100000,
    "stok buku" : 30
    },
    {
    "Kode Buku" : 8002,
    "judul" : "The Hunger Games",
    "penulis" : "J.K. Rowling",
    "tahun terbit" : "2008",
    "harga" : 85000,
    "stok buku" : 70
    },
    {
    "Kode Buku": 8003,
     "judul" : "Pulang",
     "penulis" : "Tere liye",
     "tahun terbit" : "2015",
     "harga" : 89000,
     "stok buku" : 25
     }]

def input_buku():
    global data_buku
    baru_1 = input("Judul: ")
    baru_2 = input("Penulis: ")
    baru_3 = input("Tahun terbit: ")
    baru_4 = int(input("Harga: "))
    baru_5 = int(input("Stok Buku: "))

    kode_buku_saat_ini = len(data_buku) + 8000
    data_baru = {
        "Kode Buku" : kode_buku_saat_ini,
        "judul": baru_1,
        "penulis": baru_2,
        "tahun terbit": baru_3,
        "harga": baru_4,
        "stok buku" : baru_5
    }
    print("="*75)
    data_buku.append(data_baru)

def tampilkan_buku():
    global data_buku
    print("Berikut daftar buku yang tersedia di toko buku kami : ")
    for i in range(len(data_buku)):
        for key, value in data_buku[i].items():
            print(f"{key} = {value}")
        print("="*75)

def cari_buku(kode_buku):
    global data_buku
    for buku in data_buku:
        if buku["Kode Buku"] == kode_buku:
            return buku
    return None  

def update_stok(kode_buku):
    global data_buku
    for i in range(len(data_buku)):
        for key, value in data_buku[i].items():
            if key == "Kode Buku" and value == kode_buku:
                data_buku[i]["stok buku"] = data_buku[i]["stok buku"] - 1

def uang_kembalian(harga_buku, uang_bayar):
    kembalian = uang_bayar - harga_buku
    return kembalian
                
def beli_buku():
    kode_buku = int(input("Masukkan kode buku yang mau dicari: "))
    hasil_pencarian = cari_buku(kode_buku)
    if hasil_pencarian is not None:
        for key, value in hasil_pencarian.items():
            print(f"{key} = {value}")
        konfirmasi = input("Apakah Anda yakin ingin membeli buku tersebut (y/n): ")
        if konfirmasi.lower() == "y":
            judul = hasil_pencarian["judul"]
            harga_buku = hasil_pencarian["harga"]
            stok_sebelum_pembelian = hasil_pencarian["stok buku"]
            if stok_sebelum_pembelian > 0:
                uang_bayar = int(input("Masukkan uang yang dibayar : "))
                if uang_bayar < harga_buku:
                    print("Mohon maaf, uang anda kurang untuk membeli buku ini.")
                else:
                    update_stok(kode_buku)
                    kembalian = uang_kembalian(harga_buku, uang_bayar)
                    sisa_stok = hasil_pencarian["stok buku"]
                    print(f"Pembelian buku dengan judul {judul} telah berhasil")
                    print(f"Uang kembalian anda adalah {kembalian}")
                    print(f"Sisa stok buku: {sisa_stok}")
            else:
                print("Mohon maaf, stok buku habis.")
        elif konfirmasi.lower() == "n":
            print("Baiklah")
        else:
            print("Masukan tidak valid. Harap masukkan 'y' untuk ya atau 'n' untuk tidak.")
        print("=" * 75)
    else:
        print("Buku yang anda cari sedang tidak ada, silahkan datang kembali besok")

def kasir():
    while True:
        print("1. Input Buku")
        print("2. Kembali ke menu")
        print("="*75)
        opsi = input("Masukkan opsi (1/2) : ")
        print("="*75)
        if opsi == "1":
            input_buku()
            tampilkan_buku()
        else:
            break
        print("="*75)
    
def pembeli():
    while True:
        print("1. Tampilkan Buku")
        print("2. Beli Buku")
        print("3. Kembali ke menu")
        print("="*75)
        opsi = input("Masukkan opsi (1/2/3) : ")
        if opsi == "1":
            tampilkan_buku()
            return pembeli()      
        if opsi == "2":
            beli_buku()
        else:
            break
        print("="*75)
        
while True:
    print("="*75)
    print("SELAMAT DATANG DI TOKO BUKU DARISINI")
    print("Silahkan pilih menu dibawah ini")
    print("1. Kasir")
    print("2. Pembeli")
    print("3. Keluar Toko")
    print("="*75)
    opsi = input("Masukkan opsi (1/2/3) : ")
    print("="*75)
    if opsi == "1":
        kasir()
    elif opsi == "2":
        pembeli()
    else:
        print("Terimakasih telah datang ke toko DARISINI")
        print("Datang Kembali yaaa")
        print("Perbanyaklah Literasi, karena Buku jembatan ilmu")
        break
