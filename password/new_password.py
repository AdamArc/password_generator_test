import random
import string



def generate_password(length=12):
    """Membuat password acak dengan panjang yang ditentukan."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(length):
        password += random.choice(characters)
    return password

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

# Contoh penggunaan
password_length = 12  # Anda dapat memilih panjang password yang diinginkan
print("Password baru Anda:", generate_password(password_length))