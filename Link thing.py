import pygame
pygame.init()
pygame.display.set_caption("sprite sheet") #sets the window title
screen = pygame.display.set_mode((800, 800))  #creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #sets up clock
gameover = False #variable to run game loop

#player variables
LEFT=0
RIGHT=1
UP = 2
DOWN = 3

Link = pygame.image.load('C:/Users/768588/Downloads/pixil-frame-0 (4).png') #load your spritesheet
Link.set_colorkey((255, 0, 255)) #this makes bright pink (255, 0, 255) transparent (sort of)


xpos = 500 #xpos of player
ypos = 200 #ypos of player
vx = 0 #x velocity of player
vy = 0
keys = [False, False, False, False] #this list holds whether each key has been pressed


#animation variables variables
frameWidth = 64
frameHeight = 64
RowNum = 0 #for left animation, this will need to change for other animations
frameNum = 0
ticker = 0


while not gameover:
    clock.tick(60) #FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[0] = True

            if event.key == pygame.K_RIGHT:
                keys[1] = True

            if event.key == pygame.K_UP:
                keys[2] = True

            if event.key == pygame.K_DOWN:
                keys[3] = True


        if event.type == pygame.KEYUP: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[0] = False

            if event.key == pygame.K_RIGHT:
                keys[1] = False

            if event.key == pygame.K_UP:
                keys[2] = False

            if event.key == pygame.K_DOWN:
                keys[3] = False


    #LEFT MOVEMENT
    if keys[0]==True:
        vx=-3
        direction = 0
    #RIGHT MOVEMENT
    elif keys[1] == True:
        vx = 3
        direction = 1
    #turn off velocity
    else:
        vx = 0   

    if keys[2] == True:
        vy = -3
        direction = 2
    elif keys[3] == True:
        vy =3
        direction = 3
    else:
        vy = 0


    print(keys)   

    #UPDATE POSITION BASED ON VELOCITY
    xpos+=vx
    ypos+=vy
    #ANIMATIOn---------------------------------------------------------------------------
    # only animate when in motion
    if vx < 0: #left animation
        RowNum = 1
    # ticker is a spedometer. We don't want Link animating as fast as the processor can process! Update Animation frame each time ticker goes over
        ticker+=1
        if ticker%5==0:
            frameNum+=1
            #if we are over the number of frames in our sprite, reset to 0.
        if frameNum>3:
            frameNum = 0
    if vx > 0:
        RowNum = 2
        ticker+=1
        if ticker%5==0:
            frameNum+=1
            #if we are over the number of frames in our sprite, reset to 0.
        if frameNum>3:
            frameNum = 0
    if vy < 0:
        RowNum = 3
        ticker+=1
        if ticker%5==0:
            frameNum+=1
            #if we are over the number of frames in our sprite, reset to 0.
        if frameNum>3:
            frameNum = 0
    if vy> 0:
        RowNum = 0
        ticker+=1
        if ticker%5==0:
            frameNum+=1
            #if we are over the number of frames in our sprite, reset to 0.
        if frameNum>3:
            frameNum = 0

    #RENDER---------------------------------------------------------------------------------------
    # once we've figured out what frame we're on and where we are, time to render.

    screen.fill((0,0,0)) #wipe screen so it doesn't smear
    screen.blit(Link, (xpos, ypos), (frameWidth*frameNum, RowNum*frameHeight, frameWidth, frameHeight))
    pygame.display.flip() #this actually puts the pixel on the screen

#end game loop
pygame.quit
