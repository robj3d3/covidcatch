# Imports
import os, sys # allows for creation of platform independent file paths
import pygame
from pygame.locals import *

# Check if fonts and sounds are enabled
if not pygame.font:
    print("Warning: fonts disabled")

if not pygame.mixer:
    print("Warning: sounds disabled")


# General methods
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join('data', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error as message:
        print('Cannot load sound:', wav)
        raise SystemExit(message)
    return sound


# Classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image, self.rect = load_image("img/hands-open.png", -1)


pygame.init()
screen = pygame.display.set_mode((468, 60))
pygame.display.set_caption("COVIDcatch")
pygame.mouse.set_visible(0)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

screen.blit(background, (0, 0))
pygame.display.flip()

clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
