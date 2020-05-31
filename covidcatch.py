import pygame
import time
import random

pygame.init()

# R,G,B - SomeColors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 40, 40)
green = (17, 124, 47)
blue = (0, 0, 255)
grey = (180, 180, 180)

#LoadingImages
bgImg = pygame.image.load("images/bgCovid.png")
selectText = pygame.image.load("images/choose-your-player.png")
startImg = pygame.image.load("images/starticon.png")
quitImg = pygame.image.load("images/quiticon.png")
titleImg = pygame.image.load("images/titleicon.png")
clickStartImg = pygame.image.load("images/clickedStartIcon.png")
clickQuitImg = pygame.image.load("images/clickedQuitIcon.png")

openhandsPng = pygame.image.load("images/openhands.png")
openhandsPng = pygame.transform.scale(openhandsPng, (100, 100))
facePng = pygame.image.load("images/face.png")
facePng = pygame.transform.scale(facePng, (100, 100))

sanitizerImg = pygame.image.load("images/sanitizer.png")
sanitizerImg = pygame.transform.scale(sanitizerImg, (38, 50))
glovesImg = pygame.image.load("images/gloves.png")
glovesImg = pygame.transform.scale(glovesImg, (38, 45))
maskImg = pygame.image.load("images/mask.png")
maskImg = pygame.transform.scale(maskImg, (50, 35))
distanceBoardImg = pygame.image.load("images/distanceBoard.png")
distanceBoardImg = pygame.transform.scale(distanceBoardImg, (1000, 100))
wall1Img = pygame.image.load("images/wall1.png")
wall2Img = pygame.image.load("images/wall2.png")
bgImg = pygame.transform.scale(bgImg, (1000, 800))


virusImg = pygame.image.load("images/icon.png")
virusImg = pygame.transform.scale(virusImg, (45, 45))
virusDistanceImg = pygame.image.load("images/virusDistance.png")
virusDistanceImg = pygame.transform.scale(virusDistanceImg, (40, 40))

pygame.mixer.music.load('coughing.mp3')

#SettingFrame
display_width = 1000
display_height = 800
gameDisplay = pygame.display.set_mode((display_width, display_height))
icon = pygame.display.set_icon(pygame.image.load('images/icon.png'))
pygame.display.set_caption("COVIDcatch")

#SettingClock
clock = pygame.time.Clock()

#ScoresArray
scores = []

#PlayerClassParameters
playerparms = []
# dog1parms = [openhandsPng, 5, 377, 450, 36, 30, 1.1]
# dog2parms = [facePng,3.5,380,510,30,25, 1.02]

handsparms = [openhandsPng, 5, 712, 712, 36, 30, 1.01] #increase to 1.1 last number to speed up virus faster
faceparms = [facePng,5,712,712,30,50, 1.01]
# p_img,speedIn,player_x,player_y,hitbox_x,hitbox_y,speedmultiplier

#ButtonClass
class Button:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            gameDisplay.blit(img_act,(x_act, y_act))
            if click[0] and action != None:
                time.sleep(2)
                action()
        else:
            gameDisplay.blit(img_in,(x,y))
#ButtonsForCharacterSelection
class Button2:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, parms, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            gameDisplay.blit(img_act, (x_act, y_act))
            if click[0] and action != None:
                playerparms.append(parms[0])
                playerparms.append(parms[1])
                playerparms.append(parms[2])
                playerparms.append(parms[3])
                playerparms.append(parms[4])
                playerparms.append(parms[5])
                playerparms.append(parms[6])
                time.sleep(2)
                action()
        else:
            gameDisplay.blit(img_in, (x, y))

# BackgroundClass
class Background:
    def __init__(self, bg_img, bg_x, bg_y):
        self.bg_x = bg_x
        self.bg_y = bg_y
        gameDisplay.blit(bg_img, (bg_x, bg_y))
        
        distanceBoard = Gameobject(distanceBoardImg, 0, 0, 725, 0, 0)
        gameDisplay.blit(distanceBoard.b_image, (distanceBoard.coord_x, distanceBoard.coord_y))

