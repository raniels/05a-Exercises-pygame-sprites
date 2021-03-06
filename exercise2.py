#!/usr/bin/env python
'''

For this exercise, draw a random number of randomly-sized sprites with a random color, random initial position, and random direction

'''
import sys, logging, pygame, random
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4' 

logging.basicConfig(level=logging.CRITICAL)
logger = logging.getLogger(__name__)

screen_size = (800,600)
FPS = 60
red = (255,0,0)
black = (0,0,0)

class Block(pygame.sprite.Sprite):
    def __init__(self, color, size, position, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        (self.rect.x,self.rect.y) = position
        self.direction = direction

    def update(self):
        (dx,dy) = self.direction
        self.rect.x += dx
        self.rect.y += dy
        (WIDTH,HEIGHT) = screen_size
        if self.rect.left > WIDTH:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = WIDTH
        if self.rect.top > HEIGHT:
            self.rect.bottom = 0
        if self.rect.bottom < 0:
            self.rect.top = HEIGHT


def main():
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()

    blocks = pygame.sprite.Group()
    BlockAmount = random.randrange(25)
    while BlockAmount > 0:
        Color = (random.randrange(255), random.randrange(255), random.randrange(255))
        Size = (random.randrange(100), random.randrange(100))
        Position = (random.randrange(800), random.randrange(600))
        Direction = (random.randrange(25), random.randrange(25))
        block = Block(Color, Size, Position, Direction)
        blocks.add(block)
        BlockAmount -= 1

    while True:
        clock.tick(FPS)
        screen.fill(black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        blocks.update()
        blocks.draw(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()