import pygame
import random
import math

# initialize pygame first
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.jpg')

# Title And Icon
pygame.display.set_caption("ALIEN KILLER")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
player_img = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# Enemy
enemy_img = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemy_img.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.3)
    enemyY_change.append(0.3)

# Bullet
# Ready - Pause
# Fire - Bullet moving
bullet_img = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 2
bullet_state = 'ready'

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10


def show_score(x, y):
    score = font.render('Score : '+str(score_value), True, (255, 0, 0))
    screen.blit(score, (x, y))


'''def game_info(x, y):
    info = font.render('You can play this game till your battery dies', True, (255, 200,100))
    screen.blit(info, (250, y))'''


def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bullet_img, (x+16, y+10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(abs(enemyX-bulletX), 2) + math.pow(abs(enemyY-bulletY), 2))
    if distance < 25:
        return True
    else:
        return False



'''def collisionBetweenEnemyAndPlayer(playerX, playerY, enemyX, enemyY):
    dist = math.sqrt(math.pow(abs(playerX-enemyX), 2) + math.pow(abs(playerY-enemyY), 2))
    if dist < 5:
        return  True
    else:
        return False'''

# GAME LOOP
running = True
while running:
    # RGB
    screen.fill((0, 51, 102))
    # Background
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left or top or bottom
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.6
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.6
            if event.key == pygame.K_UP:
                playerY_change = -0.6
            if event.key == pygame.K_DOWN:
                playerY_change = 0.6
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bulletX = playerX
                    bulletY = playerY
                    fire_bullet(bulletX, playerY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                playerY_change = 0

    # drawn after screen
    playerX += playerX_change
    playerY += playerY_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 735:
        playerX = 735
    if playerY <= 450:
        playerY = 450
    elif playerY >= 535:
        playerY = 535

    # Enemy Movement
    for i in range(num_of_enemies):
        """enemyX[i] += enemyX_change[i]
        enemyY[i] += enemyY_change[i]"""

        if enemyX[i] <= 0:
            enemyX_change[i] = 0.6
        elif enemyX[i] >= 735:
            enemyX_change[i] = -0.6
        if enemyY[i] <= 0:
            enemyY_change[i] = 0.6
        elif enemyY[i] >= 400:
            enemyY_change[i] = -0.6

        enemyX[i] += enemyX_change[i]
        enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = playerY
            bulletX = playerX
            bullet_state = 'ready'
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
            score_value += 1
        enemy(enemyX[i], enemyY[i], i)

        # Collision between enemy and player
        '''coll = collisionBetweenEnemyAndPlayer(playerX, playerY, enemyX[i], enemyY[i])
        if coll:
            score_value -= 1'''

    # Bullet movement
    if bulletY <= 0:
        bulletY = playerY
        bullet_state = 'ready'

    if bullet_state is 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)    # Score Display
    # game_info(textX, textY)
    pygame.display.update()

print(f"YOUR SCORE IS --> {score_value}")
print("CONGRATS!!!")
print()
print("To play again press --> shift+f10")