# PlayerClass
class Player:
    def __init__(self,p_img,speedIn,player_x,player_y,hitbox_x,hitbox_y,speedmultiplier):
        self.speed = speedIn
        self.player_x = player_x
        self.player_y = player_y
        self.p_img = p_img
        self.hitbox_x = 100
        self.hitbox_y = 100
        self.speedmult = speedmultiplier
        self.range = 90


# GameObjectsClass
class Gameobject:
    def __init__(self, b_image, speed, coord_x, coord_y, hitbox_x, hitbox_y):
        self.b_image = b_image
        self.speed = speed
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.hitbox_x = hitbox_x
        self.hitbox_y = hitbox_y

# ScoreFunction
def scorecounter(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score:" + str(count), True, white)
    gameDisplay.blit(text, (0, 0))

# CrashFunction/MessageDisplay
def text_objects(text, font):
    textsurface = font.render(text, True, red)
    return textsurface, textsurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf", 30)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    # game_loop() # NEED TO CHANGE THIS IF WE DON'T WANT IT TO RESTART EACH TIME
    runGame()


def crash(message, score): # Called at end of game
    scores.append(score)
    scores.sort(reverse = True)
    message_display(message)

#QuitFunction
def quitgame():
    pygame.quit()
    quit()

#MainMenu
def mainmenu():

    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)

        titletext = gameDisplay.blit(titleImg, (375,200))
        startButton = Button(startImg,380,260,60,20,clickStartImg,373,258,selectScreen)
        quitButton = Button(quitImg,575,260,60,20,clickQuitImg,570,258,quitgame)

        # Prints out all "high" scores to main menu
        TextSurf = pygame.font.Font("freesansbold.ttf", 30).render("High scores:", True, black)
        TextRect = TextSurf.get_rect()
        TextRect.center = ((display_width / 2), (display_height / 3)*2-60)
        gameDisplay.blit(TextSurf, TextRect)

        for i in range(len(scores)):
            TextSurf = pygame.font.Font("freesansbold.ttf", 30).render(str(scores[i]), True, black)
            TextRect = TextSurf.get_rect()
            TextRect.center = ((display_width / 2), (display_height / 3)*2+(30*i+1))
            gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(15)

#CharacterSelect
def selectScreen():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        gameDisplay.blit(selectText,(350,150))

        # dogSelect = Button2(dogImg, 280,260,40,150,clickedDogImg,278,226,dog1parms,game_loop)
        # dog2select = Button2(dog2Img,480,260,40,100, clickedDog2Img,479,239,dog2parms,game_loop)
        openhandsSelect = Button2(openhandsPng, 380, 360, 200, 200, openhandsPng, 378, 326, handsparms, game_loop)
        faceSelect = Button2(facePng, 589, 360, 200, 200, facePng, 579, 339, faceparms, game_loop)

        pygame.display.update()
        clock.tick(15)

#MainGame
def game_loop():
#CreatingObjects
# b_image, speed, coord_x, coord_y, hitbox_x, hitbox_y

    wall1 = Gameobject(wall1Img, 3, 910, 250, 0, 0)
    wall2 = Gameobject(wall2Img, 3, -20, 250, 0, 0)
    player = Player(playerparms[0],playerparms[1],playerparms[2],playerparms[3],playerparms[4],playerparms[5],playerparms[6])

    gloves = Gameobject(glovesImg, 5, random.randrange(0 + player.range, display_width - 20 - player.range),-600,40,35)
    sanitizer = Gameobject(sanitizerImg, 5, random.randrange(0 + player.range, display_width - 20 - player.range), -600, 40, 35)
    mask = Gameobject(maskImg, 5, random.randrange(0 + player.range, display_width - 20 - player.range), -600, 40, 35)

    virus = Gameobject(virusImg, 3, random.randrange(0 + player.range, display_width - 20 - player.range),-600,40,35)
    virusDistance = Gameobject(virusDistanceImg, 4, random.randrange(0 + player.range, display_width - 20 - player.range),random.randrange(-2000, -1000),40,35)
#Constants
    x_change = 0
    score = 0
    covidCounter = 0
    display_covid_text = False

    gameexit = False
#GameLoop
    while not gameexit:

