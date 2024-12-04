# -*- coding: utf-8 -*-
import pygame, sys, random
from pygame.locals import *
####################################
#PHẦN 1: ĐỊNH NGHĨA CÁC THAM SỐ ##
#####################################
###KÍCH THƯỚC KHUNG MÀN HÌNH GAME
WINDOWWIDTH_G213NTD = 400
WINDOWHEIGHT_G213NTD = 600
###KHỞI TẠO THƯ VIỆN ĐỂ DÙNG
pygame.init()

##TỐC ĐỘ KHUNG HÌNH CỦA VIDEO
FPS = 60 # Famres Per Second
fpsClock = pygame.time.Clock() #Lặp theo nhịp clock (tham số FPS) 
####################################
#####PHẦN 2: NỀN GAME ##############
#####################################
#TỐC ĐỘ CUỘN NỀN
BGSPEED = 1.5 # tốc độ cuộn nền
BGIMG = pygame.image.load('./G213NTD_GAME/img/background.png') # hình nền

# LAYER (SURFACE) NỀN
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH_G213NTD, WINDOWHEIGHT_G213NTD))
pygame.display.set_caption('Ma Hoa = G213NTD_CARRACING: Game = Game ĐUA XE')

# LỚP HÌNH NỀN = CUỘN NỀN
class Background():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = BGSPEED
        self.img = BGIMG
        self.width = self.img.get_width()
        self.height = self.img.get_height()
    def draw(self):
        DISPLAYSURF.blit(self.img, (int(self.x), int(self.y)))
        DISPLAYSURF.blit(self.img, (int(self.x), int(self.y-self.height)))
    def update(self):
        self.y += self.speed
        if self.y > self.height:
            self.y -= self.height

####################################
#####PHẦN 3: XE TRONG GAME #########
"""
•	X_MARGIN là lề hai bên trái và phải (xe không được vượt qua đó).
•	CARWIDTH và CARHEIGHT là kích thước của xe.
•	CARSPEED là tốc độ di chuyển (tiến, lùi, trái, phải) của xe.
•	CARIMG là ảnh chiếc xe.
"""
#####################################
#KÍCH THƯỚC XE
X_MARGIN_G213 = 80
CARWIDTH_G213 = 40
CARHEIGHT_G213 = 60
CARSPEED_G213 = 3
CARIMG_22110129 = pygame.image.load('./G213NTD_GAME/img/car.png')
#LỚP XE TRONG GAME
class Car():
    def __init__(self):
        self.width = CARWIDTH_G213
        self.height = CARHEIGHT_G213
        self.x = (WINDOWWIDTH_G213NTD-self.width)/2
        self.y = (WINDOWHEIGHT_G213NTD-self.height)/2
        self.speed = CARSPEED_G213
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill((255, 255, 255))
    def draw(self):
        DISPLAYSURF.blit(CARIMG_22110129, (int(self.x), int(self.y)))
    def update(self, moveLeft, moveRight, moveUp, moveDown):
        if moveLeft == True:
            self.x -= self.speed
        if moveRight == True:
            self.x += self.speed
        if moveUp == True:
            self.y -= self.speed
        if moveDown == True:
            self.y += self.speed
        
        if self.x < X_MARGIN_G213:
            self.x = X_MARGIN_G213
        if self.x + self.width > WINDOWWIDTH_G213NTD - X_MARGIN_G213:
            self.x = WINDOWWIDTH_G213NTD - X_MARGIN_G213 - self.width
        if self.y < 0:
            self.y = 0
        if self.y + self.height > WINDOWHEIGHT_G213NTD :
            self.y = WINDOWHEIGHT_G213NTD - self.height
####################################
#PHẦN 4: XE CHƯỚNG NGẠI VẬT = XE NGƯỢC CHIỀU:obstacles ##
"""
•	LANEWIDTH là độ rộng của 1 làn xe (đường có 4 làn).
•	DISTANCE là khoảng cách giữa các xe theo chiều dọc.
•	OBSTACLESSPEED là tốc độ ban đầu của những chiếc xe.
•	CHANGESPEED dùng để tăng tốc độ của những chiếc xe theo thời gian.
•	OBSTACLESIMG là ảnh chiếc xe.
"""
#####################################
LANEWIDTH_G213 = 60
DISTANCE_G213 = 200
OBSTACLESSPEED_G213 = 2
CHANGESPEED_G213 = 0.001
OBSTACLESIMG_G213 = pygame.image.load('./G213NTD_GAME/img/obstacles.png')
class Obstacles():
    def __init__(self):
        self.width = CARWIDTH_G213
        self.height = CARHEIGHT_G213
        self.distance = DISTANCE_G213
        self.speed = OBSTACLESSPEED_G213
        self.changeSpeed = CHANGESPEED_G213
        self.ls = []
        for i in range(5):
            y = -CARHEIGHT_G213-i*self.distance
            lane = random.randint(0, 3)
            self.ls.append([lane, y])
    def draw(self):
        for i in range(5):
            x = int(X_MARGIN_G213 + self.ls[i][0]*LANEWIDTH_G213 + (LANEWIDTH_G213-self.width)/2)
            y = int(self.ls[i][1])
            DISPLAYSURF.blit(OBSTACLESIMG_G213, (x, y))
    def update(self):
        for i in range(5):
            self.ls[i][1] += self.speed
        self.speed += self.changeSpeed
        if self.ls[0][1] > WINDOWHEIGHT_G213NTD:
            self.ls.pop(0)
            y = self.ls[3][1] - self.distance
            lane = random.randint(0, 3)
            self.ls.append([lane, y])

