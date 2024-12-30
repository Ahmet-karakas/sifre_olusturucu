karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
import random

def generate_password(numOfchars):
    password = ""
    for i in range(numOfchars):
        password += random.choice(karakterler)
    return password

num_of_letters = int(input("kaç karakterli bir şifre istiyorsun?"))   

password = generate_password(num_of_letters)   

print(password)