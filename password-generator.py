import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

length = input('password length? \n')
length = int(length)

password = ''
for c in range(length):
    password += random.choice(chars)

f = open("file.txt", "w")
f.write(password)
f.close()

print(password)