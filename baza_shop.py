from datetime import*


nomi = []
miqdori = []
tannarxi = []
sotuv_narxi = []
vaqt = []
srok = []
nomi2 = []
miqdori2 = []

while True:
    sorov_bolim = int(input("Qaysi bolimni tanlaysiz?\n1-Kirim \n2-Chiqim \n3-Hisobot:\n>>>"))
    if sorov_bolim == 1:
        while True:
            A = str(input("\n\nnomi: "))
            if A == "stop":
                break
            nomi.append(A)
            B = float(input("miqdori: "))
            miqdori.append(B)
            C = float(input("tannarxi: "))
            tannarxi.append(C)
            E = float(input("sotuv narxi: "))
            sotuv_narxi.append(E)
            
            v = datetime.now()
            vaqt.append(str(v))
            X = int(input("srok soatda: "))
            y = timedelta(hours=X)
            z = v + y
            srok.append(str(z))
            #print(nomi, miqdori,tannarxi, sotuv_narxi, vaqt, srok)
    

    elif sorov_bolim == 2:
        while True:
            Y = str(input("\n\nchiqim nomi: "))
            if Y == "stop":
                break
            nomi2.append(Y)
            F = float(input("chiqim miqdori: "))
            miqdori2.append(F)
            #print(nomi2, miqdori2)
    

    elif sorov_bolim == 3:
        while True:
            for i in range(len(nomi)):
                        text = f"{nomi[i]} - {miqdori[i]} - {tannarxi[i]} - {sotuv_narxi[i]} - {vaqt[i]} - {srok[i]}"
                        print(text+"\n\n")
            for i in range(len(nomi)):
                xarajat = miqdori[i] * tannarxi[i] 
                kassa_pul = miqdori2[i] * sotuv_narxi[i]
                qoldiq = miqdori[i] - miqdori2[i] 
                text = f'{nomi[i]} - uchun xisobot: xarajat = {xarajat}   kassadagi puliz =  {kassa_pul}  qolgan qoldiq = {qoldiq}' 
                print(text+"\n\n")         
            break            
    else:
        print("Xato")