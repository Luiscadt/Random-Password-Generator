import random

letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "!@#$%^&*()_+"

unidos = f'{letras}{numeros}{simbolos}'

contraseña = ''.join(random.sample(unidos, 12))

print(contraseña)



























