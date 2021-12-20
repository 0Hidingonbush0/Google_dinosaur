import sys
import pygame as pyg
import random

class Hrac(pyg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.char_walk = pyg.image.load("Veci/figure/king1.png").convert_alpha()
        self.char_walk_2 = pyg.image.load("Veci/figure/king2.png").convert_alpha()
        self.char_walk_3 = pyg.image.load("Veci/figure/king3.png").convert_alpha()
        self.char_jump = pyg.image.load("Veci/figure/kingjump.png").convert_alpha()
        self.rect = self.char_walk.get_rect(midbottom= (150, 500))
        screen.blit(self.char_walk, self.rect)
        self.gravity =0

    def PlayerInput(self):
        self.keys= pyg.key.get_pressed()
        if self.keys[pyg.K_SPACE] or self.keys[pyg.K_UP]:
            self.gravity = -20

    def Gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 502:
            self.rect.bottom = 502
        if self.rect.left <= 0:
            self.rect.left = 0

    def update(self):
        self.Hrac.PlayerInput()
        self.Hrac.Gravity()

def intro():
    screen.fill([0, 176, 178])
    screen.blit(blaha_intro, blaha_rect_intro)
    font_69 = pyg.font.Font("font/UpheavalPro.ttf", 60)
    nadpis = font_69.render("DON'T TOUCH BLAHA!", False, "#fcc729")
    nadpis_rect = nadpis.get_rect(midtop=(375, 50))
    screen.blit(nadpis, nadpis_rect)
    press_start = font.render("Pro spuštění stiskni libovolnou klávesu", False, "#fcc729")
    press_start_rect = press_start.get_rect(midtop=(375, 390))
    screen.blit(press_start, press_start_rect)


def outro():
    screen.fill("#000000")
    screen.blit(blaha_intro, blaha_rect_intro)
    font_69 = pyg.font.Font("font/UpheavalPro.ttf", 60)
    nadpis = font_69.render("BLAHA TOUCHED U!", False, "#fcc729")
    nadpis_rect = nadpis.get_rect(midtop=(375, 50))
    screen.blit(nadpis, nadpis_rect)
    skore = font.render(f"Tvoje skóre: {score}", False, "#fcc729")
    skore_rect = skore.get_rect(midtop=(375, 390))
    screen.blit(skore, skore_rect)


def prisery_pohyb(prisery_list):
    if prisery_list:
        for prisery_rect in prisery_list:
            prisery_rect.x -= 10

            if prisery_rect.bottom == 450:
                screen.blit(blaha_dva, prisery_rect)
            else:
                screen.blit(blaha, prisery_rect)
        prisery_list = [prisery for prisery in prisery_list if prisery.x > 0]

        return prisery_list
    else:
        return []

def dotyk(hrac, prisera):
    if prisera:
        for prisera_rect in prisera:
            if hrac.colliderect(prisera_rect):
                return False
    return True

def animace_hrace():
    keys = pyg.key.get_pressed()
    global char_fig, char_index
    if char_rect.bottom <497:
        char_fig = char_jump_1
    else:
        char_index += 0.05
        if char_index >= len(char_walk_list):
            char_index =1
        char_fig = char_walk_list[int(char_index)]


#Základní parametry
pyg.init()
screen = pyg.display.set_mode((750, 598))
pyg.display.set_caption("My 1st game")
clock = pyg.time.Clock()
font = pyg.font.Font("font/UpheavalPro.ttf", 25)
start_time = 0
player_gravity = 0
game_active = False
flip_right = True
score = 0


#intro
blaha_intro = pyg.image.load("Veci/figure/příšery/blahavelky.jpg").convert_alpha()
blaha_intro = pyg.transform.rotozoom(blaha_intro, 0, 0.4)
blaha_rect_intro = blaha_intro.get_rect(midtop=(375, 299))


prisery_rect_list = []
# timer
prisera_timer = pyg.USEREVENT + 1
pyg.time.set_timer(prisera_timer, random.randint(2000, 2500))


# příšery
blaha = pyg.image.load("Veci/figure/příšery/blaha1.png").convert_alpha()
blaha_rect = blaha.get_rect(midbottom=(500, 500))

blaha_dva = pyg.image.load("Veci/figure/příšery/blaha2.png").convert_alpha()
blaha_dva_r = blaha_dva.get_rect(midbottom=(500, 450))

# pozadí
background = pyg.image.load("Veci/ground/bckgr.png").convert_alpha()
floor = pyg.image.load("Veci/ground/ground1.png").convert_alpha()
floor_rect = floor.get_rect(bottomleft=(0, 598))

    # hrdina
char_walk_1 = pyg.image.load("Veci/figure/king1.png").convert_alpha()
char_walk_2 = pyg.image.load("Veci/figure/king2.png").convert_alpha()
char_walk_3 = pyg.image.load("Veci/figure/kingjump.png").convert_alpha()
char_jump_1 = pyg.image.load("Veci/figure/king3.png").convert_alpha()
char_walk_list = [char_walk_1, char_walk_2, char_walk_3]
char_index = 0

char_fig = char_walk_list[char_index]
char_rect = char_fig.get_rect(midbottom=(50, 498))


hrac = pyg.sprite.GroupSingle()
hrac.add(Hrac())
def stopky():
    cas = int((pyg.time.get_ticks() - start_time)/1000)
    skore = font.render(f"Skóre: {cas}", False, (64, 64, 64))
    skore_rect = skore.get_rect(topright=(740, 50))
    pyg.draw.rect(screen, "#33ABF9", skore_rect, 0, 7)
    screen.blit(skore, skore_rect)
    return cas


def obraz():
    global player_gravity, game_active, start_time, flip_right, score, blaha_rect, prisery_rect_list

    while True:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                sys.exit()
            #if event.type == pyg.MOUSEMOTION:
            #if king_rect.collidepoint(event.pos):
            #print("dotyk")
            if game_active:
                if char_rect.bottom == 502:
                    if event.type == pyg.MOUSEBUTTONDOWN:
                        player_gravity = -20
            else:
                if event.type == pyg.KEYDOWN:
                    game_active = True
                    blaha_rect.x = 700
                    start_time = pyg.time.get_ticks()
            if event.type == prisera_timer and game_active:
                if random.randint(0,2):
                    prisery_rect_list.append(blaha.get_rect(midbottom=(random.randint(900, 1100), 500)))
                else:
                    prisery_rect_list.append(blaha_dva.get_rect(midbottom=(random.randint(900, 1100), 450)))

        #pozadí
        if game_active:
            screen.blit(background, (0, 0))
            screen.blit(floor, floor_rect)
            screen.blit(floor, (95, 500))
            screen.blit(floor, (190, 500))
            screen.blit(floor, (285, 500))
            screen.blit(floor, (380, 500))
            screen.blit(floor, (475, 500))
            screen.blit(floor, (570, 500))
            screen.blit(floor, (665, 500))
            score = stopky()
            #hrdina
            animace_hrace()
            screen.blit(char_fig, char_rect)
            #příšery pohyb
            prisery_rect_list = prisery_pohyb(prisery_rect_list)

            #player_input
            keys = pyg.key.get_pressed()
            if char_rect.bottom == 502:
                if keys[pyg.K_SPACE] or keys[pyg.K_d] or keys[pyg.K_UP] :
                    player_gravity = -17
            #if keys[pyg.K_d] or keys[pyg.K_RIGHT]:
                #char_rect.x +=3
            #if keys[pyg.K_a] or keys[pyg.K_LEFT]:
                 #char_rect.x -=3

            #gravitace
            player_gravity += 1
            char_rect.y += player_gravity
            if char_rect.bottom >= 502:
                char_rect.bottom = 502
            if char_rect.left <=0:
                char_rect.left =0


            #dotyk
            game_active = dotyk(char_rect, prisery_rect_list)
        else:
            char_rect.midbottom=(50, 499)
            prisery_rect_list.clear()
            if score == 0:
                intro()
            else:
                outro()
        pyg.display.update()
        clock.tick(60)


obraz()