#Background
        if covidCounter > 6:
            # pygame.mixer.music.load('coughing.mp3')
            # pygame.mixer.music.play(-1)
            time.sleep(3)
            # pygame.mixer.music.stop()
            crash("Oh no! You caught COVID-19!", score)
        
        gameDisplay.fill(white)
        bg = Background(bgImg, 0, 0)
# Objects
        gameDisplay.blit(gloves.b_image, (gloves.coord_x, gloves.coord_y))
        gameDisplay.blit(sanitizer.b_image, (sanitizer.coord_x, sanitizer.coord_y))
        gameDisplay.blit(mask.b_image, (mask.coord_x, mask.coord_y))

        gameDisplay.blit(virus.b_image, (virus.coord_x, virus.coord_y))
        gameDisplay.blit(virusDistance.b_image, (virusDistance.coord_x, virusDistance.coord_y))
        gameDisplay.blit(wall1.b_image, (wall1.coord_x, wall1.coord_y))
        gameDisplay.blit(wall2.b_image, (wall2.coord_x, wall2.coord_y))

#Player
        gameDisplay.blit(player.p_img, (player.player_x,player.player_y))

#Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and player.player_x > 0:
                    x_change = player.speed*-1 + -1*player.speedmult*score
                elif event.key == pygame.K_RIGHT and player.player_x < display_width - 45:
                    x_change = player.speed + player.speedmult*score
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        player.player_x += x_change

        # print(event)

# ObjectSpeeds
        gloves.coord_y += gloves.speed
        sanitizer.coord_y += sanitizer.speed
        mask.coord_y += mask.speed

        virus.coord_y += virus.speed + 1.2 * score
        virusDistance.coord_y += virusDistance.speed
        
        # if score >= 1:
        # vac_y += 10

# Boundaries
        if player.player_x > (display_width - 100 - player.range):
            x_change = 0
        if player.player_x < (0 + player.range):
            x_change = 0

# RecallingObjects
        if gloves.coord_y > display_height:
            gloves.coord_y = -10
            gloves.coord_x = random.randrange(0 + player.range, display_width - 25 - player.range)
        if sanitizer.coord_y > display_height:
            sanitizer.coord_y = -10
            sanitizer.coord_x = random.randrange(0 + player.range, display_width - 25 - player.range)
        if mask.coord_y > display_height:
            mask.coord_y = -10
            mask.coord_x = random.randrange(0 + player.range, display_width - 25 - player.range)

        if virus.coord_y > display_height - 10:
            virus.coord_y = -10
            virus.coord_x = random.randrange(0 + player.range, display_width - 25 - player.range)
        if virusDistance.coord_y > display_height:
            virusDistance.coord_y = -2000
            virusDistance.coord_x = random.randrange(0 + player.range, display_width - 56 - player.range)
# Score
        scorecounter(score)

