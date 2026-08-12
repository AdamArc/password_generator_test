import string
from password.new_password import generate_password



def test_password_characters():
    """Tes untuk memastikan hanya karakter yang diizinkan yang digunakan dalam pembuatan password"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Membuat password yang panjang untuk pengujian yang lebih akurat
    for char in password:
        assert char in valid_characters

def test_password_length():
    """Tes untuk memastikan panjang password sesuai dengan yang diminta"""
    length = 16
    password = generate_password(length)
    assert len(password) == length

def test_password_uniqueness():
    """Tes untuk memastikan dua password yang dibuat berurutan tidak sama"""
    password1 = generate_password(12)
    password2 = generate_password(12)
    assert password1 != password2


"""

Tambahkan satu atau lebih tes dari pilihan berikut. Atau buat tes kamu sendiri.

Akan lebih bagus jika kamu bisa membuat lebih banyak tes!



Tes untuk memastikan panjang password sesuai dengan yang diminta

Tes untuk memastikan dua password yang dibuat berurutan tidak sama

""" 

