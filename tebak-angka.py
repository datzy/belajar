import random
import time
import os

def Human(x):
    print("Sebentar aku sedang memilih angka")
    time.sleep(3)
    print("Aku sudah selesai memlilih angka!!")
    time.sleep(1)
    print("Silahkan tebak angka pilihanku range 1 sampai 10")
    time.sleep(3)
    os.system('cls')
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Tebakan mu antara 1 - {10} : '))
        if guess < random_number:
            print('Maaf, Coba lagi. Angka terlalu rendah,')
        elif guess > random_number:
            print('Maaf, Coba lagi. Angka terlalu tinggi.')
        elif guess == random_number :
            print(f'Hore!! Selamat, Kamu telah berhasil menebak angka, {guess}, dengan benar !!')
            time.sleep(3)
            os.system('cls')
            Lanjut2()
        else :
            print("Masukkan input dengan benar")
            time.sleep(2)
            print(Human(10))    
        
   

def Computer(x):
    print("Silahkan pilih angka 1 - 10")
    time.sleep(1)
    print("Aku akan menebak angka tersebut !!")
    time.sleep(1)
    os.system('cls')
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'Apakah {guess}, terlalu tinggi (t), terlalu rendah (r), atau benar (b) dengan angka pilihan kamu ?? ').lower()
        if feedback == 't':
            high = guess - 1
        elif feedback == 'r':
            low = guess + 1
        elif feedback== 'b':
            print(f"Hore!! Aku berhasil menebak, {guess}, dengan benar!!")
            time.sleep(2)
            os.system('cls')
            Lanjut()
        else :
            print("Masukkan input dengan benar")
            time.sleep(2)
            print(Computer(10))


def menu():
    print("Tentukan jenis permainan anda!")
    time.sleep(1)
    print("1. Kamu menebak Aku")
    print("2. Aku menebak kamu")
    print("3. Keluar")
    pilihan = int(input("Tentukan: "))
    if pilihan==1:
        os.system('cls')
        Human(10)
    elif pilihan==2:
        os.system('cls')
        Computer(10)
    elif pilihan==3:
        keluar()
    else :
        print("Masukkan input dengan benar !!")
        time.sleep(3)
        os.system('cls')
        menu()

def Lanjut():
    print("Apakah masih ingin bermain ? Y untuk tetap bermain, N untuk kembali ke pilihan menu, E untuk keluar")
    time.sleep(2)
    lanjutkah = input ("pilihan mu ? : ")

    if lanjutkah.upper() =="Y" :
        time.sleep(1)
        os.system('cls')
        Computer(10)

    elif lanjutkah.upper() =="N" :
        time.sleep(1)
        os.system('cls')
        menu()
    
    elif lanjutkah.upper() == "E" :
        keluar()
    
    else :
        print("Masukkan input dengan benar !!")
        time.sleep(3)
        os.system('cls')
        print(Computer(10))

def Lanjut2():
    print("Apakah masih ingin bermain ? Y untuk tetap bermain, N untuk kembali ke pilihan menu, E untuk keluar")
    time.sleep(2)
    lanjutkah = input ("pilihan mu ? : ")

    if lanjutkah.upper() =="Y" :
        time.sleep(1)
        os.system('cls')
        Human(10)

    elif lanjutkah.upper() =="N" :
        time.sleep(1)
        os.system('cls')
        menu()
    
    elif lanjutkah.upper() == "E" :
        keluar()
    
    else :
        print("Masukkan input dengan benar !!")
        time.sleep(3)
        os.system('cls')
        print(Human(10))

def keluar():
    os.system('cls')
    print("Sampai jumpa. Semoga harimu menyenangkan!!")
    time.sleep(2)
    exit()

os.system('cls')
print("="*70)
time.sleep(1)
print("MARI BERMAIN TEBAK ANGKA BERSAMA MUAMMAR")
time.sleep(1)
print("="*70)
time.sleep(1)
os.system('cls')
menu()
