KataTertebak = []
import random

while True :
    KataMudahBenda = ['foto', 'gaun', 'emas', 'bank', 'alam']
    KataMudahSifat = ['kaya', 'kuat', 'baru', 'asam', 'asin']

    KataSedangBenda = ['energi', 'daging', 'cermin', 'sepeda', 'payung']
    KataSedangSifat = ['cantik', 'tampan', 'lincah', 'lemah', 'kuat']

    KataSusahBenda = ['cangkir', 'monitor', 'catatan', 'gerbang', 'halaman']
    KataSusahKerja = ['membuat', 'menyapu', 'menulis', 'membaca', 'menanam']
    KataSusahSifat = ['ganteng', 'panjang', 'kencang', 'bengkok', 'kenyang']
    snowman = u'\u2764'
    sisa_nyawa = 'Sisa nyawa: '
    guessed_word_correctly = False

    print ('''Pilih tingkat kesulitan: 
        1. Mudah
        2. Sedang
        3. Sulit''')
    difficulty = int(input('Kesulitan: '))

    if difficulty == 1:
        print ('''Pilih tema kata: 
        1. Kata Benda
        2. Kata Kerja
        3. Kata Sifat''')
        tema = int(input('Tema: '))
        clue = list('❔❔❔❔')
        nyawa = 20
        if tema == 1: 
            kata_rahasia = random.choice(KataMudahBenda)
        elif tema == 2:
            print ('Maaf tema tersebut hanya tersedia untuk tingkat sulit')
        elif tema == 3:
            kata_rahasia = random.choice(KataMudahSifat)
        else :
            print ('Error')

    elif difficulty == 2:
        print ('''Pilih tema kata: 
        1. Kata Benda
        2. Kata Kerja
        3. Kata Sifat''')
        tema = int(input('Tema: '))
        clue = list('❔❔❔❔❔❔')
        nyawa = 10
        if tema == 1: 
            kata_rahasia = random.choice(KataSedangBenda)
        elif tema == 2:
            print ('Maaf tema tersebut hanya tersedia untuk tingkat sulit')
        elif tema == 3:
            kata_rahasia = random.choice(KataSedangSifat)
        else :
            print ('Error')

    elif difficulty == 3: 
        print ('''Pilih tema kata: 
        1. Kata Benda
        2. Kata Kerja
        3. Kata Sifat''')
        tema = int(input('Tema: '))
        clue = list('❔❔❔❔❔❔❔')
        nyawa = 5
        if tema == 1: 
            kata_rahasia = random.choice(KataSusahBenda)
        elif tema == 2:
            kata_rahasia = random.choice(KataSusahKerja)
        elif tema == 3:
            kata_rahasia = random.choice(KataSusahSifat)
        else :
            print ('Error')
    
    else :
        print ('Error')


    while nyawa > 0 :
        print (''.join(clue))
        print (sisa_nyawa + snowman * nyawa)
        player_guess = input('Tebak sebuah huruf atau kata: ')

        if player_guess == kata_rahasia: 
            guessed_word_correctly = True
            break
    
        if player_guess in kata_rahasia:
            for i in range(len(kata_rahasia)):
                if player_guess == kata_rahasia[i]:
                    clue[i] = player_guess
        else:
            print('Salah!')
            nyawa = nyawa - 1

        if clue == list(kata_rahasia):
            guessed_word_correctly = True
            break


    if guessed_word_correctly == True:
        print ('Kamu menang! Kata rahasia nya adalah: '+ kata_rahasia)
        KataTertebak.append(kata_rahasia)
    else:
        print ('Kamu kalah! Kata rahasia nya adalah: '+ kata_rahasia)
    lanjut = input ('Apakah kamu ingin lanjut? (Y/N) ')
    if 'Y' in lanjut:
        continue
    elif 'y' in lanjut:
        continue
    else:
        break

KataDitebakUnik = list(set(KataTertebak))
JumlahKataDitebak = len(KataDitebakUnik)
JumlahKataBelumDitebak = 35 - JumlahKataDitebak
JmlhKtBlmDtbk = str(JumlahKataBelumDitebak)
print('Kata yang sudah Anda tebak: ')
print(KataDitebakUnik)
print('Kata yang belum Anda tebak: ' + JmlhKtBlmDtbk)