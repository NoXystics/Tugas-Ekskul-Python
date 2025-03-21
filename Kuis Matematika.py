import random

op = ['+', '-', '*', '/']
nomor = 1
skor = 0

def Answer(Angka1, Angka2, Operator):
    if Operator == "+" :
        Ans = Angka1+Angka2
    elif Operator == "-" :
        Ans = Angka1-Angka2
    elif Operator == "*" :
        Ans = Angka1*Angka2
    elif Operator == "/" :
        Ans = Angka1/Angka2
    return Ans

#MAIN GAME
def new_func():
    return float(input("Jawaban Anda: "))

while True :
    nmr = str(nomor)
    print("#"+nmr)
    Angka1 = random.randint(1,100)
    Operator = random.choice(op)
    Angka2 = random.randint(1,100)

    print(str(Angka1) + " " + Operator + " " + str(Angka2) + " =")
    jawaban = new_func()

    Ans = round(Answer(Angka1, Angka2, Operator), 2)

    if jawaban == float(Ans):
        print("Jawaban Anda Benar!")
        nomor += 1
        skor +=1
    else :
        print("Jawaban Anda Salah!")
        JawabanBenar = str(Ans)
        print("Jawaban yang benar adalah: "+JawabanBenar)
        nomor +=1
    
    if nomor == 10 :
        print("Selamat Anda telah menyelesaikan quiz!")
        skorstring = str(skor)
        print("Skor Anda adalah "+skorstring)
        break