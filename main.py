from method import Transaction

def main():
    '''Fungsi membuat objek dari class.'''
    trnsct_123 = Transaction()

    while True:
        print("----------------------------------")
        print("===== Super Cashier Program =====")
        print("1. Menambahkan Barang")
        print("2. Mengganti Barang")
        print("3. Menghapus Barang")
        print("4. Reset Daftar Belanja")
        print("5. Cek Daftar Belanja")
        print("6. Selesai")
        print("----------------------------------")

        choice = input("Masukkan angka untuk memilih: ") # menentukan pilihan melalui input

        if choice == '1':
            while True: 
                try:
                    name = input("Masukkan nama barang (ketik 'selesai' untuk keluar): ")
                    if name.lower() == 'selesai': # mengganti input ke huruf kecil 
                        break 
                    quantity = int(input("Masukkan jumlah barang: "))
                    price = float(input("Masukkan harga barang: "))
                    trnsct_123.add_item(name, quantity, price) # memanggil fungsi add_item
                    print(f"Barang berhasil ditambahkan : {name}, {quantity} pcs, Rp {price}")
                except ValueError:
                    print("Input salah! Masukkan harga dan jumlah barang dengan benar.")

        elif choice == '2':
            try:
                index = int(input("Masukkan indeks barang yang ingin diganti: "))
                if index < 0 or index >= len(trnsct_123.items):
                    raise IndexError("Indeks tidak ditemukan! Masukkan indeks dengan benar.")
                name = input("Masukkan nama barang baru: ")
                quantity = int(input("Masukkan jumlah barang baru: "))
                price = float(input("Masukkan harga barang baru: "))
                trnsct_123.update_item(index, name, quantity, price) # memanggil fungsi update_item
                print(f"Barang berhasil diganti: {name}, {quantity} pcs, Rp {price}")
            except ValueError:
                print("Error! Masukkan harga dan jumlah barang dengan benar.")

        elif choice == '3':
            try:
                name = input("Masukkan nama barang yang ingin dihapus: ")
                if trnsct_123.delete_item(name): # memanggil fungsi delete_item
                    print(f"Barang {name} berhasil dihapus.")
            except ValueError:
                print("Item not found!")

        elif choice == '4':
            trnsct_123.reset_transaction() # memanggil fungsi delete_item
            print("Semua daftar belanjaan berhasil dihapus.")

        elif choice == '5':
            trnsct_123.check_order() # memanggil fungsi check_order
            trnsct_123.calculate_total_price() # memanggil fungsi calculate_total_price

        elif choice == '6':
            print("Terima kasih telah menggunakan Super Cashier.")
            break # program selesai

        else:
            print("Pilihan tidak ada. Silakan coba lagi.")

if __name__ == '__main__': # agar fungsi main() dipanggil otomatis saat file dibuka
    main()