import pygame
import random

pygame.init()
window = pygame.display.set_mode((405,304))#width and lenght for window
pygame.display.set_caption("Sahil the Knight")#title for heading of pygame window
right = [pygame.image.load("image/k1.png"),pygame.image.load("image/k2.png"),pygame.image.load("image/k3.png"),pygame.image.load("image/k4.png"),pygame.image.load("image/k5.png"),pygame.image.load("image/k6.png"),pygame.image.load("image/k7.png"),pygame.image.load("image/k8.png")]
left = [pygame.image.load("image/k9.png"), pygame.image.load("image/k10.png"), pygame.image.load("image/k11.png"),pygame.image.load("image/k12.png"), pygame.image.load("image/k13.png"), pygame.image.load("image/k14.png"),pygame.image.load("image/k15.png"), pygame.image.load("image/k16.png")]
bg = [pygame.image.load("bg/10.png"),pygame.image.load("bg/6.png"),pygame.image.load("bg/4.png"),pygame.image.load("bg/6.png"),pygame.image.load("bg/3.png"),pygame.image.load("bg/5.png"),pygame.image.load("bg/3.png"),pygame.image.load("bg/5.png")]
bgopen = pygame.image.load("open.png")
hearts = [pygame.image.load("heart/1.png"),pygame.image.load("heart/2.png"),pygame.image.load("heart/3.png"),pygame.image.load("heart/4.png"),pygame.image.load("heart/5.png"),pygame.image.load("heart/6.png"),pygame.image.load("heart/7.png"),pygame.image.load("heart/8.png"),pygame.image.load("heart/9.png"),pygame.image.load("heart/10.png"),pygame.image.load("heart/11.png")]
gameover = pygame.image.load("bg/GAMEO.jpg")
manuals = pygame.image.load("ee.png")
clock = pygame.time.Clock()

deathsound = pygame.mixer.Sound('death.wav')