####################################
#PHẦN 5: TÍNH ĐIỂM ##
#####################################
class Score():
    def __init__(self):
        self.score = 0
    def draw(self):
        font = pygame.font.SysFont('consolas', 30)
        scoreSuface = font.render('Score: '+str(int(self.score)), True, (0, 0, 0))
        DISPLAYSURF.blit(scoreSuface, (10, 10))
    def update(self):
        self.score += 0.02
####################################
#PHẦN 6: XỬ LÝ VA CHẠM: Collision ##
#####################################
def rectCollision_G213NTD(rect1, rect2):
    if rect1[0] <= rect2[0]+rect2[2] and rect2[0] <= rect1[0]+rect1[2] and rect1[1] <= rect2[1]+rect2[3] and rect2[1] <= rect1[1]+rect1[3]:
        return True
    return False

def isGameover_G213(car, obstacles):
    carRect = [car.x, car.y, car.width, car.height]
    for i in range(5):
        x = int(X_MARGIN_G213 + obstacles.ls[i][0]*LANEWIDTH_G213 + (LANEWIDTH_G213-obstacles.width)/2)
        y = int(obstacles.ls[i][1])
        obstaclesRect = [x, y, obstacles.width, obstacles.height]
        if rectCollision_G213NTD(carRect, obstaclesRect) == True:
            return True
    return False

####################################
#PHẦN 7: CÁC THỦ TỤC CHƠI GAME ##
"""
•	gameStart() là phần chuẩn bị khi vừa mở game lên.
•	gamePlay() là phần chơi chính.
•	gameOver() là phần xuất hiện khi thua 1 màn chơi.
"""
#####################################

def gameOver_G213NTD(bg, car, obstacles, score):
    font_G213NTD = pygame.font.SysFont('consolas', 60)
    headingSuface_G213NTD = font_G213NTD.render('GAMEOVER', True, (255, 0, 0))
    headingSize_G213NTD = headingSuface_G213NTD.get_size()

    font_G213NTD = pygame.font.SysFont('consolas', 20)
    commentSuface_G213NTD = font_G213NTD.render('Press "space" to replay', True, (0, 0, 0))
    commentSize_G213NTD = commentSuface_G213NTD.get_size()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == K_SPACE:
                    return
        bg.draw()
        car.draw()
        obstacles.draw()
        score.draw()
        DISPLAYSURF.blit(headingSuface_G213NTD, (int((WINDOWWIDTH_G213NTD - headingSize_G213NTD[0])/2), 100))
        DISPLAYSURF.blit(commentSuface_G213NTD, (int((WINDOWWIDTH_G213NTD - commentSize_G213NTD[0])/2), 400))
        pygame.display.update()
        fpsClock.tick(FPS)



def gameStart_G213NTD(bg):
    bg.__init__()
    FONT_G213 = pygame.font.SysFont('consolas', 60)
    headingSuface19g1 = FONT_G213.render('RACING', True, (255, 0, 0))
    headingSizeG1Linh = headingSuface19g1.get_size()

    FONT_G213 = pygame.font.SysFont('consolas', 20)
    commentSufaceLINHG = FONT_G213.render('Press "space" to play', True, (0, 0, 0))
    commentSize_G213NTDg1 = commentSufaceLINHG.get_size()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == K_SPACE:
                    return
        bg.draw()
        DISPLAYSURF.blit(headingSuface19g1, (int((WINDOWWIDTH_G213NTD - headingSizeG1Linh[0])/2), 100))
        DISPLAYSURF.blit(commentSufaceLINHG, (int((WINDOWWIDTH_G213NTD - commentSize_G213NTDg1[0])/2), 400))
        pygame.display.update()
        fpsClock.tick(FPS)


def gamePlay_G213NTD(bg, car, obstacles, score):
    car.__init__()
    obstacles.__init__()
    bg.__init__()
    score.__init__()
    moveLeft_G213 = False
    moveRight_G213 = False
    moveUp_G213 = False
    moveDown_G213 = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    moveLeft_G213 = True
                if event.key == K_RIGHT:
                    moveRight_G213 = True
                if event.key == K_UP:
                    moveUp_G213 = True
                if event.key == K_DOWN:
                    moveDown_G213 = True
            if event.type == KEYUP:
                if event.key == K_LEFT:
                    moveLeft_G213 = False
                if event.key == K_RIGHT:
                    moveRight_G213 = False
                if event.key == K_UP:
                    moveUp_G213 = False
                if event.key == K_DOWN:
                    moveDown_G213 = False
        if isGameover_G213(car, obstacles):
            return
        bg.draw()
        bg.update()
        car.draw()
        car.update(moveLeft_G213, moveRight_G213, moveUp_G213, moveDown_G213)
        obstacles.draw()
        obstacles.update()
        score.draw()
        score.update()
        pygame.display.update()
        fpsClock.tick(FPS)

####################################
#PHẦN 8: HÀM MAIN ##
#####################################


def main():
    bg = Background()
    car = Car()
    obstacles = Obstacles()
    score = Score()
    gameStart_G213NTD(bg)
    while True:
        gamePlay_G213NTD(bg, car, obstacles, score)
        gameOver_G213NTD(bg, car, obstacles, score)

if __name__ == '__main__':
    main()