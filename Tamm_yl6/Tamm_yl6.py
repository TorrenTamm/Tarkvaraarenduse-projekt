# Torren Tamm - IS21
# Ülesanne 6

# Impordime vajalikud moodulid
import pygame
import sys
import time
pygame.init()  # alustame pygame mooduli

# Seadistame värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
white = [255, 255, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]

# Taustamuusika
pygame.mixer.music.load('yl6_muusika.mp3')
pygame.mixer.music.play(-1)  # -1, et mängiks lõputult

# Seadistame ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Ping-pong - Tamm")
screen.fill(lBlue)  # Muudame tausta helesiniseks
clock = pygame.time.Clock()  # Loome 'clock' objekti

startTime = time.time()  # Saame alustamise aja
skoor = 0  # Seadistame skoori muutuja

# Seadistame palli kiiruse ja positsiooni
posX, posY = 0, 0
speedX, speedY = 3, 4

# Seadistame aluse kiiruse ja positsiooni
alusX, alusY = 0, screenY/1.5
alusSpeedX = 3

# Objektide seadistamine
pall = pygame.Rect(posX, posY, 20, 20)  # Loome palli objekti
palliPilt = pygame.image.load("yl6_pall.png")  # Laeme palli pildi
palliPilt = pygame.transform.scale(palliPilt, (20, 20))  # Muudame palli pildi suurust
alus = pygame.Rect(alusX, alusY, 120, 20)  # Loome aluse objekti
alusePilt = pygame.image.load("yl6_alus.png")  # Laeme aluse pildi
alusePilt = pygame.transform.scale(alusePilt, (120, 20))  # Muudame aluse pildi suurust

gameover = False  # gameover muutuja seadistamine
while not gameover:  # kordub, kuni gameover muutuja on False
    clock.tick(60)  # seadistame kaadrisageduse
    for event in pygame.event.get():  # sündmuse käitlemine
        if event.type == pygame.QUIT:  # kui aken suletakse
            gameover = True
            sys.exit()  # lõpetame mängu

        # Aluse liigutamine klahvide abil
        elif event.type == pygame.KEYDOWN:  # Kui vajutatakse alla klahv
            if event.key == pygame.K_RIGHT:  # Kui see klahv on parem nool
                alusSpeedX = 3  # Paneme aluse paremale liikuma
            elif event.key == pygame.K_LEFT:  # Kui see klahv on vasak nool
                alusSpeedX = -3  # Paneme aluse vasakule liikuma

    # Palli liikumine
    pall = pygame.Rect(posX, posY, 20, 20)  # Paneme palli õigele positsioonile
    screen.blit(palliPilt, pall)  # Lisame pildi palli objektile
    posX += speedX  # Palli X teljel liikumine
    posY += speedY  # Palli Y teljel liikumine

    # Aluse liikumine
    alus = pygame.Rect(alusX, alusY, 120, 20)  # Paneme aluse õigele positsioonile
    screen.blit(alusePilt, alus)  # Lisame pildi aluse objektile
    alusX += alusSpeedX  # Aluse liigutamine

    # Skoori kuvamine
    screen.blit(pygame.font.Font(None, 30).render(f"Skoor: {skoor}", True, white), [10, 20])

    # Kui puudutab ekraani ääri, muudab palli suunda
    if posX > screenX - palliPilt.get_rect().width or posX < 0:  # Kui pall puudutab vasakut või paremat äärt
        speedX = -speedX  # Muudab palli suunda
    if posY < 0:  # Kui pall puudutab ülemist äärt
        speedY = -speedY  # Muudab palli suunda
    if posY > screenY-palliPilt.get_rect().height:  # Kui pall puudutab alumist äärt
        # Mäng läbi
        pygame.mixer.music.stop()  # Lõpetab taustamuusika
        # Kuvame "Mäng läbi" ja skoori
        screen.blit(pygame.font.Font(None, 50).render("Mäng läbi!", True, white), [230, 300])
        screen.blit(pygame.font.Font(None, 50).render(f"Skoor: {skoor}", True, white), [240, 200])  # Kuvab skoori

    # Kui puudutab alust, muudab palli suunda ja suurendab skoori
    if pall.colliderect(alus) and speedY > 0:
        speedY = -speedY
        skoor += 1

    # Kui puudutab ekraani ääri, peatab aluse
    if alusX > screenX - alusePilt.get_rect().width or alusX < 0:
        alusSpeedX = 0

    # Kuvame aja
    screen.blit(pygame.font.Font(None, 20).render(f"Aeg: {int(time.time() - startTime)}", True, white), [10, 460])

    # Graafika kuvamine ekraanil
    pygame.display.flip()
    screen.fill(lBlue)  # Et vanad pildid ei jääks peale
