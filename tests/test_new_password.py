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
    expected_length = 100
    password = generate_password(expected_length)
    
    assert len(password) == expected_length, (
        f"Panjang password seharusnya {expected_length}, "
        f"tetapi didapat {len(password)}"
    )

def test_password_uniqueness():
    """Tes untuk memastikan dua password yang dibuat berurutan tidak sama"""
    password1 = generate_password(100)
    password2 = generate_password(100)
    
    assert password1 != password2, "Dua password yang di-generate berurutan tidak boleh sama"

"""
Tambahkan satu atau lebih tes dari pilihan berikut. Atau buat tes kamu sendiri.
Akan lebih bagus jika kamu bisa membuat lebih banyak tes!

Tes untuk memastikan panjang password sesuai dengan yang diminta
Tes untuk memastikan dua password yang dibuat berurutan tidak sama
"""
