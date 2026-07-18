import string
from password.new_password import generate_password

def test_password_characters():
    valid_characters = (
        string.ascii_letters + string.digits + string.punctuation
    )
    password = generate_password(100)
    for char in password:
        assert char in valid_characters

def test_password_length():
    length = 20
    password = generate_password(length)
    assert len(password) == length

def test_passwords_are_different():
    password1 = generate_password(20)
    password2 = generate_password(20)
    assert password1 != password2

"""
Tambahkan satu atau lebih tes dari pilihan berikut. Atau buat tes kamu sendiri.
Akan lebih bagus jika kamu bisa membuat lebih banyak tes!

Tes untuk memastikan panjang password sesuai dengan yang diminta
Tes untuk memastikan dua password yang dibuat berurutan tidak sama
"""