run = False
def games(run, sound):
    pygame.init()
    window = pygame.display.set_mode((405, 304))
    pygame.display.set_caption("BOSS FIGHT")# title for heading of pygame window
    bg = pygame.image.load("bg.jpg")
    portal = pygame.image.load('image/portal.png')
    winner = pygame.image.load("bg/WIN.jpg")
    clock = pygame.time.Clock()

    bulletsound = pygame.mixer.Sound('bullet.wav')
    hitsound = pygame.mixer.Sound('hit.wav')
    deathsound = pygame.mixer.Sound('death.wav')
    Music = pygame.mixer.music.load('fight.mp3')

    window.blit(bg,(0,0))
    window.blit(portal, (2,225))
    pygame.display.update()
    pygame.time.delay(2000)

    class players(object):
        def __init__(self,x,y,width,height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.velocity = 5
            self.run = True
            self.isjump = False
            self.jumpcount = 10
            self.walkleft = False
            self.walkright = False
            self.wcount = 0
            self.stand = True
            self.border = (self.x + 15, self.y + 11, 29, 52)
            self.score = 0
            self.lifeline = 10
            self.i = 0

        def collide(self):
            self.isjump = False
            self.jumpcount = 10
            self.x = 5
            self.y = 250
            self.wcount = 0
            pygame.time.delay(1000)

        def draws(self,window):
            if self.wcount >= 64:
                self.wcount = 0

            if not(self.stand):
                if self.walkleft:
                    window.blit(left[self.wcount // 8], (self.x, self.y))
                    self.wcount += 1
                elif self.walkright:
                    window.blit(right[self.wcount // 8], (self.x, self.y))
                    self.wcount += 1
            else:
                if self.walkright:
                    window.blit(right[7], (self.x, self.y))
                else:
                    window.blit(left[7], (self.x, self.y))
            self.border = (self.x + 15, self.y + 15, 35, 56)
            if ghost.view == False:
                pygame.time.delay(100)
                window.blit(winner, (0,0))
                pygame.display.update()

    def drawgames():
        window.blit(bg, (0, 0))
        text = fonts.render('LIFE: ', 1, (255, 255, 255),True)
        window.blit(text, (180, 15))
        window.blit(hearts[play.i], (220, 20))
        play.draws(window)
        ghost.draw(window)
        for bullet in bullets:
            bullet.drawing(window)
        pygame.display.update()

    class shoot(object):
        def __init__(self,x,y,radius,color,faced):
            self.x = x
            self.y = y
            self.radius = radius
            self.color = color
            self.faced = faced
            self.vel = 6 * faced

        def drawing(self,window):
            pygame.draw.circle(window, self.color, (self.x,self.y), self.radius)

    class Ghostplay(object):
        Left = [pygame.image.load('ghosts/w1.png'), pygame.image.load('ghosts/w2.png'), pygame.image.load('ghosts/w3.png'),
                     pygame.image.load('ghosts/w4.png'), pygame.image.load('ghosts/w5.png'), pygame.image.load('ghosts/w6.png'), pygame.image.load('ghosts/w7.png'), pygame.image.load('ghosts/w8.png')]
        Right = [pygame.image.load('ghosts/y1.png'), pygame.image.load('ghosts/y2.png'), pygame.image.load('ghosts/y3.png'),
                    pygame.image.load('ghosts/y4.png'), pygame.image.load('ghosts/y5.png'), pygame.image.load('ghosts/y6.png'), pygame.image.load('ghosts/y7.png'), pygame.image.load('ghosts/y8.png')]

        def __init__(self, x, y, width, height, stop):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.stop = stop
            self.root = [self.x, self.stop]
            self.wcount = 0
            self.vel = 5
            self.border = (self.x + 17, self.y + 2, 31, 57)
            self.life = 20
            self.view = True

        def draw(self, window):
            self.go()
            if self.view:
                if self.wcount + 1 >= 64:
                    self.wcount = 0
                if self.vel > 0:
                    window.blit(self.Right[self.wcount // 8], (self.x, self.y))
                    self.wcount += 1
                else:
                    window.blit(self.Left[self.wcount // 8], (self.x, self.y))
                    self.wcount += 1

                pygame.draw.rect(window, (255, 0, 0), (self.border[0]-20, self.border[1] - 20, 100, 10))#to make red color life bar above the ghost bot
                pygame.draw.rect(window, (0, 128, 0), (self.border[0]-20, self.border[1] - 20, 100 -(5*(20 - self.life)), 10))#to make green life bar above the enemy and decrease with eery hit
                self.border = (self.x + 20, self.y + 5, 28, 60)

        def go(self):
            if self.vel > 0:
                if self.x + self.vel < self.root[1]:#check whether enemy is at the end of root at right
                    self.x += self.vel
                else:
                    self.vel = self.vel * -1
                    self.wcount = 0
            else:
                if self.x - self.vel > self.root[0]:#check whether is at left corner
                    self.x += self.vel
                else:
                    self.vel = self.vel * -1
                    self.wcount = 0

        def shots(self):
            if self.life > 0:#checks if the life is greater than the 0 and once it is false then dont display the ghost
                self.life -= 1
            else:
                self.view = False
            print('Shot')

    fonts = pygame.font.SysFont('calibri', 20)
    bullets = []
    play = players(5, 250, 50, 50)
    ghost = Ghostplay(50, 250, 50, 50, 300)

    shooting = 0
    music = False
    if sound == True:
        pygame.mixer.music.play(-1)
        music = True
    while run:
        clock.tick(32)
        if ghost.view == True:#if the ghost is on the screen then only the collision should occur
            if play.border[1] < ghost.border[1] + ghost.border[3] and play.border[1] + play.border[3] > ghost.border[1]:#check wheher the vertcal boundaireis of the both character collide
                if play.border[0] + play.border[2] > ghost.border[0] and play.border[0] < ghost.border[0] + ghost.border[2]:#check wheher the horizontal boundaireis of the both character collide
                    play.collide()
                    play.score -= 1
                    play.lifeline -=1
                    play.i += 1
                    pygame.display.update()
                    if play.score == -10:
                        window.blit(hearts[10],(220,20))
                        pygame.display.update()
                        pygame.time.delay(1000)
                        window.blit(gameover,(0,0))
                        pygame.display.update()
                        deathsound.play()
                        pygame.time.delay(1000)
                        if music == True:
                            Music = pygame.mixer.music.load('run2.mp3')
                            pygame.mixer.music.play(-1)
                        pygame.display.set_caption("Sahil the Knight")
                        dash()

        if shooting > 0:
            shooting += 1
        if shooting > 4:
            shooting = 0

        for event in pygame.event.get():# check all event we do like moving the mouse
            if event.type == pygame.QUIT:
                run = False

        for bullet in bullets:
            if bullet.y - bullet.radius < ghost.border[1] + ghost.border[3] and bullet.y + bullet.radius > ghost.border[1]:#checks whether it is within upper and lower boundary of the ghost border
                if bullet.x + bullet.radius > ghost.border[0] and bullet.x - bullet.radius < ghost.border[0] + ghost.border[2]:#checks whether it is within right and left boundary of the ghost border
                    hitsound.play()
                    ghost.shots()
                    bullets.pop(bullets.index(bullet))

            if bullet.x < 405 and bullet.x > 0:#to make bullet disapper appear after hitting the edge of the window
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_y]:
            pygame.mixer.music.play(-1)
            music = True
        elif keys[pygame.K_n]:
            pygame.mixer.music.stop()
            music = False
        if keys[pygame.K_SPACE] and shooting == 0:
            bulletsound.play()
            if play.walkleft:
                faced = -1
            else:
                faced = 1

            if len(bullets) < 6:
                bullets.append(shoot(round(play.x + play.width // 2), round(play.y + play.height // 2), 3, (255, 0, 0), faced))
            shooting = 1

        if keys[pygame.K_LEFT] and play.x > play.velocity:  # AND condition is to maintain the block within the screen
            play.x -= play.velocity
            play.walkleft = True
            play.walkright = False
            play.stand = False
        elif keys[pygame.K_RIGHT] and play.x < (420 - play.width - play.velocity):
            play.x += play.velocity
            play.walkright = True
            play.walkleft = False
            play.stand = False
        else:
            play.stand = True
            play.wcount = 0
        if not(play.isjump):  # checks whether the variable is filled with none,empty,zero or False and if yes then it will execute
            if keys[pygame.K_UP]:
                play.isjump = True
                play.walkleft = False
                play.walkright = False
                play.wcount = 0
        else:
            if play.jumpcount >= -10:
                neg = 1
                if play.jumpcount < 0:
                    neg = -1
                play.y -= (play.jumpcount ** 2) * 0.35 * neg  # to move box upward and then by decrementing the val of the jumpcount moving it slowly decreasing speed
                play.jumpcount -= 1
            else:
                play.isjump = False
                play.jumpcount = 10
        drawgames()
    pygame.quit()

def dash():
    Music = pygame.mixer.music.load('run2.mp3')
    window.blit(bgopen, (0,0))
    pygame.display.update()
    pygame.time.delay(1000)
    class manual:
        i = 0
    if manual.i == 0:
        window.blit(manuals,(0,0))
        pygame.display.update()
        pygame.time.delay(5000)
        manual.i += 1
    global musics
    musics = False
    class move:
        def update(x):
           return 0
        def place(x):
            return random.randint(80, 290)

    class player(object):
        def __init__(self,x,y,width,height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.isjump = False
            self.jumpcount = 10
            self.right = False
            self.walkright = False
            self.wcount = 0
            self.velocity = 5
            self.rights = True
            self.start = False
            self.border = (self.x + 15, self.y + 11, 29, 52)
            self.i = 0

        def draw(self,window):
            if self.wcount >= 64:
                self.wcount = 0
            if self.walkright:
                window.blit(right[self.wcount // 8], (self.x, self.y))
                self.wcount += 1
            bot.border = (bot.x + 8, bot.y - 8, 20, 48)
            #pygame.draw.rect(window,(255,0,0),self.border,2)

    class obstacle(object):
        block = pygame.image.load('image/stone05.png')
        def __init__(self, x, y, width, height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.border = (self.x + 17, self.y + 2, 30, 30)

        def draw(self,window):
            window.blit(self.block, (self.x, self.y))
            blocked.border = (blocked.x + 50, 140, 30, 10)

    def drawgame():
        window.blit(bg[bot.i], (0, 0))
        bot.draw(window)
        blocked.draw(window)
        if bot.x == 0:
            bot.i += 1
        if bot.i == 8:
            games(True, musics)
        #pygame.draw.rect(window, (255, 0, 0), blocked.border, 2)
        pygame.display.update()

    x = move.place(1)
    bot = player(30,125,50,50)
    blocked = obstacle(x,30,60,20)
    run = True
    while run:
        clock.tick(28)
        if bot.border[1] < blocked.border[1] + bot.border[3] and bot.y + bot.height > blocked.border[1]:# check wheher the vertcal boundaireis of the both character collide
            if bot.border[0] + bot.border[2] > blocked.border[0] and bot.x < blocked.border[0] + blocked.border[2]:# check wheher the horizontal boundaireis of the both character collide
                pygame.time.delay(800)
                window.blit(gameover, (0, 0))
                deathsound.play()
                pygame.display.update()
                pygame.time.delay(3000)
                dash()

        for event in pygame.event.get():#check all event we do like moving the mouse
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_y]:
            musics = True
            pygame.mixer.music.play(-1)
        elif keys[pygame.K_n]:
            musics = False
            pygame.mixer.music.stop()
        if keys[pygame.K_KP_ENTER]:
            bot.start = True
        if bot.start:
            if bot.rights and bot.x <= (450-bot.width-bot.velocity):
                bot.x += bot.velocity
                bot.walkright = True
            else:
                bot.walkright = False
                bot.wcount = 0

            if not(bot.isjump):#checks whether the variable is filled with none,empty,zero or False and if yes then it will execute
                if keys[pygame.K_UP]:
                    bot.isjump = True
                    bot.walkright = False
                    bot.wcount = 0
            else:
                if bot.jumpcount >= -10:
                    neg = 1
                    if bot.jumpcount < 0:
                        neg = -1
                    bot.y -= (bot.jumpcount ** 2) * 0.3 * neg#to move box upward and then by decrementing the val of the jumpcount moving it slowly decreasing speed
                    bot.jumpcount -= 1
                else:
                    bot.isjump = False
                    bot.jumpcount = 10
            if bot.x >= 430-bot.width-bot.velocity:
               bot.x = move.update(x)
            if bot.x == 0:
                x = 1
                x = move.place(x)
                blocked = obstacle(x, 30, 60, 60)
        drawgame()
    pygame.quit()
dash()