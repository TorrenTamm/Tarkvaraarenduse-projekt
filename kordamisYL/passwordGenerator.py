import random # Impordib random mooduli

chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()'  # Seadistab kasutatavad sümbolid

while 1: # Korduv while loop
    password_len=int(input('Sisesta parooli pikkus: '))  # Küsi kasutajalt parooli pikkust
    password_count=int(input('Sisesta, mitu parooli tehakse: ')) # Küsi kasutajalt mitu parooli teha
    for x in range (0, password_count):  # Kordus, mis loob paroolid
        password = ''  # Loob password muutuja
        for x in range (0, password_len):  # Kordus, mis loob parooli tähed
            password_char = random.choice(chars)  # Leiab suvalise märgi
            password = password + password_char  # Lisab selle suvalise märgi parooli lõppu
        print('Siin on teie parool: ', password)  # Printib passwordi