# Collisons
    # Virus - BAD
        if player.player_y <= virus.coord_y + virus.hitbox_y and player.player_y >= virus.coord_y or player.player_y + player.hitbox_y >= virus.coord_y and player.player_y + player.hitbox_y <= virus.coord_y + virus.hitbox_y:
            if player.player_x >= virus.coord_x and player.player_x <= virus.coord_x + virus.hitbox_x or player.player_x + player.hitbox_x >= virus.coord_x and player.player_x + player.hitbox_x <= virus.coord_x + virus.hitbox_x or player.player_x <= virus.coord_x and player.player_x + player.hitbox_x >= virus.coord_x + virus.hitbox_x:
                    # crash("Oh no! You caught COVID-19")
                    player.range += 50
                    virus.coord_y = -10
                    virus.coord_x = random.randrange(0 + player.range, display_width - 25 - player.range)
                    wall2.coord_x += 50 # Move walls in
                    wall1.coord_x -= 50
                    covidCounter += 1

                    # Display bad catch alert text
                    if covidCounter <= 6:

                        TextSurf, TextRect = text_objects("Eeeek you caught a virus!", pygame.font.Font("freesansbold.ttf", 30))
                        TextRect.center = ((display_width / 2), (display_height / 2))
                        gameDisplay.blit(TextSurf, TextRect)

                        pygame.display.flip()
                        # while pygame.mixer.music.get_busy():
                        #     time.sleep(0.1)
                        time.sleep(3)

                    player.player_x = 350 # Reset hand position to mid
    # Virus Distance - BAD
        if player.player_y <= virusDistance.coord_y + virusDistance.hitbox_y:
            if player.player_x >= virusDistance.coord_x and player.player_x <= virusDistance.coord_x + virusDistance.hitbox_x or player.player_x + player.hitbox_x >= virusDistance.coord_x and player.player_x + player.hitbox_x <= virusDistance.coord_x + virusDistance.hitbox_x or player.player_x <= virusDistance.coord_x and player.player_x + player.hitbox_x >= virusDistance.coord_x + virusDistance.hitbox_x:
                # crash("Oh no! You weren't socially distanced")
                player.range += 50
                virusDistance.coord_y = -10
                virusDistance.coord_x = random.randrange(0 + player.range, display_width - 25 - player.range)
                wall2.coord_x += 50 # Move walls in
                wall1.coord_x -= 50
                covidCounter += 1

                # Display bad catch alert text
                if covidCounter <= 6:


                    TextSurf, TextRect = text_objects("Eeeek you caught a virus!", pygame.font.Font("freesansbold.ttf", 30))
                    TextRect.center = ((display_width / 2), (display_height / 2))
                    gameDisplay.blit(TextSurf, TextRect)


                    pygame.display.flip()
                    nr = 0
                    # while pygame.mixer.music.get_busy():
                    #     nr += 1
                    #     if nr > 3:
                    #         break
                    time.sleep(3)

                player.player_x = 350 # Reset hand position to mid

    # Gloves - GOOD
        if player.player_y <= gloves.coord_y + gloves.hitbox_y and player.player_y >= gloves.coord_y or player.player_y + player.hitbox_y >= gloves.coord_y and player.player_y + player.hitbox_y <= gloves.coord_y + gloves.hitbox_y:
            if player.player_x >= gloves.coord_x and player.player_x <= gloves.coord_x + gloves.hitbox_x or player.player_x + player.hitbox_x >= gloves.coord_x and player.player_x + player.hitbox_x <= gloves.coord_x + gloves.hitbox_x or player.player_x <= gloves.coord_x and player.player_x + player.hitbox_x >= gloves.coord_x + gloves.hitbox_x:
                    gloves.coord_y = -10
                    gloves.coord_x = random.randrange(0 + player.range, display_width - 25 - player.range)
                    score += 1
                    print(score)
    # Sanitizer - GOOD
        if player.player_y <= sanitizer.coord_y + sanitizer.hitbox_y and player.player_y >= sanitizer.coord_y or player.player_y + player.hitbox_y >= sanitizer.coord_y and player.player_y + player.hitbox_y <= sanitizer.coord_y + sanitizer.hitbox_y:
            if player.player_x >= sanitizer.coord_x and player.player_x < sanitizer.coord_x + sanitizer.hitbox_x or player.player_x + player.hitbox_x >= sanitizer.coord_x and player.player_x + player.hitbox_x <= sanitizer.coord_x + sanitizer.hitbox_x or player.player_x <= sanitizer.coord_x and player.player_x + player.hitbox_x >= sanitizer.coord_x + sanitizer.hitbox_x:
                    sanitizer.coord_y = -10
                    sanitizer.coord_x = random.randrange(0 + player.range, display_width - 25 - player.range)
                    score += 1
                    print(score)
    # Mask - GOOD
        if player.player_y <= mask.coord_y + mask.hitbox_y and player.player_y >= mask.coord_y or player.player_y + player.hitbox_y >= mask.coord_y and player.player_y + player.hitbox_y <= mask.coord_y + mask.hitbox_y:
            if player.player_x >= mask.coord_x and player.player_x <= mask.coord_x + mask.hitbox_x or player.player_x + player.hitbox_x >= mask.coord_x and player.player_x + player.hitbox_x <= mask.coord_x + mask.hitbox_x or player.player_x <= mask.coord_x and player.player_x + player.hitbox_x >= mask.coord_x + mask.hitbox_x:
                    mask.coord_y = -10
                    mask.coord_x = random.randrange(0 + player.range, display_width - 25 - player.range)
                    score += 1
                    print(score)

        pygame.display.update()
        clock.tick(60)

def runGame():
    mainmenu()
    selectScreen()
    game_loop()
    pygame.QUIT()
    quit()

runGame()