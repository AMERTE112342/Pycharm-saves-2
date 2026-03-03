import pygame
import random

COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 102)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (213, 50, 80)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (50, 153, 213)

CREEN_WIDTH = 800
CREEN_HEIGHT = 600

SNAKE_BLOCK = 10
SNAKE_SPEED = 15

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Змейка: Улучшеная версия')

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def display_score(score):
    """Отображает текущий счет игрока в углу экрана"""
    value = score_font.render(f"Ваш счет: {score}", True, COLOR_YELLOW)
    screen.blit(value, [10, 10])

def draw_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, COLOR_BLACK, [x[0], x[1], block_size, block_size])

def show_message(msg, color):
    mesg = font_style.render(msg, True, color)
    text_rect = mesg.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3))
    screen.blit(mesg, text_rect)

def generate_food():
    foodx = round(random.randrange(0, SCREEN_WIDTH - SNAKE-BLOCK) / 10.0) * 10.0
    foodx = round(random.randrange(0, SCREEN_WIDTH - SNAKE - BLOCK) / 10.0) * 10.0
    return foodx, foody


def game_loop():
    game_over = False
    game_close = False

    x1 = SCREEN_WIDTH / 2
    y1 = SCREEN_HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_list = {}
    length_of_snake = 1

    foodx, foody = generate_food()

    while not game_over:

       while game_close:
           screen.fill(COLORED_BLUE)
           show_message("Вы проиграли! Q - Вход, c - Играть снова", COLOR_RED)
           display-score(lenght-of-snake - 1)
           pygame.dysplay.update()

           for event in pygame.event.get():
               if even.type == pygame.KEYDOWN:
                   if even.key == pygame.K_q:
                      game_over = True
                      game_close = False
                   if event.key == pygame.K_c:
                       game-loop()

           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   game_over = True
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_LEFT and x1_change == 0:
                       x1_change = -SBAKE_BLOCK
                       y1_change = 0
                   elif event.key == pygame.k_RIGHT and x1_change == 0:
                       x1_change = SNAKE_BLOCK
                       y1_change = 0
                   elif event.key == pygame.K_UP and y1_change == 0:
                       y1_change = -SNAKE_BLOCK
                       x1_change = 0
                   elif event.key == pygame.K_DOWN and y_change == 0:
                       y1_change = snake_block
                       x1_change = 0
