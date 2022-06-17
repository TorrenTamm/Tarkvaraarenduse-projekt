# Torren Tamm, IS21
# Ülesanne 4: Objektide animeerimine

import pygame
import random
import sys
import time
# Impordib vajalikud moodulid

pygame.init()  # alustame pygame mooduli
screen = pygame.display.set_mode((640, 480))  # Seadistame enkraani suuruse
pygame.display.set_caption("Ül4: Animeerimine - Tamm")  # Seadistame akna tiitli

clock = pygame.time.Clock()  # Loome 'clock' objekti

startTime = time.time()  # Saame alustamise aja
score = 0  # seadistame skoori muutuja

bg = pygame.image.load("bg_rally.jpg")  # Laadime taustapildi
bg2 = pygame.image.load("bg_rally.jpg")  # Laadime teise taustapildi mida on vaja animatsiooniks
bgposX = 0  # esimese taustapildi X positsioon
bg2posX = 480  # teise taustapildi X positsioon
bgspeedX = -3  # taustapildi animatsiooni X kiirus

f1Blue = pygame.image.load("f1_blue.png")  # laadime auto pildi
f1Blue = pygame.transform.rotate(f1Blue, 180)  # keerame auto pildi ümber

f1Blue2 = pygame.image.load("f1_blue.png")  # laadime teise auto pildi
f1Blue2 = pygame.transform.rotate(f1Blue2, 180)  # keerame auto pildi ümber

f1Red = pygame.image.load("f1_red.png")  # laadime auto pildi

gameover = False  # seadistame gameover muutuja

blueSpeedY = 3  # sinise auto kiirus Y

bluePosY = random.randint(0, 100)  # sinise auto positsioon Y
blue2PosY = random.randint(0, 100)  # 2 sinise auto positsioon Y
redPosX, redPosY = 298, 390  # punase auto positsioonid
redSpeedY = 0  # punase auto kiirus Y
bluePosX = random.randint(300, 460)  # sinise auto positsioon X
blue2PosX = random.randint(130, 280)  # 2 sinise auto positsioon X

while not gameover:  # kordub, kuni gameover muutuja on False
    clock.tick(120)  # seadistame kaadrisageduse

    for event in pygame.event.get():  # sündmuse käitlemine
        if event.type == pygame.QUIT:  # kui aken suletakse
            sys.exit()  # lõpetame mängu

    # taustapiltide lisamine
    screen.blit(bg, (0, bgposX))
    screen.blit(bg2, (0, bg2posX))

    # kiiruse kasutamine
    bgposX -= bgspeedX
    bg2posX -= bgspeedX

    # kui taustapilt jõuab lõppu, viime tagasi algusesse
    if bgposX >= 480:
        bgposX = -480
    if bg2posX >= 480:
        bg2posX = -480

    # siniste autode lisamine
    screen.blit(f1Blue, (bluePosX, bluePosY))
    screen.blit(f1Blue2, (blue2PosX, blue2PosY))

    # autode liigutamine
    bluePosY += blueSpeedY + 0.8
    blue2PosY += blueSpeedY + 1

    # punase auto lisamine
    screen.blit(f1Red, (redPosX, redPosY))
    redPosY += redSpeedY  # auto liigutamine

    # skoori kuvamine
    screen.blit(pygame.font.Font(None, 30).render(f"Skoor: {score}", True, [255, 255, 255]), [10, 20])

    # autode positsiooni taastamine
    if bluePosY >= 480:  # kui auto jõuab lõppu
        bluePosY = -120  # taastame auto positsiooni
        score += 1  # suurendame skoori
        bluePosX = random.randint(130, 280)  # paneme auto suvalisse kohta

    if blue2PosY >= 480:  # kui 2 auto jõuab lõppu
        blue2PosY = -120  # taastame positsiooni
        score += 1  # suurendame skoori
        blue2PosX = random.randint(300, 480)  # paneme auto suvalisse kohta

    if redPosY >= 480:  # kui punane auto lahkub ekraanilt
        redPosY = -120  # taastame positsiooni

    # punase auto liigutamine
    key = pygame.key.get_pressed()  # saame vajutatud klahvi
    if key[pygame.K_LEFT]:  # kui vasak klahv
        redPosX -= 5  # liigutame autot vasakule
    if key[pygame.K_RIGHT]:  # kui parem klahv
        redPosX += 5  # liigutame autot paremale

    # mängu lõpp, kui sinine auto puudutab punast
    if redPosY + 55 >= bluePosY >= redPosY - 55:  # kui sinine ja punane auto on samal Y kordinaadil
        if redPosX + 50 >= bluePosX >= redPosX - 50:  # kui sinine ja punane auto on ka samal X kordinaadil
            gameover = True  # lõpetame mängu

    if redPosY + 55 >= blue2PosY >= redPosY - 55:  # kui sinine 2 ja punane auto on samal Y kordinaadil
        if redPosX + 50 >= blue2PosX >= redPosX - 50:  # kui sinine 2 ja punane auto on ka samal X kordinaadil
            gameover = True  # lõpetame mängu

    # suurendame kiirust iga 10 sekundi tagant
    if time.time() % 10 == 0:  # kui aeg on 10 jagatav
        blueSpeedY += 1  # suurendame kiirust 1 võtta

    # kuvame aega
    screen.blit(pygame.font.Font(None, 20).render(f"Aeg: {int(time.time() - startTime)}",
                                                  True, [255, 255, 255]), [10, 460])
    pygame.display.flip()  # värskendame ekraani

while True:  # lõppematu kordus, et kontrollida kas mäng on läbi
    if gameover:  # kui mäng on läbi
        # kuvame "Mäng läbi!"
        screen.blit(pygame.font.Font(None, 50).render("Mäng läbi!", True, [255, 255, 255]), [230, 300])
        # kuvame skoori
        screen.blit(pygame.font.Font(None, 50).render(f"Skoor: {score}", True, [255, 255, 255]),
                    [240, 200])
        pygame.display.flip()  # uuendame ekraani

    for event in pygame.event.get():  # ootame sündmust
        if event.type == pygame.QUIT:  # kui ekraan suletakse
            sys.exit()  # lõpetame mängu
