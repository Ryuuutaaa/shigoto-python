import random

welcome_massage = "RYUPY GAMESS"
ryupy_position = random.randint(1,4)

print("****************************************")
print(f"** {welcome_massage} **")
print("****************************************")

nama_user = input("Masukan nama andaa = ")
print(f''' Haaloo {nama_user} coba perhatikan goa berikut |_| |_| |_| ''')

pilihan_user = int(input("Menurut kamu di goa nomor berapa RYU berada?? [1/2/3/4] = "))

print(f"Pilihan kamu adalah {pilihan_user}")

if pilihan_user == ryupy_position : 
    print(f"SELAMAT {nama_user} KAMU MENANG!!!!, goa berada di nomor {ryupy_position}")
else : 
    print(f"{nama_user} KAMU KALAH? ryupy tidak ada disitu, goa berada di nomor {ryupy_position}")