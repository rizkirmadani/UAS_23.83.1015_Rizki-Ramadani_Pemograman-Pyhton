import requests

BASE_URL = "http://127.0.0.1:5000/characters"

def display_menu():
    print("\n=== API Client Menu ===")
    print("1. Lihat Semua Karakter")
    print("2. Tambah Karakter")
    print("3. Perbarui Karakter")
    print("4. Hapus Karakter")
    print("5. Keluar")

def get_characters():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        characters = response.json()
        print("\n=== Daftar Karakter ===")
        for char in characters:
            print(f"ID: {char['id']}, Nama: {char['name']}, Level: {char['level']}, Kekuatan: {char['strength']}, Kesehatan: {char['health']}, Mana: {char['mana']}, Kelincahan: {char['agility']}")
    else:
        print("Gagal mengambil data karakter.")

def add_character():
    name = input("Masukkan nama karakter: ")
    level = int(input("Masukkan level karakter: "))
    strength = int(input("Masukkan kekuatan karakter: "))
    health = int(input("Masukkan kesehatan karakter: "))
    mana = int(input("Masukkan mana karakter: "))
    agility = int(input("Masukkan kelincahan karakter: "))
    data = {"name": name, "level": level, "strength": strength, "health": health, "mana": mana, "agility": agility}
    response = requests.post(BASE_URL, json=data)
    if response.status_code == 201:
        print("Karakter berhasil ditambahkan!")
    else:
        print("Gagal menambahkan karakter.")

def update_character():
    char_id = int(input("Masukkan ID karakter yang ingin diperbarui: "))
    name = input("Masukkan nama baru: ")
    level = int(input("Masukkan level baru: "))
    strength = int(input("Masukkan kekuatan baru: "))
    health = int(input("Masukkan kesehatan baru: "))
    mana = int(input("Masukkan mana baru: "))
    agility = int(input("Masukkan kelincahan baru: "))
    data = {"name": name, "level": level, "strength": strength, "health": health, "mana": mana, "agility": agility}
    response = requests.put(f"{BASE_URL}/{char_id}", json=data)
    if response.status_code == 200:
        print("Karakter berhasil diperbarui!")
    else:
        print("Gagal memperbarui karakter.")

def delete_character():
    char_id = int(input("Masukkan ID karakter yang ingin dihapus: "))
    response = requests.delete(f"{BASE_URL}/{char_id}")
    if response.status_code == 200:
        print("Karakter berhasil dihapus!")
    else:
        print("Gagal menghapus karakter.")

def main():
    while True:
        display_menu()
        choice = input("Pilih menu: ")
        if choice == "1":
            get_characters()
        elif choice == "2":
            add_character()
        elif choice == "3":
            update_character()
        elif choice == "4":
            delete_character()
        elif choice == "5":
            print("Terima kasih telah menggunakan aplikasi!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

            

if __name__ == "__main__":
    main()
