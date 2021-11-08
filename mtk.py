from os import system

def menu():
    print("Silahkan Pilih Menu : ")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Keluar")
    Menu = int(input("Silahkan pilih menu : "))
    if Menu==1:
        time.sleep(1)
        os.system('cls')
        time.sleep(1)
        penjumlahan()
    elif Menu==2:
        time.sleep(1)
        os.system('cls')
        time.sleep(1)
        pengurangan()
    elif Menu==3:
        Exit()
    
    else :
        print("Input anda salah!!")
        os.system("cls")
        menu()


            
def penjumlahan() :
    import random
    import time
    number1 = random.randint(0,9)
    number2 = random.randint(0,9)
    print("="*80)
    print (number1 ,"+",number2, "=")
    hasil1 = number1 + number2
    jawab1 = input ('jawab : ')
    if int(jawab1) == int(hasil1):
        time.sleep(1)
        print("Benar")
        time.sleep(1)
    elif int(jawab1) != int(hasil1) :
        time.sleep(1)
        print("Salah")
        time.sleep(1)
    else:
        print("Masukkan input yang valid")
    check = input ("ketik Y untuk mengulang, ketik selain N untuk berhenti, ketik lainnya untuk keluar : ")
    if check.upper()== "Y" :
        os.system('cls')
        penjumlahan ()
    elif check.upper()== "N" :
        os.system('cls')
        menu()
    Exit()

def pengurangan():
    import random
    import time
    number1 = random.randint(0,9)
    number2 = random.randint(0,9)
    print("="*80)
    print (number1 ,"-",number2, "=")
    hasil1 = number1 - number2
    jawab1 = input ('jawab : ')
    if int(jawab1) == int(hasil1):
        time.sleep(1)
        print("Benar")
        time.sleep(1)
    elif int(jawab1) != int(hasil1) :
        time.sleep(1)
        print("Salah")
        time.sleep(1)
    else:
        print("Masukkan input yang valid")
    check = input ("ketik Y untuk mengulang, ketik selain N untuk berhenti, ketik lainnya untuk keluar : ")
    if check.upper()== "Y" :
        os.system('cls')
        pengurangan ()
    elif check.upper()== "N" :
        os.system('cls')
        menu()
    Exit()

def Exit():
    time.sleep(1)
    os.system('cls')
    print("Sampai jumpa di Pembelajaran selanjutnya")
    time.sleep(2)
    print("Byee")
    time.sleep(2)
    exit()


while True :       
    import time
    import os
    
    time.sleep(1)
    print ("BELAJAR MTK BERSAMA MUAMMAR")
    time.sleep(1)
    os.system('cls')
    menu()
