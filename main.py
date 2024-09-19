import random
print("GAME BY MUHAMMAD AINUL FUADY!")

welcome_message = "WELCOME TO CUYPY GAMES!"
cuypy_position = random.randint(1, 4)

print("*****************************")
print(f"** {welcome_message} **")
print("*****************************")

nama_users = input("Masukan nama kamu: ")

print(f'''Halo {nama_users}! Coba perhatikan goa dibawah ini!
|_| |_| |_| |_|
''')

pilihan_user = int(
    input("Menurut kamu di goa nomer berapa CUYPY berada? [1 / 2 / 3 / 4]: "))

confirm = input("Apakah anda yakin dengan pilihannya? (iya/tidak): ")
if confirm.lower() == 'tidak':
    exit()

if cuypy_position == pilihan_user:
    print(f"Selamat {nama_users} kamu menang gg kamu! posisi CUYPY ada di goa nomer {
          cuypy_position} dan pilihanmu adalah goa nomor {pilihan_user}.")
else:
    print(f"Kamu kalah CUYPY bukan berada di situ, tapi ada di goa nomor {
          cuypy_position}. sedangkan kamu memilih goa nomer {pilihan_user} ")
