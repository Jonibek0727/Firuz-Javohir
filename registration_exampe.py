import re


Mail = r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
Phone = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
Passw = r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'

regist = []

def registr(info,email,phone_num,password):
    di ={"info":info,
        'email':email,
        'phone_num':phone_num,
        'password1':password,
        
    }
    return di

def info():
    print("РЕГИСТРАЦИЯ:\n>>>")
    name = input("ваше имя: ")
    date1 = (input("дата: "))
    m_w = input("пол: ")
   
   
    text = (f'{name}, {date1}, {m_w},')
    return text
def mail():
    email = input("емаил:")
    if  re.search(Mail,email):
        return email
    else:
        mail()
def phone():
    phone_num = input("тел.номер: ")  
    if re.search(Phone,phone_num):
        return phone_num
    else:
        phone()
def passw():
    password = input("пороли: ")
    pass_check = input("повторный пороль: ")
    if re.search(Passw,password):

        if password == pass_check:
            return password
        else:
            print("пороли не совподают")
            passw()
    else:
        print("password is wrong")  
        passw()     
def main():
    a = info()
  #  print(f'добро пожаловать {a}\nпоздровляем вы успешно зарегестрировались.')    
    b = mail()
    c = phone()
    d = passw()
    e =registr(a,b,c,d)
    print(e)
main()