from tabulate import tabulate


class Transaction:
    def __init__(self):
        self.items = [] # list kosong untuk menampung daftar item yang diinput


    def add_item(self, name, quantity, price):
        '''
        Fungsi untuk menambahkan item yang dibeli.

        Parameter:
        name (str): nama barang.
        quantity (int): jumlah barang.
        price (float): harga barang.
        '''
        self.items.append({"name": name, "quantity": quantity, "price": price}) # menambah item kedalam list

    def update_item(self, index, name, quantity, price):
        '''
        Fungsi untuk mengganti item yang dibeli.

        Parameter:
        index (int): indeks barang yang akan diganti.
        name (str): nama barang.
        quantity (int): jumlah barang.
        price (float): harga barang.
        '''
        if index < len(self.items): # jika indeks < total item maka nama, quantity, price dapat diganti 
            self.items[index]["name"] = name
            self.items[index]["quantity"] = quantity
            self.items[index]["price"] = price

        else:
            print("Indeks tidak ditemukan")

    def delete_item(self, name):
        '''
        Fungsi untuk menghapus sebuah item.

        Parameter:
        name (str): nama barang.
        '''
        for item in self.items: # loop untuk setiap item dalam list
            if item["name"] == name: # memeriksa apakah ada nama item yang sama
                self.items.remove(item) # menghapus item 
            return True
        return False # tidak ada nama item yang sama

    def reset_transaction(self):
        '''Fungsi untuk menghapus semua item.'''
        self.items = [] # list kembali menjadi kosong

    def check_order(self):
        '''Fungsi untuk mengecek item yang dipesan.'''
        if not self.items: # jika tidak sama dengan list item
            print("Terdapat kesalahan input data.")
        else:
            print("Pesanan anda sudah benar.")
            headers = ["Nama Barang", "Jumlah", "Harga"] # membuat header tabel
            table_data = [[item["name"], item["quantity"], item["price"]] for item in self.items] # memasukkan data ke tabel
            print(tabulate(table_data, headers=headers, tablefmt="grid"))

    def calculate_total_price(self):
        '''Fungsi untuk menghitung total harga.

        Return :
        total_price(float): total harga sebelum diskon
        discount(float): diskon
        discounted_price(float): harga setelah diskon
        '''
        total_price = 0
        for item in self.items: # loop untuk setiap item dalam item list
            price = item["price"] * item["quantity"] # mengalikan harga dengan jumlah item
            total_price += price # menghitung total harga

        discount = 0
        if total_price > 500_000: # jika total harga > 500_000, diskon 0.10
            discount = 0.10

        elif total_price > 300_000: # jika total harga > 300_000, diskon 0.08
            discount = 0.08

        elif total_price > 200_000: # jika total harga > 200_000, diskon 0.05
            discount = 0.05

        discounted_price = total_price - (total_price * discount) # menghitung harga setelah diskon

        print("Total harga belanjaan anda: Rp ", total_price)
        print("Anda mendapat diskon sebesar: ", f"{discount * 100:.2f}%")
        print("Total harga setelah diskon: Rp ", discounted_price)

        return total_price, discounted_price, discount 
