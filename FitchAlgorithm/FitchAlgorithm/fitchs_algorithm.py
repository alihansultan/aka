import sys
import statistics
from binary_tree import Node, pprint, stringify, _bst_insert, _new_node, _validate_tree, _build_tree, _weight_of, _add_left, _add_right, _build_list, _right_of, _left_of, _value_of, _null
from tkinter import *
import tkinter as tk
from tkinter import filedialog, Text
import tkinter.messagebox
import os


match = 2
other = -1
maxScore = 0
maxPosition = (0, 0)
pairwise_alignment_score = 0
sequence = []
names = []
finalSequence = []
score_sequence = []
deltaMatrix = []
fitchIndex = []
filename = "sekanslar3.txt"



def dosyaAc3():
    os.system("sekanslar3.txt")


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


canvas = tk.Canvas(root, height=500, width=600, bg="#ba2b1a")
canvas.pack()

frame = tk.Frame(root, bg = "white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)









dosyaAcmaEtiketi = tk.Button(root, text="Metin dosyasini ac", padx=10, pady=5, fg="white", bg="red", command=dosyaAc3).place(x=240, y=300)
uyarix = Label(frame, text = "Dikkat! Metin dosyasındaki değişikliklerin işlenmesi için ", fg = 'black',  font = ('arial', 9, 'bold')).place(x=75, y=285)
uyari2x = Label(frame, text = "programın yeniden başlatılması gerekmektedir.", fg = 'black',  font = ('arial', 9, 'bold')).place(x=90, y=305)

baslik = Label(frame, text = "Fitch Algoritması Hesaplama", fg = 'blue',  font = ('arial', 18, 'bold'))
baslik.pack()
bosluk = Label(frame, text = "                               ", fg = 'black',  font = ('arial', 18, 'bold'))
bosluk.pack()
dosya = open('sekanslar3.txt')
yazdirma = dosya.read()


yaz = Label(frame, text = yazdirma, fg = 'black',  font = ('arial', 7, 'normal'))
yaz.pack()

uyari3x = Label(frame, text = "Dikkat! Yukarıdakı sekansların hepsi ekrana sığmayabilir. ", fg = 'black',  font = ('arial', 9, 'bold')).place(x=75, y=200)
uyari3x = Label(frame, text = "Tam halini görmek için metin belgesini açınız.", fg = 'black',  font = ('arial', 9, 'bold')).place(x=75, y=220)


def main3():
    # Sıra giriş yapısı
    sequence, distance_matrix = fileReader(filename)
    for i in range(1, len(sequence), 2):
        names.append(sequence[i - 1][1:].strip())
        finalSequence.append(sequence[i].strip())

    # distance_matrix'i başlat
    distance_matrix = pairwiseDistanceMatrix(finalSequence, distance_matrix)
    score_sequence, min_sequence = scoreSequence(distance_matrix)

    new_root = buildTree(names, score_sequence, finalSequence)
    fitchsIndexCreation(new_root)

    window = Tk()
    window.title("Sonuçlar")
    window.geometry('600x600')

    text_area = Text(window)
    text_area.pack()

    text_area.insert(INSERT, stringify(new_root))

    window.mainloop()

def fileReader(filename):
    # genişletilmiş ascii ile dosya aç
    with open(filename, 'r') as newFile:
        data = newFile.readlines()
        for line in data:
            line.rstrip('\n')
            line = line.replace(' ', " ")     # herhangi bir boşluğu çıkarın
            sequence.append(line)
    distance_matrix = [
        [0 for col in range(len(sequence) // 2)]for row in range(len(sequence) // 2)]
    return sequence, distance_matrix


def delta(leftSequence, rightSequence):
    deltaScore = 0

    if(leftSequence == rightSequence):
        deltaScore = 0
    else:
        deltaScore = 1
    print(deltaScore)
    # print("Deltas")
    deltaMatrix.append(deltaScore)


def buildTree(names, weights, values):
    medianValues = list(weights)

    medianValues.sort()

    if len(medianValues) % 2 == 0:
        root_value = medianValues[int(len(medianValues) / 2)]
    else:
        root_value = statistics.median(medianValues)

    for x in range(len(weights)):
        if weights[x] == root_value:
            root_index = x
        else:
            continue
    new_root = _new_node(names[root_index], values[root_index], weights[root_index])
    for x in range(len(weights)):
        if x != root_index:
            _bst_insert(new_root, names[x], values[x], weights[x])
        else:
            continue
    return(new_root)


def fitchsIndexCreation(root_node):
    global fitchIndex
    node = root_node
    if root_node == _null:
        return
    if _left_of(node) == _null and _right_of(node) == _null:
        return
    try:
        test_1 = set(_value_of(_left_of(node)))
    except:
        test_1 = set()
    try:
        test_2 = set(_value_of(_right_of(node)))
    except:
        test_2 = set()
    inSet = set.intersection(test_1, test_2)
    if len(inSet) == 0:
        node.value = set.union(test_1, test_2)
    else:
        node.value = inSet

    fitchsIndexCreation(_left_of(node))
    fitchsIndexCreation(_right_of(node))


def compare(a, b):
    notEqual = []
    for x, y in zip(a, b):
        if x == y:
            print('equal')
            notEqual.append((x, y))
        else:
            print('not equal')
            notEqual.append((x, y))
    if len(notEqual) < 1:
        return a
    else:
        return notEqual

        
        ## S'deki tüm diziler için ikili mesafe puanını hesaplar 
       


def pairwiseDistanceMatrix(sequence_list, distance_matrix):
    global seq1
    global seq2
    global rows
    global cols
    for x in range(len(sequence_list)):
        for y in range(len(sequence_list)):
            seq1 = sequence_list[x]
            seq2 = sequence_list[y]

            rows = len(seq1) + 1
            cols = len(seq2) + 1

            score_matrix, start_pos = createScoreMatrix(rows, cols)
            distance_score = traceback(score_matrix, start_pos)

            distance_matrix[x][y] = distance_score
        # offset += 1
    return distance_matrix



## Hizalama puanlarının sırasını oluşturur 


def scoreSequence(d_matrix):
    score_min = 10000000
    score_value = 0
    sc_sequence = []
    for x in range(len(d_matrix)):
        for y in range(len(d_matrix)):
            score_value = score_value + d_matrix[x][y]
        if score_value < score_min:
            score_min_index = x
            score_min = score_value
        sc_sequence.append(score_value)
        score_value = 0
    return sc_sequence, score_min_index


# Giriş dizelerinden puanlama matrisi oluşturur


def createScoreMatrix(rows, cols):
    global maxScore
    maxPosition = (0, 0)
    score_matrix = [[0 for col in range(cols)]for row in range(rows)]

    for i in range(1, rows):
        for j in range(1, cols):
            similarity = match if seq1[i - 1] == seq2[j - 1] else other
            diag_score = score_matrix[i - 1][j - 1] + similarity
            up_score = score_matrix[i - 1][j] + other
            left_score = score_matrix[i][j - 1] + other
            curMax = max(0, diag_score, up_score, left_score)
            if curMax > maxScore:
                maxScore = curMax
                maxPosition = (i, j)
            score_matrix[i][j] = curMax
    maxScore = 0
    return score_matrix, maxPosition


# Puanlama matrisine göre en uygun hizalama dizesini oluşturur


def traceback(score_matrix, start_pos):
    pairwise_alignment_score = 0
    END, DIAG, UP, LEFT = range(4)
    aligned_seq1 = []
    aligned_seq2 = []
    x, y = start_pos
    move = nextMove(score_matrix, x, y)
    while move != END:
        if move == DIAG:
            aligned_seq1.append(seq1[x - 1])
            aligned_seq2.append(seq2[y - 1])
            x -= 1
            y -= 1
        elif move == UP:
            aligned_seq1.append(seq1[x - 1])
            aligned_seq2.append('-')
            x -= 1
            pairwise_alignment_score += 1
        else:
            aligned_seq1.append('-')
            aligned_seq2.append(seq2[y - 1])
            y -= 1
            pairwise_alignment_score += 1

        move = nextMove(score_matrix, x, y)

    aligned_seq1.append(seq1[x - 1])
    aligned_seq2.append(seq1[y - 1])

    return pairwise_alignment_score


## Geri izleme için bir sonraki hareketi belirler 



def nextMove(score_matrix, x, y):

    # Çapraz puanı atayın
    diag = score_matrix[x - 1][y - 1]

    # Ekleme / silme puanlarını atayın
    up = score_matrix[x - 1][y]
    left = score_matrix[x][y - 1]

    # Sonraki karakteri / eklemeyi / silmeyi bulmak için üç durumu da kontrol edin
    if diag >= up and diag >= left:
        return 1 if diag != 0 else 0
    elif up > diag and up >= left:
        return 2 if up != 0 else 0
    elif left > diag and left > up:
        return 3 if left != 0 else 0

    # Hata tespiti
    else:
        
        raise ValueError('invalid move during traceback')


# Yazdırma için hizalama dizesini oluşturur



def alignment_string(aligned_seq1, aligned_seq2):

    # Başlangıç değerlerini ayarlar
    idents, gaps, mismatches = 0, 0, 0
    alignment_string = []

    # Her iki dizeyi de çalıştırır
    for base1, base2 in zip(aligned_seq1, aligned_seq2):

        # Eşleşme kontrolleri
        if base1 == base2:
            alignment_string.append('|')
            idents += 1

        # Ekleme / silme için kontroller
        elif '-' in (base1, base2):
            alignment_string.append(' ')
            gaps += 1

        # Yukarıdakilerin hiçbiri uyuşmuyorsa 'mismatch' olacaktır.
        else:
            alignment_string.append(':')
            mismatches += 1

    # "Hizalama" dizesini ve hizalama özelliklerini döndürür.
    return ''.join(alignment_string), idents, gaps, mismatches


calistir = tk.Button(root, text="Fitch Hesapla", padx=10, pady=5, fg="white", bg="#734a12", command=main3).place(x=255, y=390)
uyari = Label(root, text = "Dikkat! Hesaplama süreci 5 ila 10 sn sürmektedir.", fg = 'black',  font = ('arial', 9, 'bold')).place(x=150, y=430)

 
        
cikis = tk.Button(root, text="Çıkış yap", padx=10, pady=5, fg="white", bg="#434343", command=cikis)
cikis.pack()

root.mainloop()