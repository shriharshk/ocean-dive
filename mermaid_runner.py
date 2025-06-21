import pygame
import random

# Game settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Player constants
PLAYER_SPEED = 5
ASCEND_SPEED = -10
DIVE_SPEED = 10

# Obstacle settings
OBSTACLE_SPEED = 5
OBSTACLE_FREQ = 1500  # milliseconds

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 30))
        self.image.fill((0, 255, 255))  # Placeholder color for mermaid
        self.rect = self.image.get_rect()
        self.rect.center = (100, SCREEN_HEIGHT // 2)
        self.velocity_y = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.velocity_y = ASCEND_SPEED
        elif keys[pygame.K_DOWN]:
            self.velocity_y = DIVE_SPEED
        else:
            self.velocity_y = 0
        self.rect.y += self.velocity_y
        self.rect.y = max(0, min(SCREEN_HEIGHT - self.rect.height, self.rect.y))

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = random.randint(50, SCREEN_HEIGHT - 50)

    def update(self):
        self.rect.x -= OBSTACLE_SPEED
        if self.rect.right < 0:
            self.kill()

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Mermaid Runner')
        self.clock = pygame.time.Clock()
        self.running = True

        # Load music from the Dusty Chip I Music Library (placeholder path)
        # Place one of the asset's OGG files in the project directory
        # and replace 'dusty_title.ogg' with the actual filename.
        try:
            pygame.mixer.music.load('dusty_title.ogg')
            pygame.mixer.music.play(-1)
        except pygame.error:
            print('Background music file not found.')

        self.player = Player()
        self.all_sprites = pygame.sprite.Group(self.player)
        self.obstacles = pygame.sprite.Group()

        pygame.time.set_timer(pygame.USEREVENT + 1, OBSTACLE_FREQ)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.USEREVENT + 1:
                    self.spawn_obstacle()

            self.all_sprites.update()
            self.obstacles.update()

            if pygame.sprite.spritecollideany(self.player, self.obstacles):
                print('Game Over!')
                self.running = False

            self.screen.fill((0, 0, 128))
            self.all_sprites.draw(self.screen)
            self.obstacles.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(FPS)

    def spawn_obstacle(self):
        obstacle = Obstacle(SCREEN_WIDTH + 20)
        self.obstacles.add(obstacle)
        self.all_sprites.add(obstacle)

if __name__ == '__main__':
    Game().run()
