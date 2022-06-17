# Impordime vajalikud moodulid
import pygame
import sys
pygame.init()  # alustame pygame mooduli

# Seadistame värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]

# Seadistame ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Ping-pong - Tamm")
screen.fill(lBlue)
clock = pygame.time.Clock()

# Seadistame palli kiiruse ja positsiooni
posX, posY = 0, 0
speedX, speedY = 3, 4

# Seadistame aluse kiiruse ja positsiooni
alusX, alusY = 0, screenY/1.5
alusSpeedX = 2

# Piltide laadimine
pall = pygame.Rect(posX, posY, 20, 20)
palliPilt = pygame.image.load("yl5_pall.png")
palliPilt = pygame.transform.scale(palliPilt, (20, 20))
alus = pygame.Rect(alusX, alusY, 120, 20)
alusePilt = pygame.image.load("yl5_alus.png")
alusePilt = pygame.transform.scale(alusePilt, (120, 20))

# Scoori muutuja seadistamine
skoor = 0

gameover = False  # gameover muutuja seadistamine
while not gameover:  # kordub, kuni gameover muutuja on False
    clock.tick(60)  # seadistame kaadrisageduse
    for event in pygame.event.get():  # sündmuse käitlemine
        if event.type == pygame.QUIT:  # kui aken suletakse
            sys.exit()  # lõpetame mängu

    # Palli liikumine
    pall = pygame.Rect(posX, posY, 20, 20)
    screen.blit(palliPilt, pall)
    posX += speedX
    posY += speedY

    # Aluse liikumine
    alus = pygame.Rect(alusX, alusY, 120, 20)
    screen.blit(alusePilt, alus)
    alusX += alusSpeedX

    # Skoori kuvamine
    screen.blit(pygame.font.Font(None, 30).render(f"Skoor: {skoor}", True, [255, 255, 255]), [10, 20])

    # Kui puudutab ekraani ääri, muudab palli suunda
    if posX > screenX - palliPilt.get_rect().width or posX < 0:
        speedX = -speedX
    if posY > screenY-palliPilt.get_rect().height or posY < 0:
        speedY = -speedY
        if posY > screenY-palliPilt.get_rect().height:
            skoor -= 1

    # Kui puudutab alust, muudab palli suunda ja suurendab skoori
    if pall.colliderect(alus) and speedY > 0:
        speedY = -speedY
        skoor += 1

    # Kui puudutab ekraani ääri, muudab aluse suunda
    if alusX > screenX - alusePilt.get_rect().width or alusX < 0:
        alusSpeedX = -alusSpeedX

    # Graafika kuvamine ekraanil
    pygame.display.flip()
    screen.fill(lBlue)  # Et vanad pildid ei jääks peale

pygame.quit()  # Kui mäng on läbi
