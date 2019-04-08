import pygame
import random
import game1

pygame.init()
window = pygame.display.set_mode((405,304))#width and lenght for window
pygame.display.set_caption("Sahil the Knight")#title for heading of pygame window
right = [pygame.image.load("image/k1.png"),pygame.image.load("image/k2.png"),pygame.image.load("image/k3.png"),pygame.image.load("image/k4.png"),pygame.image.load("image/k5.png"),pygame.image.load("image/k6.png"),pygame.image.load("image/k7.png"),pygame.image.load("image/k8.png")]
bg = [pygame.image.load("bg/10.png"),pygame.image.load("bg/6.png"),pygame.image.load("bg/4.png"),pygame.image.load("bg/6.png"),pygame.image.load("bg/3.png"),pygame.image.load("bg/5.png"),pygame.image.load("bg/3.png"),pygame.image.load("bg/5.png")]
bg1 = pygame.image.load("bg.jpg")
gameover = pygame.image.load("bg/7.png")
clock = pygame.time.Clock()

deathsound = pygame.mixer.Sound('death.wav')
Music = pygame.mixer.music.load('run.mp3')

def dash():
    global musics
    musics = False
    class move:
        def update(x):
           x = 0
           return x
        def place(x):
            x = random.randint(80, 290)
            return x

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
            bot.border = (bot.x - 8, bot.y - 8, 35, 56)
            #pygame.draw.rect(window,(255,0,0),self.border,2)

    class obstacle(object):
        block = pygame.image.load('image/stone05.png')
        def __init__(self, x, y, width, height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.wcount = 0
            self.vel = 5
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
            game1.games(True, musics)
        #pygame.draw.rect(window, (255, 0, 0), blocked.border, 2)
        pygame.display.update()

    run = True
    x = 1
    x = move.place(x)
    bot = player(30,125,50,50)
    blocked = obstacle(x,30,60,20)
    while run:
        clock.tick(28)
        if bot.border[1] < blocked.border[1] + bot.border[3] and bot.y + bot.height > blocked.border[1]:# check wheher the vertcal boundaireis of the both character collide
            if bot.border[0] + bot.border[2] > blocked.border[0] and bot.x < blocked.border[0] + blocked.border[2]:# check wheher the horizontal boundaireis of the both character collide
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
               bot.x = move.update(bot.x)
            if bot.x == 0:
                x = 1
                x = move.place(x)
                blocked = obstacle(x, 30, 60, 60)
        drawgame()
    pygame.quit()
dash()