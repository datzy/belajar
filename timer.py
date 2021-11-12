import time
import os

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print ('Timer Selesai')
    time.sleep(1)
    keluar()


def keluar():
    lanjut=input(str('apakah ingin mengulang ? Y untuk ya, dan lainya untuk tidak. '))
    if lanjut.upper()=="Y":
        time.sleep(1)
        os.system('cls')
        t = input('Masukkan waktu dalam detik : ')
        countdown(int(t))

    else :
        os.system('cls')
        print('Sampai jumpa. Semoga harimu menyenangkan!!')
        time.sleep(3)
        os.system('cls')
        exit()


print("="*70)
time.sleep(2)
print("MARI MENGGUNAKAN TIMER BERSAMA MUAMMAR")
time.sleep(2)
print("="*70)
time.sleep(2)
os.system('cls')
t = input('Masukkan waktu dalam detik : ')
countdown(int(t))