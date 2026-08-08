import string
from password.new_password import generate_password

def test_password_characters():
    """Tes untuk memastikan hanya karakter yang diizinkan yang digunakan dalam pembuatan password"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Membuat password yang panjang untuk pengujian yang lebih akurat
    for char in password:
        assert char in valid_characters

"""
Tambahkan satu atau lebih tes dari pilihan berikut. Atau buat tes kamu sendiri.
Akan lebih bagus jika kamu bisa membuat lebih banyak tes!

Tes untuk memastikan panjang password sesuai dengan yang diminta
Tes untuk memastikan dua password yang dibuat berurutan tidak sama
"""

def test_password_long():
    password = generate_password(50)  # Membuat password yang panjang untuk pengujian yang lebih akurat
    assert len(password) == 50

def test_password_diff():
    password = generate_password(50)
    password2 = generate_password(50)  # Membuat password yang panjang untuk pengujian yang lebih akurat
    assert password != password2


