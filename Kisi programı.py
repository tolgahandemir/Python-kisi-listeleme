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
               
        