import requests  # Impordib requests mooduli


# Allalaadimise funktsioon
def download_files(url):
    local_filename = url.split('/')[-1]  # Seab muutuja local_filename väärtuse
    with requests.get(url, stream=True) as r:  # Defineerib muutuja r requests.get funktsiooni parameetritega
        print("Allalaadimine...")  # Printib "Allalaadimine..."
        with open("../"+local_filename, 'wb') as f:  # Defineerib f muutuja local_filename väärtusega
            print("Kirjutan andmed faili")  # Printib "Kirjutan andmed faili"
            for chunk in r.iter_content(chunk_size=8192):  # Defineerib muutuja chunk r.iter_content funktsiooni parameetriga
                f.write(chunk)  # Kirjutab allalaetud informatsiooni faili
    f.close()  # Sulgeb faili
    print("Allalaadimine lõpetatud")  # Printib "Allalaadimine lõpetatud"
    print("Fail salvestatud nimega " + local_filename)  # Printib "Fail salvestatud nimega " + local_filename


while 1:  # Korduv while loop
    print("Tere tulemast pildi allalaadimise programmi") # Printib "Tere tulemast pildi allalaadimise programmi"
    image_url = input(str("Pildi URL : "))  # Küsib kasutaja sisestamist
    download_files(image_url)  # Käivitab funktsiooni
    print("")  # Printib tühja rea
