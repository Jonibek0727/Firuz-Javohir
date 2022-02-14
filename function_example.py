import re

email_cheak = r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
phone_num = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'


mijozlar = []
def mijoz_info(text, email,tel):
    """ Mijoz haqida malumotlarni lugat ko'rinishida qaytaruvchi funksiya"""
    mijoz = {
        'text':text,
        'email':email,
        'telefon':tel
    }
    return mijoz

def info():
    print("Mojoz haqida malumotlarni kiriting: ")
    ism = input("Ism: ")
    familiya = input("Familiya: ")
    tyil = int(input("Tugilgan yili: "))
    tjoy = input("Tugilgan joy: ")
    text = f'{ism} {familiya} {tyil} {tjoy}'
    return text

def cheak_email():
    email = input("Email: ")
    if re.search(email_cheak, email):
        return email
    else:
        cheak_email()

def cheak_phone():
    telefon = input("Telefon raqami: ")
    if re.search(phone_num, telefon):
        return telefon
    else:
        cheak_phone()
def main():
    A = info()
    B = cheak_email()
    C = cheak_phone()

    tetx = mijoz_info(A,B,C)
    for i in tetx.values():
        print(i)

main()
