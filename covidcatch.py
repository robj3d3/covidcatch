import os, sys # allows for creation of platform independent file paths
import pygame
from pygame.locals import *

if not pygame.font:
    print("Warning: fonts disabled")

if not pygame.mixer:
    print("Warning: sounds disabled")



pygame.init()
