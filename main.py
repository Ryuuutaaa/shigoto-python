import random

welcome_massage = "RYUPY GAMESS"
ryupy_position = random.randint(1,4)

print("****************************************")
print(f"** {welcome_massage} **")
print("****************************************")

nama_user = input("Masukan nama andaa = ")

while nama_user == "" : 
    nama_user = input("Masukan dulu nama kamu siapaa??? ")

bentuk_goa = "|_|"
goa_kosong = [bentuk_goa] * 4 # Ini tetap harus kosong

goa = goa_kosong.copy() # ini tempat baru untuk ryupy   
goa[ryupy_position - 1] = "|0_0|"

goa_kosong = " ".join(goa_kosong)
goa = " ".join(goa)

print(f''' Haaloo {nama_user} coba perhatikan goa berikut {goa_kosong} ''')

while True:
    pilihan_user = input("\nMenurut kamu di goa nomor berapa RYU berada?? [1/2/3/4] = ")
    if pilihan_user not in ['1', '2', '3', '4']:
        print("Yang bener aja, angka cuma 1 2 3 4 jangan yang lain!!!, MASUKAN LAGI ")
    else:
        pilihan_user = int(pilihan_user)
        break

confirm_answer = input("\nYakin dengan jawabanmu ? [y/n]")

if confirm_answer == "n" : 
    print("Program dihentikan!!!!")
    exit()
elif confirm_answer == "y" :
    if pilihan_user == ryupy_position : 
        print(f"\n{goa}, SELAMAT KAMU MENANG!!!!")
    else : 
        print(f"\n{goa} MAAF KAMU KALAHHH!!!")
else : 
    print("\nprogram berakhir silahkan coba lagi nantiiii")
    exit()