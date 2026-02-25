import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 30)

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)


# Player
player = pygame.Rect(370, 520, 60, 40)
player_speed = 6

# Bullets
bullets = []
bullet_speed = 8

# Enemies
enemies = []
enemy_speed = 3

score = 0
game_over = False

run = True
while run:
    clock.tick(60)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                bullet = pygame.Rect(player.x + 25, player.y, 10, 20)
                bullets.append(bullet)

            if event.key == pygame.K_r and game_over:
                bullets.clear()
                enemies.clear()
                score = 0
                game_over = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.x -= player_speed
    if keys[pygame.K_d]:
        player.x += player_speed

    if not game_over:
        # Spawn enemies
        if random.randint(1, 40) == 1:
            enemy = pygame.Rect(random.randint(0, WIDTH-40), 0, 40, 40)
            enemies.append(enemy)

        # Move bullets
        for bullet in bullets[:]:
            bullet.y -= bullet_speed
            if bullet.y < 0:
                bullets.remove(bullet)

        # Move enemies
        for enemy in enemies[:]:
            enemy.y += enemy_speed
            if enemy.y > HEIGHT:
                game_over = True
            # Collision
            for bullet in bullets[:]:
                if enemy.colliderect(bullet):
                    enemies.remove(enemy)
                    bullets.remove(bullet)
                    score += 1
                    break

    # Draw
    pygame.draw.rect(screen, WHITE, player)
    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet)
    for enemy in enemies:
        pygame.draw.rect(screen, WHITE, enemy)

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10,10))

    if game_over:
        over_text = font.render("GAME OVER - Press R to Restart", True, WHITE)
        screen.blit(over_text, (200,300))

    pygame.display.update()

pygame.quit()