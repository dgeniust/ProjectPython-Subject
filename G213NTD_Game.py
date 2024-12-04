# -*- coding: utf-8 -*-
import pygame, sys, random
from pygame.locals import *
####################################
#PHẦN 1: ĐỊNH NGHĨA CÁC THAM SỐ ##
#####################################
###KÍCH THƯỚC KHUNG MÀN HÌNH GAME
WINDOWWIDTH_cuaLinh = 400
WINDOWHEIGHT_LinhPhan = 600
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
BGIMG = pygame.image.load('D:\Lap Trinh Python\G213NguyenThanhDat\G213NTD_GAME\img\background.png') # hình nền

# LAYER (SURFACE) NỀN
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH_cuaLinh, WINDOWHEIGHT_LinhPhan))
pygame.display.set_caption('stt Ho Tên = Ex9.5: Game = Game ĐUA XE')

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
X_MARGIN_19Linh = 80
CARWIDTH_19Linh = 40
CARHEIGHT19_Linh = 60
CARSPEED_19Linh = 3
CARIMG_22110172 = pygame.image.load('img/car.png')
#LỚP XE TRONG GAME
class Car():
    def __init__(self):
        self.width = CARWIDTH_19Linh
        self.height = CARHEIGHT19_Linh
        self.x = (WINDOWWIDTH_cuaLinh-self.width)/2
        self.y = (WINDOWHEIGHT_LinhPhan-self.height)/2
        self.speed = CARSPEED_19Linh
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill((255, 255, 255))
    def draw_cuaLinh(self):
        DISPLAYSURF.blit(CARIMG_22110172, (int(self.x), int(self.y)))
    def update_voiLinh(self, moveLeft, moveRight, moveUp, moveDown):
        if moveLeft == True:
            self.x -= self.speed
        if moveRight == True:
            self.x += self.speed
        if moveUp == True:
            self.y -= self.speed
        if moveDown == True:
            self.y += self.speed
        
        if self.x < X_MARGIN_19Linh:
            self.x = X_MARGIN_19Linh
        if self.x + self.width > WINDOWWIDTH_cuaLinh - X_MARGIN_19Linh:
            self.x = WINDOWWIDTH_cuaLinh - X_MARGIN_19Linh - self.width
        if self.y < 0:
            self.y = 0
        if self.y + self.height > WINDOWHEIGHT_LinhPhan :
            self.y = WINDOWHEIGHT_LinhPhan - self.height
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
LANEWIDTH_LinhPhan = 60
DISTANCE_LinhPhan = 200
OBSTACLESSPEED_LinhPhan = 2
CHANGESPEED_LinhPhan = 0.001
OBSTACLESIMG_LinhPhan = pygame.image.load('img/obstacles.png')
class Obstacles():
    def __init__(self):
        self.width = CARWIDTH_19Linh
        self.height = CARHEIGHT19_Linh
        self.distance = DISTANCE_LinhPhan
        self.speed = OBSTACLESSPEED_LinhPhan
        self.changeSpeed = CHANGESPEED_LinhPhan
        self.ls = []
        for i in range(5):
            y = -CARHEIGHT19_Linh-i*self.distance
            lane = random.randint(0, 3)
            self.ls.append([lane, y])
    def draw_22110172_Linh(self):
        for i in range(5):
            x = int(X_MARGIN_19Linh + self.ls[i][0]*LANEWIDTH_LinhPhan + (LANEWIDTH_LinhPhan-self.width)/2)
            y = int(self.ls[i][1])
            DISPLAYSURF.blit(OBSTACLESIMG_LinhPhan, (x, y))
    def update_cung_Linh(self):
        for i in range(5):
            self.ls[i][1] += self.speed
        self.speed += self.changeSpeed
        if self.ls[0][1] > WINDOWHEIGHT_LinhPhan:
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
    def draw_Linh(self):
        font = pygame.font.SysFont('consolas', 30)
        scoreSuface = font.render('Score: '+str(int(self.score)), True, (0, 0, 0))
        DISPLAYSURF.blit(scoreSuface, (10, 10))
    def update_172(self):
        self.score += 0.02
