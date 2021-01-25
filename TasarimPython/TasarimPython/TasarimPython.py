import tkinter as tk
from tkinter import filedialog, Text
from tkinter import *
import tkinter.messagebox
import os
from Bio import Phylo
from io import StringIO

def dosyaAc():
    os.system("text.txt")

def UPGMA():
        
        window = Tk()
        window.title("UPGMA")
        window.geometry('350x250')
        yazi = "UPGMA: ", UPGMA(M, M_etiketler)
        
        print(yazi)
        label = Label(window, text = yazi, fg = 'red', bg = 'yellow', relief = "solid", font = ('arial', 12, 'bold')).place(x=60, y=95)
        Phylo.draw(agac)

       # bosluk = tk.Label(frame, text="", bg="white")
       # bosluk.pack()
       # label = tk.Label(frame, text=yazi, bg="gray")
       # label.pack()
        

def Hesaplamalar():
        window = Tk()
        window.title("Sonuçlar")
        window.geometry('450x350')
        yazi = "\nA ile B uzaklığı: ", uzaklikAB, "\nA ile C uzaklığı: ", uzaklikAC, "\nA ile D uzaklığı: ", uzaklikAD, "\nA ile E uzaklığı: ", uzaklikAE,  "\nA ile F uzaklığı", uzaklikAF, "\nB ile C uzaklığı: ", uzaklikBC, "\nB ile D uzaklığı: ", uzaklikBD, "\nB ile E uzaklığı: ", uzaklikBE, "\nB ile F uzaklığı: ", uzaklikBF,"\nC ile D uzaklığı: ", uzaklikCD, "\nC ile E uzaklığı: ", uzaklikCE, "\nC ile F uzaklığı: ", uzaklikCF,"\nD ile E uzaklığı: ", uzaklikDE, "\nD ile F uzaklığı: ",  uzaklikDF, "\nE ile F uzaklığı: ", uzaklikEF
        yazi2 = "Harf sayısı: ", harfSayisi, "\n"
        label = Label(window, text = yazi2, fg = 'red',  font = ('arial', 13, 'bold')).place(x=120, y=10)
        label2 = Label(window, text = yazi, fg = 'blue',  font = ('arial', 10, 'normal')).place(x=120, y=35)

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


