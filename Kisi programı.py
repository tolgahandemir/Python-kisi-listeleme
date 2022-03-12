print("""**********************************
      
1-Bilgi Girişi
2-Tamamını Listeleme
3-Aranılan kişiye ait bilgileri listeleme
4-Aranılan kişiye ait bilgileri silme
5-Program sonu
      
**************************************************""")
ad = ""
soyad=""
meslek=""
tc=0
kişiler=[]
while True:
    işlem=input("İşlemi Giriniz: ")
    if(işlem=="1"):
        ad=input("Adınızı Giriniz ")
        soyad=input("Soyadınızı giriniz ")
        meslek=input("Mesleğinizi Giriniz ")
        tc=int(input("Tcnizi Giriniz "))
        bilgiler=[ad,soyad,meslek,tc]
        kişiler.append(bilgiler)
        print(" Adınız: {}\n Soyadınız : {}\n Mesleğiniz : {}\n Tc : {} ".format(bilgiler[0],bilgiler[1],bilgiler[2],bilgiler[3]))
        print("kişi eklendi")
        bilgiler=[]
    elif(işlem=="2"):
        if(len(kişiler)==0):
            print("Listenecek kişi bulunamadı")
        for kişi in kişiler:
            print(" Adınız: {}\n Soyadınız : {}\n Mesleğiniz : {}\n Tc : {} ".format(kişi[0],kişi[1],kişi[2],kişi[3]))
    elif(işlem=="3"):
        aranan_tc=int(input("Tc numaranızı giriniz : "))
        kişi_bulundu_mu=False
        for kişi in kişiler:
            if(kişi[3]==aranan_tc):
                print(" Adınız: {}\n Soyadınız : {}\n Mesleğiniz : {}\n Tc : {} ".format(kişi[0],kişi[1],kişi[2],kişi[3]))
                kişi_bulundu_mu=True
        if not(kişi_bulundu_mu):
                print("Böyle bir kişi bulunamadı")
    elif(işlem=="4"):
        silinecek_tc=int(input("Tc numaranızı giriniz : "))
        kişi_silindi_mi=False
        for kişi in kişiler:
            if(kişi[3]==silinecek_tc):
                kişiler.remove(kişi)
                print("Kişi Silindi")
                kişi_silindi_mi=True
        
        if not (kişi_silindi_mi):
            print("Böyle bir kişi bulunamadı")
    elif(işlem=="5"):
        print("Program Sonlandırıldı.")
        break
    elif(işlem=="6"):
        aranacak_isim=input("İsmi Giriniz:")
        bulunan_kişiler=[]
        for kişi in kişiler:
            if(kişi[0]==aranacak_isim):
                bulunan_kişiler.append(kişi)
        if(len(bulunan_kişiler)==0):
            print("Böyle bir kişi bulunamadı")
        else:
            for bulunan_kişi in bulunan_kişiler:
                print(" Adınız: {}\n Soyadınız : {}\n Mesleğiniz : {}\n Tc : {} ".format(bulunan_kişi[0],bulunan_kişi[1],bulunan_kişi[2],bulunan_kişi[3]))
    elif(işlem=="7"):
        aranacak_meslek=input("Mesleği Giriniz:")
        bulunan_meslekler=[]
        for kişi in kişiler:
            if(kişi[2]==aranacak_meslek):
                bulunan_meslekler.append(kişi)
        if(len(bulunan_meslekler)==0):
            print("Böyle bir kişi bulunamadı")
        else:
            for bulunan_meslek in bulunan_meslekler:
                print(" Adınız: {}\n Soyadınız : {}\n Mesleğiniz : {}\n Tc : {} ".format(bulunan_meslek[0],bulunan_meslek[1],bulunan_meslek[2],bulunan_meslek[3]))
             
        
        