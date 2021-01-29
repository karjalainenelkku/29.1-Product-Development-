import pygame  # pygame-module needs to be imported
import sys     # sys-module will be needed to exit the program
from pygame.locals import * # pygame.locals gives us the constants of pygame
pygame.init()  # this function initializes pygame, mandatory in the beginning


# the basic display-surface with suitable width and height
leveys = 1200 # 'leveys' variable contains the width of the display-surface
korkeus = 700 # 'korkeus' variable contains the height of the display-surface
# the next function will create the display-surface and stores it into 'pinta'
pinta = pygame.display.set_mode((leveys,korkeus))
# the caption of the display-window is set with the following function
pygame.display.set_caption("My game")


# the actual "building blocks" of the game, the Surface-objects
hahmo = pygame.image.load("mario.png").convert()     # image-surface
pallo = pygame.image.load("tulipallo.png").convert() # image-surface
# load()-function can load a picture which is on the same folder
# convert()-function converts it into the right pixel-format
# Surface((x,y)) creates empty surface, the default color is black
suorakaide = pygame.Surface((350,100))
# pinta, hahmo, pallo and suorakaide are all Surface-objects


# the game also needs some RGB-colors (r,g,b), where 0<r,g,b<255
musta = (0,0,0)   # black color
puna = (255,0,0)  # red color
vihr = (0,255,0)  # green color
sini = (0,0,255)  # blue color
# Surface-objects can be filled with a color using fill()-function
suorakaide.fill(puna) # paints the suorakaide-Surface with color 'puna'


# Surface-objects can be added to the display-surface with blit()-function
pinta.blit(pallo, (0,0))
pinta.blit(hahmo, (500,600))
pinta.blit(suorakaide, (0,300))
# blit(Surface,(x,y)) adds the Surface into coordinates (x,y)=(left, top)


# the display-surface needs to be updated for the Surfaces to become visible
pygame.display.flip()
# pygame.display.update() would do the same


# Rect-object holds the coordinates of a Surface-object
# Rect-objects are needed to move Surfaces and check if they overlap
# Surface.get_rect() returns the Rect-object of the Surface
palloAlue = pallo.get_rect()
hahmoAlue = hahmo.get_rect()
suoraAlue = suorakaide.get_rect()
# for example hahmoAlue = Rect(left,top,width,height) = (0,0,70,91)
# by default, get_rect() sets the left-top-corner to (0,0)
# hahmo and suorakaide were not blitted into (0,0)
# we need to cahnge the coordinates with dot-notation (left,right,top,bottom)
hahmoAlue.left = 500
hahmoAlue.top = 600
suoraAlue.left = 0
suoraAlue.top = 300


# nopeus contains the [x,y]-speed of the pallo-Surface in pixels (x,y>=1)
nopeus = [1,1]







# endless game-loop which runs until sys.exit() and/or pygame.quit()
while True:


    # check if the user has closed the display-window or pressed esc
    for tapahtuma in pygame.event.get():  # all the events in the event queue
        if tapahtuma.type == pygame.QUIT: # if the player closed the window
            pygame.quit() # the display-window closes
            sys.exit()    # the whole python program exits
        if tapahtuma.type == KEYDOWN:     # if the player pressed down any key
            if tapahtuma.key == K_ESCAPE: # if the key was esc
                pygame.quit() # the display-window closes
                sys.exit()    # the whole python program exits



    # pallo-Surface will be moved by nopeus=[1,1] in every iteration
    palloAlue.move_ip(nopeus)
    # move_ip([x,y]) changes the Rect-objects coordinates by x and y
    # move([x,y]) doesn't change the Rect-object, it creates new one:
    # palloAlue = palloAlue.move(nopeus)



    # pallo-Surface bounces from the edges of the display-surface
    if palloAlue.left < 0 or palloAlue.right > leveys:
    # if pallo is vertically outside
        nopeus[0] = -nopeus[0]
        # the x-direction of the speed will be changed with minus
    if palloAlue.top < 0 or palloAlue.bottom > korkeus:
    # if pallo is horizontally outside
        nopeus[1] = -nopeus[1]
        # the y-direction of the speed will be changed with minus



    # pallo-Surface bounces from the suorakaide-Surface
    if suoraAlue.colliderect(palloAlue):
    # colliderect()-function returns True if two Rect-objects overlap
        if suoraAlue.colliderect(palloAlue.move(-nopeus[0],0)):
        # if the pallo came from vertical direction
            nopeus[1] = -nopeus[1]
            # the y-direction of the speed will be changed with minus
        if suoraAlue.colliderect(palloAlue.move(0,nopeus[1])):
        # if the pallo came from horizontal direction
            nopeus[0] = -nopeus[0]
            # the x-direction of the speed will be changed with minus



    # you can move hahmo-Surface with left,right,up,down-keys
    painallukset = pygame.key.get_pressed()
    # get.pressed()-function gives a list of all the keys that are being pressed
    if painallukset[K_LEFT]:       # if left-key is in this list
        hahmoAlue.move_ip((-1,0))  # hahmo will be moved one pixel left
    if painallukset[K_RIGHT]:
        hahmoAlue.move_ip((1,0))
    if painallukset[K_DOWN]:
        hahmoAlue.move_ip((0,1))
    if painallukset[K_UP]:
        hahmoAlue.move_ip((0,-1))
    # from pygame-documentation you can find all the names for the keys







    # clear the display-surface and draw all the Surfaces again
    pinta.fill(musta) # without this, moving characters would have a "trace"
    pinta.blit(pallo, palloAlue)
    pinta.blit(hahmo, hahmoAlue)
    pinta.blit(suorakaide, suoraAlue)


    # this is always needed to the end to update the display surface
    pygame.display.flip()