canvas = tk.Canvas(root, height=500, width=500, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg = "white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

hesaplama = tk.Button(root, text="Hesaplamaları Gör", padx=10, pady=5, fg="white", bg="#263D42", command=Hesaplamalar)
hesaplama.pack()

calistir = tk.Button(root, text="UPGMA sonucunu görmek için tıkla", padx=10, pady=5, fg="white", bg="#263D42", command=UPGMA)
calistir.pack()

dosyaAcmaEtiketi = tk.Button(root, text="Metin dosyasini ac", padx=10, pady=5, fg="white", bg="red", command=dosyaAc).place(x=190, y=290)
uyarix = Label(frame, text = "Dikkat! Metin dosyasındaki değişikliklerin işlenmesi için ", fg = 'black',  font = ('arial', 9, 'bold')).place(x=45, y=300)
uyari2x = Label(frame, text = "programın yeniden başlatılması gerekmektedir.", fg = 'black',  font = ('arial', 9, 'bold')).place(x=60, y=320)

cikis = tk.Button(root, text="Çıkış yap", padx=10, pady=5, fg="white", bg="#263D42", command=cikis)
cikis.pack()








A = ""
B = ""
C = ""
D = ""
E = ""
F = ""
bayrak1 = 1;
bayrak2 = 0;
bayrak3 = 0;
bayrak4 = 0;
bayrak5 = 0;
bayrak6 = 0;
satir = '';



# Dosya okuma işlemi
dosya = open('text.txt', 'r')
while True:
    char = dosya.read(1)
    
    # Sırasıyla okumalar başlıyor. Eğer '\n' sembolü gelirse duracaktır, ardından diğer dizilim için işlemler
    # gerçekleştirilecektir.
    
    if bayrak6 == 1:
        if(char != '\n'):
            F+=char
        if(char == ''):
            bayrak6 = 0
            break
    
    if bayrak5 == 1:
        if(char != '\n'):
            E+=char
        if(char == '\n'):
            bayrak5 = 0
            bayrak6 = 1
    
    if bayrak4 == 1:
        if(char != '\n'):
            D+=char
        if(char == '\n'):
            bayrak4 = 0
            bayrak5 = 1
    
    if bayrak3 == 1:
        if(char != '\n'):
            C+=char
        if(char == '\n'):
            bayrak3 = 0
            bayrak4 = 1
    
    if bayrak2 == 1:
        if(char != '\n'):
            B+=char
        if(char == '\n'):
            bayrak2 = 0
            bayrak3 = 1
    
    if bayrak1 == 1:
       if(char != '\n'):
         A+=char  
         
       if(char == '\n'):
           bayrak1 = 0
           bayrak2 = 1

print("Dizilimler: \n")           

print(A)
print(B)
print(C)
print(D)
print(E)
print(F)
print("")

baslik = Label(frame, text = "UPGMA Hesaplama", fg = 'magenta',  font = ('arial', 18, 'bold'))
baslik.pack()
bosluk = Label(frame, text = "                               ", fg = 'magenta',  font = ('arial', 18, 'bold'))
bosluk.pack()
label2 = tk.Label(frame, text="Dizinler:", bg= "white")
label2.pack()

label3 = tk.Label(frame, text="A: "+A, bg = "white")
label3.pack()
label4 = tk.Label(frame, text="B: "+B, bg = "white")
label4.pack()
label5 = tk.Label(frame, text="C: "+C, bg = "white")
label5.pack()
label6 = tk.Label(frame, text="D: "+D, bg = "white")
label6.pack()
label7 = tk.Label(frame, text="E: "+E, bg = "white")
label7.pack()
label8 = tk.Label(frame, text="F: "+F, bg = "white")
label8.pack()


harfSayisi = len(A) # Karakter uzunluğu belirleme işlemi



print("Harf sayisi: ", harfSayisi, "\n")
        

sayi = 0
sayac = 1
uzaklikAB = 0 
uzaklikAC = 0 
uzaklikAD = 0 
uzaklikAE = 0 
uzaklikAF = 0 
uzaklikBC = 0 
uzaklikBD = 0
uzaklikBE = 0 
uzaklikBF = 0 
uzaklikCD = 0 
uzaklikCE = 0 
uzaklikCF = 0 
uzaklikDE = 0 
uzaklikDF = 0			
uzaklikEF = 0
yazi1 = ""
yazi2 = ""
uzaklik = 0


# Uzaklık kontrolleri için satır ve sütunların seçimleri.

while(sayac <= 15):
    if(sayac == 1):
        yazi1 = A
        yazi2 = B
    if(sayac == 2):
        yazi1 = A
        yazi2 = C
    if(sayac == 3):
        yazi1 = A
        yazi2 = D
    if(sayac == 4):
        yazi1 = A
        yazi2 = E
    if(sayac == 5):
        yazi1 = A
        yazi2 = F
    if(sayac == 6):
        yazi1 = B
        yazi2 = C
    if(sayac == 7):
        yazi1 = B
        yazi2 = D
    if(sayac == 8):
        yazi1 = B
        yazi2 = E
    if(sayac == 9):
        yazi1 = B
        yazi2 = F
    if(sayac == 10):
        yazi1 = C
        yazi2 = D
    if(sayac == 11):
        yazi1 = C
        yazi2 = E
    if(sayac == 12):
        yazi1 = C
        yazi2 = F
    if(sayac == 13):
        yazi1 = D
        yazi2 = E
    if(sayac == 14):
        yazi1 = D
        yazi2 = F
    if(sayac == 15):
        yazi1 = E
        yazi2 = F
    
    # Hangi karakterler farklı ise o halde uzaklık değişkeni birer arttırılacaktır.
    
    while(sayi < harfSayisi):
        if(yazi1[sayi] != yazi2[sayi]):
            uzaklik+=1
        sayi+=1
        
        # sayac değişkenine göre satır ve sütun değişkenlerinin seçimi.
    if(sayi == harfSayisi):
        if(sayac == 1):
            uzaklikAB = uzaklik
            print("A ile B uzakligi: " , uzaklikAB)
        if(sayac == 2):
            uzaklikAC = uzaklik
            print("A ile C uzakligi: " , uzaklikAC)
        if(sayac == 3):
            uzaklikAD = uzaklik
            print("A ile D uzakligi: " , uzaklikAD)
        if(sayac == 4):
            uzaklikAE = uzaklik
            print("A ile E uzakligi: " , uzaklikAE)
        if(sayac == 5):
            uzaklikAF = uzaklik
            print("A ile F uzakligi: " , uzaklikAF)
        if(sayac == 6):
            uzaklikBC = uzaklik
            print("B ile C uzakligi: " , uzaklikBC)
        if(sayac == 7):
            uzaklikBD = uzaklik
            print("B ile D uzakligi: " , uzaklikBD)
        if(sayac == 8):
            uzaklikBE = uzaklik
            print("B ile E uzakligi: " , uzaklikBE)
        if(sayac == 9):
            uzaklikBF = uzaklik
            print("B ile F uzakligi: " , uzaklikBF)
        if(sayac == 10):
            uzaklikCD = uzaklik
            print("C ile D uzakligi: " , uzaklikCD)
        if(sayac == 11):
            uzaklikCE = uzaklik
            print("C ile E uzakligi: " , uzaklikCE)
        if(sayac == 12):
            uzaklikCF = uzaklik
            print("C ile F uzakligi: " , uzaklikCF)
        if(sayac == 13):
            uzaklikDE = uzaklik
            print("D ile E uzakligi: " , uzaklikDE)
        if(sayac == 14):
            uzaklikDF = uzaklik
            print("D ile F uzakligi: " , uzaklikDF)
        if(sayac == 15):
            uzaklikEF = uzaklik
            print("E ile F uzakligi: " , uzaklikEF)
        
        uzaklik = 0
        sayi = 0
        sayac += 1
        


# Hızlı Bir UPGMA Uygulaması (Aritmetik Ortalama ile Ağırlıksız Çift Grup Yöntemi)

# enKucuk_Hucre:
#   Tablodaki en küçük hücreyi bulur.
def enKucuk_Hucre(tablo):
    # Varsayılanı sonsuz olarak ayarla.
    min_hucre = float("inf")
    x, y = -1, -1

    # Her hücreye gidip, en küçük olanı ara.
    for i in range(len(tablo)):
        for j in range(len(tablo[i])):
            if tablo[i][j] < min_hucre:
                min_hucre = tablo[i][j]
                x, y = i, j

    # Hücrenin x ve y koordinatlarını döndür.
    return x, y


# etiketleri_Ekle:
#   Bir etiket listesinde iki etiketi birleştirir.
def etiketleri_Ekle(etiketler, a, b):
    # İndeksler sıralanmamışsa değiştirin.
    if b < a:
        a, b = b, a

    # İlk dizindeki etiketleri birleştirin.
    etiketler[a] = "(" + etiketler[a] + "," + etiketler[b] + ")"

    # İkinci dizindeki (artık gereksiz olan) etiketi kaldırın.
    del etiketler[b]


# tabloyu_Ekle:
#   Veri girişlerinin ortalamasını alarak hücredeki bir tablonun girdilerini (a, b) birleştirir.
def tabloyu_Ekle(tablo, a, b):
    # İndeksler sıralanmamışsa değiştirin.
    if b < a:
        a, b = b, a

    # Daha düşük indekslerde, i < A için; (A, i) olan tüm satırları yeniden oluşturun.
    satir = []
    for i in range(0, a):
        satir.append((tablo[a][i] + tablo[b][i])/2)
    tablo[a] = satir
    
    # Ardından, i > A için; tüm (i, A) sütunlarını yeniden oluşturun.
    #   Not: Matris daha küçük bir üçgen olduğundan dolayı, b satırı yalnızca b'den küçük indisleri için değerler taşır.
    for i in range(a+1, b):
        tablo[i][a] = (tablo[i][a]+tablo[b][i])/2
        
    #   Değerlerin geri kalanını i satırından alıyoruz.
    for i in range(b+1, len(tablo)):
        tablo[i][a] = (tablo[i][a]+tablo[i][b])/2
        # (Artık gereksiz olan) ikinci dizin sütunu girişini kaldırın.
        del tablo[i][b]

    # (Artık gereksiz olan) ikinci dizin satırını kaldırın.
    del tablo[b]


# UPGMA:
#   UPGMA algoritmasını etiketli bir tabloda çalıştırır.
def UPGMA(tablo, etiketler):
    # Tüm etiketler birleştirilene kadar işlemleri yap.
    while len(etiketler) > 1:
        # Tablodaki en küçük hücreyi bulun.
        x, y = enKucuk_Hucre(tablo)

        # Hücre koordinatlarındaki tabloya ekleme yapın.
        tabloyu_Ekle(tablo, x, y)

        # Etiketleri uygun şekilde güncelleyin.
        etiketleri_Ekle(etiketler, x, y)

    # Son etiketi döndürün.
    return etiketler[0]



## Burada, şu sitedeki UPGMA tablosu test edildi: https://www.youtube.com/watch?v=09eD4A_HxVQ&t=303s

# alfa_etiketleri:
#   Başlangıç harfinden bitiş harfine kadar etiketler yapar.
def alfa_etiketleri(baslangic, bitis):
    etiketler = []
    for i in range(ord(baslangic), ord(bitis)+1):
        etiketler.append(chr(i))
    return etiketler

# Test tablosu verileri ve ilgili etiketler
M_etiketler = alfa_etiketleri("A", "F")   # A ile F
M = [
    [],                                                      # A
    [uzaklikAB],                                             # B
    [uzaklikAC, uzaklikBC],                                  # C
    [uzaklikAD, uzaklikBD, uzaklikCD],                       # D
    [uzaklikAE, uzaklikBE, uzaklikCE, uzaklikDE],            # E
    [uzaklikAF, uzaklikBF, uzaklikCF, uzaklikDF, uzaklikEF]  # F
   
    ]

print()
print("UPGMA: ", UPGMA(M, M_etiketler))
print()
agacVerisi = UPGMA(M, M_etiketler)
print(agacVerisi)
handle = StringIO(agacVerisi)
agac = Phylo.read(handle, "newick")

print(agac)




# UPGMA(M, M_etiketler) şu şekilde çıktı vermelidir: '(((A,B),E),(C,D))'

root.mainloop()
