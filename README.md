# Final Project Kelompok_2 
**Nama** 1. Zewa Al Varizhy Maneva (23.83.1012) 2. Rizki Ramadani (23.83.1015)

**Kelas** 23TK02

**Mata Kuliah** Pemograman Python


## Laporan Praktikum: CRUD Game API

Proyek ini adalah implementasi API sederhana berbasis Python untuk mengelola data game dengan fitur CRUD (Create, Read, Update, Delete). Proyek memiliki dua bagian utama:

**Server:** Menyediakan API untuk operasi CRUD.

**Client:** Aplikasi yang digunakan untuk mengakses API.


## Isi Proyek

**Folder game_crud**

• **client.py:** Program Python untuk antarmuka client.

• **server.py:** Program Python untuk server API.

• **static:** Folder untuk file statis seperti CSS dan JavaScript.

• **venv:** Virtual environment untuk pengelolaan pustaka Python.

• **pycache:** Folder cache Python untuk mempercepat eksekusi.


## Folder hasil dan cara

• **data base.png:** Gambar struktur database yang digunakan.

• **hasil API.png:** Contoh respons dari API.

• **memanggil Get.png:** Gambar demonstrasi pemanggilan API dengan metode GET.

• **menu client.png:** Tampilan aplikasi client.

• **server.png** Ilustrasi proses server API.

• **xampp.png:** Konfigurasi database menggunakan XAMPP.


## Cara Menggunakan

**1. Persiapan**
   1. Instal Python di komputer Anda.
   2. Aktifkan virtual environment dengan:
      ```bash
      cd game_crud
      source venv/bin/activate  # Linux/MacOS
      venv\Scripts\activate    # Windows
      ```
   3. Instal pustaka yang diperlukan:**
  ```bash
  pip install -r requirements.txt
  ```
**2. Menjalankan Server:**
   1. Jalankan server API dengan perintah berikut:
```bash
python server.py
```
   2. Server berjalan di http://127.0.0.1:5000 (default).

**3. Menjalankan Client**
   1. Jalankan aplikasi client dengan perintah:
```bash
python client.py
```
**4. Menguji API**

Gunakan aplikasi seperti Postman atau browser untuk mencoba endpoint berikut:

**GET /games:** Menampilkan daftar game.

**POST /games:** Menambahkan game baru.

**PUT /games/<id>:** Memperbarui data game berdasarkan ID.

**DELETE /games/<id>:** Menghapus data game berdasarkan ID.


## Hasil yang Didapatkan

**Hasil API:** Semua endpoint API berhasil diuji. Contoh respons dapat dilihat di hasil API.png.

**Database:** Struktur database dijelaskan di data base.png.

**Tampilan Client:** Tampilan antarmuka tersedia di menu client.png.


## Teknologi yang Digunakan

**Python:** Bahasa utama untuk pengembangan & Untuk mendukung tampilan client.

**Flask:** Framework untuk API server.

**XAMPP:** Untuk pengelolaan database.


## Dokumentasi Tambahan

**1. Data Base**
![data base](https://github.com/user-attachments/assets/cfc16705-abc5-4183-833e-8b78116a7f9f)
**Menunjukkan struktur atau diagram database yang digunakan dalam proyek. Gambar ini membantu memahami relasi antar tabel dan data yang disimpan.**

**2. Hasil API**
![hasil API](https://github.com/user-attachments/assets/93db4946-55d9-4a84-96a2-2f33272c5525)
**Screenshot dari respons API saat melakukan pengujian. Gambar ini menunjukkan data yang berhasil dikembalikan server sesuai dengan permintaan.**

**3. Memanggil Get**
![memanggil Get](https://github.com/user-attachments/assets/62f9dcf5-e8c9-42f9-ae20-c85309e8ff3b)
**Menampilkan demonstrasi penggunaan metode GET untuk mengambil data dari API. Gambar ini mungkin berisi tool seperti Postman atau curl.**

**4. Menu Client**
![menu client](https://github.com/user-attachments/assets/c04f5ab4-47cb-4bf3-beae-09751d84dd78)
**Tampilan antarmuka aplikasi client. Gambar ini memperlihatkan bagaimana user dapat berinteraksi dengan data yang disediakan API.**

**5. Server**
![server](https://github.com/user-attachments/assets/6478acb1-0504-4ee3-8e81-fc0edb9e3642)
**Ilustrasi dari proses server, seperti bagaimana server berjalan atau menangani permintaan dari client.**

**6. XAMPP**
![xampp](https://github.com/user-attachments/assets/02fe6ae7-9ae9-470f-aba4-c6b3876fab60)
**Menampilkan konfigurasi XAMPP yang digunakan untuk mengelola database. Gambar ini menunjukkan detail seperti nama database, tabel, atau pengaturan lain yang relevan.**

**7. Code Server**
![server](https://github.com/user-attachments/assets/3f3d0acd-c814-4726-8ee6-e7ddaa9c4b0f)

**8. Code Client**
![client](https://github.com/user-attachments/assets/beaba9ec-88db-4e3b-8f78-7d46c4c90b07)

**9. Code Swagger**
![swagger,json](https://github.com/user-attachments/assets/3fc3dcf6-6c4a-47f4-b7c3-215a8999f606)
