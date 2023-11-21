import random

karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

panjang = int(input("Panjang Password: "))

password = ""

for i in range(panjang):
    password += random.choice(karakter)

print("Kata sandi yang dihasilkan adalah: ", password)
