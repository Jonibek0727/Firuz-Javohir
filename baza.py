ism =[]
yosh = []
ps = []
inn =[]
manzil = []
foto = []
maxsus_belgilar = []

while True:
    baza = int(input("Bazani tuldirush uchun 1 ni bosing: Bazani qidirish uchun 2 ni bosing: ")) #sorov uyushtirdim
    if baza == 1:
        
        N = 1
        while True:

            Ism = str(input(f"{N}-Ismizni kiriting: "))
            if Ism == "stop":
                break
        
            ism.append(Ism)
            Yosh = int(input(f"{N}-Yoshizni kiriting: "))
            yosh.append(Yosh)
            Ps = str(input(f"{N}-Pasport seriya: "))
            ps.append(Ps)
            Inn = int(input(f"{N}-Inn: "))
            inn.append(Inn)
            Manzil = str(input(f"{N}-Manzil: "))
            manzil.append(Manzil.capitalize())
            Foto = str(input(f"{N}-Foto: "))
            foto.append(Foto)
            Maxsus_belgi = str(input(f"{N}-Maxsus belgisi: "))
            maxsus_belgilar.append(Maxsus_belgi)
            N += 1
        print(ism,yosh,ps,manzil)

    elif baza == 2:

        qidiruv = int(input("Umumiy qidiruv 1:\Tuman buyicha qidiruv 2:\n "))
        if qidiruv == 1:
            a = 1
            for i in range(len(Ism)):
                print(f"{a}-{ism[i]} {yosh[i]} {ps[i]} {inn[i]} {manzil[i]} {foto[i]} {maxsus_belgilar[i]}")
                a += 1

            #print("Umumiy qidiruv: ")
        elif qidiruv == 2:
            while True:
                qidiruv = int(input("\nQaysi tuman boyicha qidiruv:  \n1-Yunusobot: \n2-Mirzo Ulugbek: \n3-Chilonzor: \n4-Yashnobot: \n5-Mirobod: \n\
                    \n6-Olmozor: \n7-Shayxontoxir: \n8-Yakkasaroy: \n9-Uchteppa: \n10-Bektemir: \n11-Sergeli: "))
                if qidiruv == 0:
                    break
                elif qidiruv == 1:
                    A = 0
                    for i in manzil:
                        if 'Yunusobot' in i:
                            print(f'Iam - {ism[A]} - yoshi - {yosh[A]} - Pasport seriasi - {ps[A]} - Inn - {inn[A]} - Foto - {foto[A]} - Maxsus belgilar - {maxsus_belgilar[A]}')

                elif qidiruv == 2:
                    A = 0
                    for i in manzil:
                        if 'Mirzo Ulugbek' in i:
                            print(f'Iam - {ism[A]} - yoshi - {yosh[A]} - Pasport seriasi - {ps[A]} - Inn - {inn[A]} - Foto - {foto[A]} - Maxsus belgilar - {maxsus_belgilar[A]}')


                elif qidiruv == 3:
                    A = 0
                    for i in manzil:
                        if 'Chilonzor' in i:
                            print(f'Iam - {ism[A]} - yoshi - {yosh[A]} - Pasport seriasi - {ps[A]} - Inn - {inn[A]} - Foto - {foto[A]} - Maxsus belgilar - {maxsus_belgilar[A]}')

                elif qidiruv == 4:
                    A = 0
                    for i in manzil:
                        if 'Yashnobot' in i:
                            print(f'Iam - {ism[A]} - yoshi - {yosh[A]} - Pasport seriasi - {ps[A]} - Inn - {inn[A]} - Foto - {foto[A]} - Maxsus belgilar - {maxsus_belgilar[A]}')

                elif qidiruv == 5:
                    A = 0
                    for i in manzil:
                        if 'Mirobot' in i:
                            print(f'Iam - {ism[A]} - yoshi - {yosh[A]} - Pasport seriasi - {ps[A]} - Inn - {inn[A]} - Foto - {foto[A]} - Maxsus belgilar - {maxsus_belgilar[A]}')

                elif qidiruv == 6:
                    A = 0
                    for i in manzil:
                        if 'Olmozor' in i:
                            print(f'Iam - {ism[A]} - yoshi - {yosh[A]} - Pasport seriasi - {ps[A]} - Inn - {inn[A]} - Foto - {foto[A]} - Maxsus belgilar - {maxsus_belgilar[A]}')              

                elif qidiruv == 7:
                    A = 0
                    for i in manzil:
                        if 'Shayxontoxir' in i:
                            print(f'Iam - {ism[A]} - yoshi - {yosh[A]} - Pasport seriasi - {ps[A]} - Inn - {inn[A]} - Foto - {foto[A]} - Maxsus belgilar - {maxsus_belgilar[A]}')
                elif qidiruv == 8:
                    A = 0
                    for i in manzil:
                        if 'Yakkasaroy' in i:
                            print(f'Iam - {ism[A]} - yoshi - {yosh[A]} - Pasport seriasi - {ps[A]} - Inn - {inn[A]} - Foto - {foto[A]} - Maxsus belgilar - {maxsus_belgilar[A]}')


                elif qidiruv == 9:
                    A = 0
                    for i in manzil:
                        if 'Uchteppa' in i:
                            print(f'Iam - {ism[A]} - yoshi - {yosh[A]} - Pasport seriasi - {ps[A]} - Inn - {inn[A]} - Foto - {foto[A]} - Maxsus belgilar - {maxsus_belgilar[A]}')

                elif qidiruv == 10:
                    A = 0
                    for i in manzil:
                        if 'Bektemir' in i:
                            print(f'Iam - {ism[A]} - yoshi - {yosh[A]} - Pasport seriasi - {ps[A]} - Inn - {inn[A]} - Foto - {foto[A]} - Maxsus belgilar - {maxsus_belgilar[A]}') 

                elif qidiruv == 11:
                    A = 0
                    for i in manzil:
                        if 'Sergeli' in i:
                            print(f'Iam - {ism[A]} - yoshi - {yosh[A]} - Pasport seriasi - {ps[A]} - Inn - {inn[A]} - Foto - {foto[A]} - Maxsus belgilar - {maxsus_belgilar[A]}')                                                                               
        else:
            print("Xato")    
    else:
        print("Xato")