
#Önyükleme (bootstrap) ve maksimum parsimony kullanarak, dört dizilik bir dizi için bir consensus ağacı 

import random
import tkinter as tk
from tkinter import filedialog, Text
from tkinter import *
import tkinter.messagebox
import os


def dosyaAc():
    
    os.system("Sekanslar.txt")
    

    


def hakkinda():
    tkinter.messagebox.showinfo("Hakkında","Merhaba! Bu demo programı, Tasarım dersi için oluşturulmuştur.")


def cikis():

        quit(0)

root = tk.Tk()

root.title("Proje")

menu = Menu(root)
root.config(menu=menu)

subm1 = Menu(menu)
menu.add_cascade(label="Dosya", menu=subm1)
subm1.add_command(label="Çıkış", command=cikis)


subm2 = Menu(menu)
menu.add_cascade(label="Yardım", menu=subm2)
subm2.add_command(label="Hakkında", command = hakkinda)


canvas = tk.Canvas(root, height=500, width=700, bg="#00a778")
canvas.pack()

frame = tk.Frame(root, bg = "white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)



def sekansOku(filename):
    sonucListesi = []
    infile = open(filename, 'r')

    satir = infile.readline()
    baslik = satir.rstrip() 
    etiket = baslik[1:] 

    sekans = ''

    for satir in infile:
        satir = satir.rstrip()

        # Boş satırları yoksay.
        if satir != '':

            if satir[0] == '>':
                sonucListesi.append([etiket, sekans])
                baslik = satir.rstrip()
                etiket = baslik[1:]
                sekans = ''

            else:
                sekans += satir

    infile.close()
    sonucListesi.append([etiket, sekans])
    return sonucListesi


sekansBilgisi = sekansOku('Sekanslar.txt')



def main():
    window = Tk()
    window.title("Sonuçlar")
    window.geometry('600x600')
    labelx = Label(window, text = "Hesaplama yapılıyor... ", fg = 'red',  font = ('arial', 13, 'bold')).place(x=90, y=100)
    # Dosyadan bilgi oku
    sekansBilgisi = sekansOku('Sekanslar.txt')

    sekansListesi = []
    etiketListesi = []
    # Dosyadaki dizilerinin ve etiketlerinin ayrı bir listesi oluşturulur.
    for i in range(0, len(sekansBilgisi)): 
        sekans = sekansBilgisi[i][1]
        sekansListesi.append(sekans)
        etiket = sekansBilgisi[i][0]
        etiketListesi.append(etiket)

    # Dizileri bilgi verici (informative) sitelere atayın.
    sekansListesi = bilgiGoster(sekansListesi)
    n = len(sekansListesi[0]) # Bilgi verici sitelerin sayısı

    # A, B, C ve D sekanslarını ayarlama
    cladeCifti1 = 0 # A-B sınıflarının (clade) sayısını (ve dolayısıyla C-D sınıflarını da) sayar.
    cladeCifti2 = 0 # A-C sınıflarının (clade) sayısını (ve dolayısıyla B-D sınıflarını da) sayar.
    cladeCifti3 = 0 # A-D sınıflarının (clade) sayısını (ve dolayısıyla B-C sınıflarını da) sayar.

    # Önyüklemeyi (bootstrapping) 1000 kez çalıştır.
    denemeSayisi = 1000
    for deneme in range(denemeSayisi):
        ornekSiraListesi = []
        for sekans2 in sekansListesi: # Her sekans için.
            ornek = ''
            for x in range(n): # Her bilgi verici site için.
                site = random.randrange(n) 
                ornek += sekans2[site]
            ornekSiraListesi.append(ornek) # Burada çoğaltmadan sonra dizilerin bir listesini yapılır.

        ilkAgac = rastgeleAgacOlustur(ornekSiraListesi) # Rastgele bir başlangıç ağacı seçer.
        uzunluk = uzunlukHesapla(ilkAgac) # Toplam dal uzunluğunu bul.
        enIyiAgac = ilkAgac

        # En iyi ağaçta değişiklik olmaksızın ağaçların kaç kez karşılaştırıldığını sayın.
        degisiklikYok = 0
        # 10 keyfi olarak seçilen bir eşiktir, ancak en iyi ağaç ince değerini yansıtmalıdır.
        while (degisiklikYok < 10):
            agacKiyasla = rastgeleAgacOlustur(ornekSiraListesi) # Yeni bir rastgele ağacı oluştur.
            uzunlukKiyasla = uzunlukHesapla(agacKiyasla) # Bu ağacın dal uzunluğunu bulun.
            if (uzunlukKiyasla < uzunluk): # Eğer bu şimdiye kadar bulunan en iyi dal uzunluğuysa,
                uzunluk = uzunlukKiyasla # bunu karşılaştırılacak yeni değer hasatir getirin.
                enIyiAgac = agacKiyasla # Ardından bunu şimdiye kadarki en iyi değer olarak sakla.
            else:
                degisiklikYok += 1

        # İlk üç deneme için bu topolojileri ekrana yazdırın.
        if (deneme == 0 or deneme == 1 or deneme == 2):
            
            agacYazdir = ((enIyiAgac[0][0][0], enIyiAgac[0][1][0]),
                         (enIyiAgac[1][0][0], enIyiAgac[1][1][0]))
            # Denemeye göre baskı ön ekini değiştirin.
            if (deneme == 0):
                basKisim = 'Birinci' 
            elif (deneme == 1):
                basKisim = 'İkinci'
            elif (deneme == 2):
                basKisim = 'Ucuncu'
            print(basKisim + ' bootstrap (ön yükleme) hesaplaması aşağıdaki topolojiyi ortaya koymaktadır: ')
            print(agacYazdir)
            print('') 

        # Birinci sınıftaki (first clade) dizilerin etiketlerini belirleyin.
        # (Örnek: 0 ve 1 değerleri, birinci dizinin ve ikinci dizinin bir sınıfını (a clade) temsil eder.)
        etiket1 = enIyiAgac[0][0][1]
        etiket2 = enIyiAgac[0][1][1]
        # Bir örnek topolojide sınıflar (clades) gözlemlendiğinde sınıf sayaçlarını artırın.
        if ((etiket1 == 0 and etiket2 == 1) or
            (etiket1 == 1 and etiket2 == 0)):
            cladeCifti1 += 1
        elif ((etiket1 == 0 and etiket2 == 2) or
              (etiket1 == 2 and etiket2 == 0)):
            cladeCifti2 += 1
        elif ((etiket1 == 0 and etiket2 == 3) or
              (etiket1 == 3 and etiket2 == 0)):
            cladeCifti3 += 1 
        elif ((etiket1 == 1 and etiket2 == 2) or
              (etiket1 == 2 and etiket2 == 1)):
            cladeCifti3 += 1
        elif ((etiket1 == 1 and etiket2 == 3) or
              (etiket1 == 3 and etiket2 == 1)):
            cladeCifti2 += 1 
        elif ((etiket1 == 2 and etiket2 == 3) or
              (etiket1 == 3 and etiket2 == 2)):
            cladeCifti1 += 1

    # En çok hangi sınıf (clade) çiftinin göründüğünü belirleyin.
    consensus = max(cladeCifti1, cladeCifti2, cladeCifti3)
    # consensusAgaci'na yazdırılmak üzere kaldırılan etiketler.
    # clade (sınıf) sayaçları, bootstrap (önyükleme) değerini elde etmek için toplam deneme sayısına bölünür.
    if (consensus == cladeCifti1):
        consensusAgaci = [[etiketListesi[0], etiketListesi[1]],
                         [etiketListesi[2], etiketListesi[3]]]
        bootstrap = cladeCifti1/denemeSayisi
    elif (consensus == cladeCifti2):
        consensusAgaci = [[etiketListesi[0], etiketListesi[2]],
                         [etiketListesi[1], etiketListesi[3]]]
        bootstrap = cladeCifti2/denemeSayisi
    elif (consensus == cladeCifti3):
        consensusAgaci = [[etiketListesi[0], etiketListesi[3]],
                         [etiketListesi[1], etiketListesi[2]]]
        bootstrap = cladeCifti3/denemeSayisi
    # Consensus ağacını ve önyükleme değerini yazdırma:
    print('Verilen diziler için consensus ağacı şu şekilde bulundu: ')
    labely = Label(window, text = "Verilen diziler için consensus ağacı\n     şu şekilde bulundu: ", fg = 'red',  font = ('arial', 13, 'bold')).place(x=90, y=100)
    print('')
   
    print(str(consensusAgaci[0][0]) + '         ' + str(consensusAgaci[1][0]))
    labelz = Label(window, text = str(consensusAgaci[0][0]) + "         " + str(consensusAgaci[1][0]), fg = 'magenta',  font = ('arial', 13, 'bold')).place(x=90, y=155)
    print('                 \________/')
    labelt = Label(window, text = "                 \________/", fg = 'magenta',  font = ('arial', 13, 'bold')).place(x=90, y=180)
    print('                 /        \\')
    labela = Label(window, text = "                 /               \\", fg = 'magenta',  font = ('arial', 13, 'bold')).place(x=90, y=200)
    print(str(consensusAgaci[0][1]) + '         ' + str(consensusAgaci[1][1]))
    labelb = Label(window, text = str(consensusAgaci[0][1]) + "         " + str(consensusAgaci[1][1]), fg = 'magenta',  font = ('arial', 13, 'bold')).place(x=90, y=220)
    print('')
    print('bootstrap (önyükleme) değeri: ' + str(bootstrap) + '.')
    labelc = Label(window, text = "bootstrap (önyükleme) değeri: " + str(bootstrap) + ".", fg = 'blue',  font = ('arial', 13, 'bold')).place(x=90, y=300)
    
# bilgiGoster: Bir dizi listesindeki bilgilendirici siteleri kontrol eden bir fonksiyondur.
def bilgiGoster(sekansListesi):

    sekansUzunlugu = len(sekansListesi[0])   
    bilgiTakip = [] # Dizilerdeki bilgi verici sitelerin yerlerini takip eder.
    for x in range(sekansUzunlugu): 
        sayacA = 0
        sayacC = 0
        sayacG = 0
        sayacT = 0
        # Dizileri yineleyin, ardından her bir nükleotid için görünüm sayısını hesaplayın.
        for sekans in sekansListesi: 
            if (sekans[x] == 'A'):
                sayacA += 1
            elif (sekans[x] == 'C'):
                sayacC += 1
            elif (sekans[x] == 'G'):
                sayacG += 1
            elif (sekans[x] == 'T'):
                sayacT += 1
        # Bilgi verici bir site, en az iki farklı nükleotidin iki veya daha fazla görüntüsüne sahiptir.
        if ((sayacA >= 2 and sayacC >= 2) or
            (sayacA >= 2 and sayacG >= 2) or
            (sayacA >= 2 and sayacT >= 2) or
            (sayacC >= 2 and sayacG >= 2) or
            (sayacC >= 2 and sayacT >= 2) or
            (sayacG >= 2 and sayacT >= 2)):
            bilgiTakip.append(1) # "1" ile izleyicide bilgi verici siteleri temsil eder.
        else:
            bilgiTakip.append(0) # bilgi verici olmayan siteleri 0 ile temsil eder.

    sekansBilgiListe = []
    
    for sekans in sekansListesi:
        sekansBilgi = ''
        for x in range(sekansUzunlugu):
            if (bilgiTakip[x] == 1): 
                sekansBilgi += sekans[x]
        sekansBilgiListe.append(sekansBilgi)

    return sekansBilgiListe    

# rastgeleAgacOlustur - Dört diziden oluşan bir listeden rastgele bir ağaç oluşturan bir fonksiyondur.

def rastgeleAgacOlustur(sekansListesi):
    agac = []
    seqnum = 0
    ek = []
    # Sınıfların (clades) daha sonra belirlenmesine yardımcı olmak için dizilerin her birine bir etiket atayın.
    for sekans in sekansListesi:
        etiket = seqnum
        seqnum += 1
        ek.append([sekans, etiket])
    # Diziler için rastgele bir sıra seçin.
    a = random.choice(ek)
    ek.remove(a)
    b = random.choice(ek)
    ek.remove(b)
    c = random.choice(ek)
    ek.remove(c)
    d = random.choice(ek)
    # Rastgele düzeni yansıtan bir ağaç oluşturun.
    agac.append([a,b])
    agac.append([c,d])
    return agac


# uzunlukHesapla - Belirli bir ağacın toplam dal uzunluğunu hesaplayan bir fonksiyondur.

def uzunlukHesapla(agac):

    # Etiketlere değil, sadece dizilere bakılır.
    a = agac[0][0][0]
    b = agac[0][1][0]
    c = agac[1][0][0]
    d = agac[1][1][0]

    # Uzunluk, verilen iki dizi arasındaki ikame sayısı ile belirlenir.
    ab_uzunluk = subsay(a, b)
    cd_uzunluk = subsay(c, d)
    ac_uzunluk = subsay(a, c)
    bd_uzunluk = subsay(b, d)
    # Toplam dal uzunluğunun üst üste binen kısımlarından hesaplanması gerekir.
    l = (ac_uzunluk + bd_uzunluk + ab_uzunluk + cd_uzunluk)/2
    
    return l


# subsay - İki dizge arasındaki ikame sayısını (ve dolayısıyla iki dizi için dal uzunluğunu) sayan bir fonksiyondur.

def subsay(seq1, seq2):
    subsayisi = 0
    for x in range(len(seq1)):
        # Bir indeksteki nükleotidler eşleşmediğinde bir ikame meydana gelir.
        if (seq1[x] != seq2[x]):
            subsayisi += 1
    return subsayisi


# sekansOku - FASTA'ya benzer bir biçime sahip dosyaları okuyan bir fonksiyon.



def sekansOku(filename):
    sonucListesi = []
    infile = open(filename, 'r')

    satir = infile.readline()
    baslik = satir.rstrip() 
    etiket = baslik[1:] 

    sekans = ''

    for satir in infile:
        satir = satir.rstrip()

        # Boş satırları yoksay.
        if satir != '':

            if satir[0] == '>':
                sonucListesi.append([etiket, sekans])
                baslik = satir.rstrip()
                etiket = baslik[1:]
                sekans = ''

            else:
                sekans += satir

    infile.close()
    sonucListesi.append([etiket, sekans])
    return sonucListesi

def Hesaplamalar():
        
        
        label = Label(window, text = (main), fg = 'red',  font = ('arial', 13, 'bold')).place(x=120, y=10)
        
label__0 = Label(root, text = "Maksimum Parsimony Hesaplama", fg = 'magenta',  font = ('arial', 18, 'bold')).place(x=170, y=90)
label1 = Label(root, text = "Sekansları metin dosyasında görmek için tıklayınız.", fg = 'red',  font = ('arial', 13, 'bold')).place(x=170, y=160)

dosyaAcmaEtiketi = tk.Button(root, text="Metin dosyasini ac", padx=10, pady=5, fg="white", bg="red", command=dosyaAc).place(x=290, y=190)
uyarix = Label(frame, text = "Dikkat! Metin dosyasındaki değişikliklerin işlenmesi için ", fg = 'black',  font = ('arial', 9, 'bold')).place(x=125, y=200)
uyari2x = Label(frame, text = "programın yeniden başlatılması gerekmektedir.", fg = 'black',  font = ('arial', 9, 'bold')).place(x=140, y=220)

#label1 = Label(root, text = ("Sekanslar:\n " ), fg = 'red',  font = ('arial', 13, 'bold')).place(x=130, y=70)
#label2 = Label(root, text =  str(sekansOku('Sekanslar.txt')), fg = 'red',  font = ('arial', 10, 'bold')).place(x=130, y=110)
hesaplama = tk.Button(root, text="Hesapla", padx=10, pady=5, fg="white", bg="green", command=main).place(x=315, y=320)
uyari = Label(root, text = "Dikkat! Hesaplama süreci 5 ila 10 sn sürmektedir.", fg = 'black',  font = ('arial', 9, 'bold')).place(x=220, y=355)

cikisYap = tk.Button(root, text="Cikis yap", padx=10, pady=5, fg="white", bg="#263D42", command=cikis)
cikisYap.pack()


root.mainloop()

