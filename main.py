import random

welcome_massage = "RYUPY GAMESS"
ryupy_position = random.randint(1,4)

print("****************************************")
print(f"** {welcome_massage} **")
print("****************************************")

nama_user = input("Masukan nama andaa = ")

bentuk_goa = "|_|"
goa_kosong = [bentuk_goa] * 4 # Ini tetap harus kosong
goa = goa_kosong.copy() # ini tempat baru untuk ryupy   

goa[ryupy_position - 1] = "|0_0|"

print(f''' Haaloo {nama_user} coba perhatikan goa berikut {goa_kosong} ''')

pilihan_user = int(input("\nMenurut kamu di goa nomor berapa RYU berada?? [1/2/3/4] = "))

confirm_answer = input("\nYakin dengan jawabanmu ? [y/n]")

if confirm_answer == "n" : 
    print("Program dihentikan!!!!")
    exit()
elif confirm_answer == "y" :
    if pilihan_user == ryupy_position : 
        print(f"\n{goa}, SELAMAT KAMU MENANG!!!!")
    else : 
        print(f"\n{goa}, MAAF KAMU KALAHHH!!!")
else : 
    print("\nprogram berakhir silahkan coba lagi nantiiii")
    exit()