####################################
#PHẦN 6: XỬ LÝ VA CHẠM: Collision ##
#####################################
def rectCollisionPTML(rect1, rect2):
    if rect1[0] <= rect2[0]+rect2[2] and rect2[0] <= rect1[0]+rect1[2] and rect1[1] <= rect2[1]+rect2[3] and rect2[1] <= rect1[1]+rect1[3]:
        return True
    return False

def isGameoverLINHPHAN(car, obstacles):
    carRect = [car.x, car.y, car.width, car.height]
    for i in range(5):
        x = int(X_MARGIN_19Linh + obstacles.ls[i][0]*LANEWIDTH_LinhPhan + (LANEWIDTH_LinhPhan-obstacles.width)/2)
        y = int(obstacles.ls[i][1])
        obstaclesRect = [x, y, obstacles.width, obstacles.height]
        if rectCollisionPTML(carRect, obstaclesRect) == True:
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

def gameOverLINH(bg, car, obstacles, score):
    font_Linh172 = pygame.font.SysFont('consolas', 60)
    headingSufacevoiLinh = font_Linh172.render('GAMEOVER', True, (255, 0, 0))
    headingSizeLINHPHAN = headingSufacevoiLinh.get_size()

    font_Linh172 = pygame.font.SysFont('consolas', 20)
    commentSufaceLINHPHAN = font_Linh172.render('Press "space" to replay', True, (0, 0, 0))
    commentSizeLINHPHAN = commentSufaceLINHPHAN.get_size()
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
        DISPLAYSURF.blit(headingSufacevoiLinh, (int((WINDOWWIDTH_cuaLinh - headingSizeLINHPHAN[0])/2), 100))
        DISPLAYSURF.blit(commentSufaceLINHPHAN, (int((WINDOWWIDTH_cuaLinh - commentSizeLINHPHAN[0])/2), 400))
        pygame.display.update()
        fpsClock.tick(FPS)



def gameStartOKLINH(bg):
    bg.__init__()
    Linhfont = pygame.font.SysFont('consolas', 60)
    headingSuface19g1 = Linhfont.render('RACING', True, (255, 0, 0))
    headingSizeG1Linh = headingSuface19g1.get_size()

    Linhfont = pygame.font.SysFont('consolas', 20)
    commentSufaceLINHG = Linhfont.render('Press "space" to play', True, (0, 0, 0))
    commentSizeLINHPHANg1 = commentSufaceLINHG.get_size()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == K_SPACE:
                    return
        bg.draw()
        DISPLAYSURF.blit(headingSuface19g1, (int((WINDOWWIDTH_cuaLinh - headingSizeG1Linh[0])/2), 100))
        DISPLAYSURF.blit(commentSufaceLINHG, (int((WINDOWWIDTH_cuaLinh - commentSizeLINHPHANg1[0])/2), 400))
        pygame.display.update()
        fpsClock.tick(FPS)


def gamePlay172(bg, car, obstacles, score):
    car.__init__()
    obstacles.__init__()
    bg.__init__()
    score.__init__()
    moveLeft19Linh = False
    moveRight19Linh = False
    moveUp172Linh = False
    moveDown19Linh = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    moveLeft19Linh = True
                if event.key == K_RIGHT:
                    moveRight19Linh = True
                if event.key == K_UP:
                    moveUp172Linh = True
                if event.key == K_DOWN:
                    moveDown19Linh = True
            if event.type == KEYUP:
                if event.key == K_LEFT:
                    moveLeft19Linh = False
                if event.key == K_RIGHT:
                    moveRight19Linh = False
                if event.key == K_UP:
                    moveUp172Linh = False
                if event.key == K_DOWN:
                    moveDown19Linh = False
        if isGameoverLINHPHAN(car, obstacles):
            return
        bg.draw()
        bg.update()
        car.draw()
        car.update(moveLeft19Linh, moveRight19Linh, moveUp172Linh, moveDown19Linh)
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
    gameStartOKLINH(bg)
    while True:
        gamePlay172(bg, car, obstacles, score)
        gameOverLINH(bg, car, obstacles, score)

if __name__ == '__main__':
    main()