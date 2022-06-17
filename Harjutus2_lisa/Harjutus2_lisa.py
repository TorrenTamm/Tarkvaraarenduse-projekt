import pygame
pygame.init()

# Github: https://github.com/RovanGitHub/Tarkvaraarenduse-projekt

#ekraani seaded
screen=pygame.display.set_mode([640,480]) # teeb akna suurusega 640x480
pygame.display.set_caption("Harjutus 2") # paneb akna nimeks Harjutus 2

# Pood
bg = pygame.image.load("bg_shop.png") # seab akna taustaks poe pildi
screen.blit(bg,[0,0]) # toob pildi välja ja paigutab

# Logo
logo = pygame.image.load("logo.png")  # laeb logo
logo = pygame.transform.scale(logo, [222, 64])  # muudab logo suurust
screen.blit(logo, [10, 20])  # paigutab logo

# Mehike
seller = pygame.image.load("seller.png") # toob sisse mehikese pildi
seller = pygame.transform.scale(seller, [252, 303]) # muudab pildi suurust
screen.blit(seller,[103,161]) # toob mehikese välja ja muuda asukohta

# Jutumull
mull = pygame.image.load("chat.png") # toob sisse jutumulli
mull = pygame.transform.scale(mull, [258, 203]) # muudab jutumulli suurust
screen.blit(mull,[255,65]) # toob jutumulli välja ja muudab asukohta

#lisame teksti
font = pygame.font.SysFont('arial', 22, bold=True) # seadistab fondi arial, suurus 22 ja teeb boldiks
text = font.render("Tere, olen Torren Tamm", True, [255,255,255]) # seab teksti ja teksti valge värvina
screen.blit(text, [280,135]) # toob teksti välja ja muudab asukohta

# Mõõk
mook = pygame.image.load("mõõk.png")  # toob sisse mõõga
mook = pygame.transform.scale(mook, [208, 153]) # muudab mõõga suurust
mook = pygame.transform.rotate(mook, -35) # keerab mõõka
screen.blit(mook, [453, 145]) # toob mõõga välja ja muudab asukohta

# Tort
tort = pygame.image.load("tort.png")  # laeb tordi
tort = pygame.transform.scale(tort, [95,75])  # muudab tordi suurust
screen.blit(tort,[330,220])  # toob tordi välja ja muudab asukohta


pygame.display.flip() # värskendab ekraani



# selle jaoks et aken ära ei kaoks ja kinni saaks panna, internetist võetud.
running = True
while running:
    ev = pygame.event.get()

    for event in ev:

        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            print(x, y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if running == False:
            pygame.quit()