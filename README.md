# Self Cashier Program
Program self-cashier untuk tugas Python Course di Pacmann.

## Latar Belakang
Andi perlu membuat sistem kasir self-service sehingga customer yang tidak berada di kota tersebut dapat membeli barang di supermarket miliknya. 

## Tujuan
Membuat sistem kasir self-service sehingga customer dapat melakukan input belanjaan dan kelengkapannya sendiri. 

## Persyaratan
- customer dapat memasukkan nama item, jumlah item, dan harga item yang ingin dibeli
- customer dapat mengganti nama item, jumlah item, dan harga item tanpa menghapus itemnya
- customer dapat menghapus item belanjaan maupun mereset daftar belanja
- customer dapat memeriksa daftar belanjaan
- customer dapat melihat total belanja dan harga yang harus dibayarkan sesuai dengan ketentuan diskon

## Fitur
- menambahkan input nama item, jumlah item, dan harga item ke dalam list
- mengupdate nama item, jumlah item, dan harga item
- menghapus salah satu item
- mereset daftar belanjaan
- mengecek kembali daftar belanjaan
- menghitung total belanjaan
  
![feature](https://github.com/annpam/super-cashier/assets/124033328/4635b036-1b4b-4aa0-9cc8-af9fc7651b4f)  

## Alur Program 
- Program dimulai dengan menjalankan main.py
- Program membuat objek dari class, yaitu trnsct_123 = Transaction (). 
- Program memasuki loop (while) yang berjalan selama kondisi True, sehingga program dapat terus berjalan sampai pengguna selesai menggunakan program.
- Di dalam loop, program menampilkan menu pilihan kepada pengguna. Menu ini didasarkan pada fitur yang direncanakan sebelumnya, yaitu opsi untuk menambah item, mengganti item, menghapus item, mereset daftar belanja, mengecek daftar belanja, menghitung total belanja, dan terakhir keluar dari program.
- Pengguna diminta untuk memasukkan pilihan berupa angka melalui input. Pilihan ini menggunakan method choice. 
- Setelah pilihan dimasukkan, program menggunakan method if-elif-else untuk menentukan fitur yang akan dijalankan.
- Jika pengguna memilih 1 (Menambahkan Barang), program meminta pengguna untuk memasukkan nama barang, harga barang, dan jumlah barang. Selanjutnya, input ini kemudian digunakan dalam fungsi add_item dengan menggunakan perintah trnsct_123.add_item(name, quantity, price). Fungsi ini akan menambahkan barang ke daftar transaksi.
- Jika pengguna memilih 2 (Mengganti Barang), program meminta pengguna untuk memasukkan index barang yang ingin diganti, lalu memasukkan nama. jumlah, dan harga barang yang ingin diganti. Fungsi yang digunakan adalah trnsct_123.update_item(index, name, quantity, price). Fungsi ini akan mengupdate barang berdasarkan indexnya. 
- Jika pengguna memilih 3 (Menghapus Barang), program akan meminta pengguna untuk memasukkan nama barang yang ingin dihapus. Fungsi yang digunakan adalah trnsct_123.delete_item(name), fungsi ini akan menghapus barang berdasarkan nama barangnya. 
- Jika pengguna memilih 4 (Reset Daftar Belanja), maka semua daftar belanjaan akan dihapus menggunakan fungsi trnsct_123.reset_transaction().
- Jika pengguna memilih 5 (Periksa Daftar Belanja), maka semua daftar belanjaan yang sudah masuk akan ditampilkan, sehingga pengguna bisa memeriksa apakah belanjaan sudah sesuai atau belum dan menampilkan total harga. Fungsi yang digunakan untuk memanggil daftar belanja adalah trnsct_123.check_order() dan trnsct_123.calculate_total_price()..
- Jika pengguna memilih 6 (Selesai), maka program akan keluar dari loop menggunakan break dan program selesai. 

## Penjelasan Fungsi 
Penjelasan dari tiap fungsi dalam file method.py

```
 def add_item(self, name, quantity, price):
        '''
        Fungsi untuk menambahkan item yang dibeli.

        Parameter:
        name (str): nama barang.
        quantity (int): jumlah barang.
        price (float): harga barang.
        '''
        self.items.append({"name": name, "quantity": quantity, "price": price})
```

```
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
```

```
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
```

```
 def reset_transaction(self):
        '''Fungsi untuk menghapus semua item.'''
        self.items = [] # list kembali menjadi kosong

```

```
def check_order(self):
        '''Fungsi untuk mengecek item yang dipesan.'''
        if not self.items: # jika tidak sama dengan list item
            print("Terdapat kesalahan input data.")
        else:
            print("Pesanan anda sudah benar.")
            headers = ["Nama Barang", "Jumlah", "Harga"] # membuat header tabel
            table_data = [[item["name"], item["quantity"], item["price"]] for item in self.items] # memasukkan data ke tabel
            print(tabulate(table_data, headers=headers, tablefmt="grid"))

```

```
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
```

## Contoh Output
Berikut ini adalah contoh output program yang dijalankan lewat command prompt.

- Menu awal

  ![menu](https://github.com/annpam/super-cashier/assets/124033328/032834f3-5298-43ea-8f37-ffc49ee1da3e)

- Test 1
  
  ![add_item](https://github.com/annpam/super-cashier/assets/124033328/10d94662-3ce0-4967-a424-812677f6d0ff)

- Test 2
  
  ![delete_item](https://github.com/annpam/super-cashier/assets/124033328/fe39766a-576f-4e7a-b194-5bfbf17ae8b6)

- Test 3

  ![reset_item](https://github.com/annpam/super-cashier/assets/124033328/ffa79afb-b0ce-4747-a539-bfd2592193d4)

- Test 4
  
  ![check_price](https://github.com/annpam/super-cashier/assets/124033328/aded5213-091d-460f-af55-77a36c66edb3)


## Conclusion
- Program ini merupakan program self-cashier yang inputnya dapat dilakukan oleh customer sendiri.
- Untuk ke depannya, dapat dilakukan penyederhanaan alur agar customer tidak harus kembali ke menu awal untuk memilih menu.

