import string
from password.new_password import generate_password

def test_password_characters():
    """Tes untuk memastikan hanya karakter yang diizinkan yang digunakan dalam pembuatan password"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Membuat password yang panjang untuk pengujian yang lebih akurat
    for char in password:
        assert char in valid_characters

#Tambahkan satu atau lebih tes dari pilihan berikut. Atau buat tes kamu sendiri. Akan lebih bagus jika kamu bisa membuat lebih banyak tes!

#Tes untuk memastikan panjang password sesuai dengan yang diminta
def test_password_length():
 lengths_to_test = [8, 12, 16, 32]
 for length in lengths_to_test:
        password = generate_password(length)
        assert len(password) == length, f"Gagal: Panjang password harus {length}, tetapi menghasilkan {len(password)}"


#Tes untuk memastikan dua password yang dibuat berurutan tidak sama
def test_password_different():
    password_1 = generate_password(16)
    password_2 = generate_password(16)
    assert password_1 != password_2, "Gagal: Dua password yang dibuat berurutan menghasilkan nilai yang sama"
