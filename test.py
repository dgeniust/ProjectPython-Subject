import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Thiết lập kích thước màn hình và màu sắc
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Đua Xe")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Tốc độ di chuyển và tốc độ chướng ngại vật
car_speed = 5
obstacle_speed = 5

# Tải hình ảnh xe và chướng ngại vật
car_image = pygame.image.load('./G213NTD_GAME/img/car.png')  # Thay đổi đường dẫn hình ảnh xe
car_rect = car_image.get_rect()
car_rect.centerx = screen_width // 2
car_rect.bottom = screen_height - 10

# Khởi tạo font chữ
font = pygame.font.SysFont('Arial', 30)

# Hàm hiển thị điểm số
def show_score(score):
    score_text = font.render("Điểm: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

# Hàm tạo chướng ngại vật
def create_obstacle():
    width = random.randint(50, 150)
    height = random.randint(20, 40)
    x = random.randint(0, screen_width - width)
    y = -height
    return pygame.Rect(x, y, width, height)

# Hàm chính của game
def game_loop():
    run_game = True
    clock = pygame.time.Clock()
    score = 0
    obstacles = []

    while run_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False

        # Điều khiển xe
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and car_rect.left > 0:
            car_rect.x -= car_speed
        if keys[pygame.K_RIGHT] and car_rect.right < screen_width:
            car_rect.x += car_speed

        # Tạo và di chuyển chướng ngại vật
        if random.randint(1, 20) == 1:
            obstacles.append(create_obstacle())

        for obstacle in obstacles:
            obstacle.y += obstacle_speed
            if obstacle.colliderect(car_rect):
                run_game = False  # Xe va chạm với chướng ngại vật, kết thúc game

            if obstacle.top > screen_height:
                obstacles.remove(obstacle)
                score += 1  # Người chơi vượt qua chướng ngại vật

        # Vẽ lại màn hình
        screen.fill(BLACK)
        screen.blit(car_image, car_rect)
        
        # Vẽ chướng ngại vật
        for obstacle in obstacles:
            pygame.draw.rect(screen, RED, obstacle)

        # Hiển thị điểm số
        show_score(score)

        # Cập nhật màn hình
        pygame.display.update()

        # Cập nhật FPS
        clock.tick(60)

    pygame.quit()

# Chạy game
game_loop()
