import random
import os
import time

def play():
    print("="*70)
    print("Tentukan pilihanmu ! G untuk gunting, B untuk batu, K untuk kertas !")
    print("e untuk keluar\n")
    pemain = input("Pilihan : ")
    bot = random.choice(['b', 'k', 'g'])

    if pemain == bot:
        time.sleep(1)
        print("Kamu Seri")
        time.sleep(1)
        print("="*70)
        time.sleep(1)
        os.system('cls')
        play()

    elif pemain.upper()=="E":
        time.sleep(1)
        os.system('cls')
        menu()

    # b > g, g > k, k > b
    if is_win(pemain, bot):
        time.sleep(1)
        print("kamu kalah!")
        time.sleep(1)
        print("="*70)
        time.sleep(1)
        os.system('cls')
        play()
        menu()

    elif is_lose(pemain, bot):
        time.sleep(1)
        print("kamu menang!")
        time.sleep(1)
        print("="*70)
        time.sleep(1)
        os.system('cls')
        play()
        menu()
    
    else :
        os.system('cls')
        print("="*70)
        print("Masukkan input dengan benar!")
        print("="*70)
        time.sleep(1)
        os.system('cls')
        play()
        

def is_lose(pemain, bot):
    if (pemain == 'g' and bot == 'b') or (pemain == 'k' and bot == 'g') \
        or (pemain == 'b' and bot == 'k'):
        return True

def is_win(pemain, bot):
    # return true if pemain wins
    # r > s, s > p, p > r
    if (pemain == 'b' and bot == 'g') or (pemain == 'g' and bot == 'k') \
        or (pemain == 'k' and bot == 'b'):
        return True

def menu():
    import os
    print("Apakah masih ingin bermain?")
    time.sleep(1)
    print("Ketik Y untuk lanjut, ketik N untuk keluar")
    time.sleep(1)
    lanjut = input("Pilihan : ")
    if lanjut.upper()=="Y":
        os.system('cls')
        time.sleep(2)
        play()
    else :
        time.sleep(1)
        os.system('cls')
        print("Sampai Jumpa. Semoga harimu menyenangkan!")
        time.sleep(3)
        os.system('cls')
        exit()


print("="*70)
time.sleep(1)
print("MARI BERMAIN SUIT BERSAMA AMAR")
time.sleep(2)
print("="*70)
time.sleep(1)
os.system('cls')
print(play())
