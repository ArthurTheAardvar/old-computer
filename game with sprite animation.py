import pygame
pygame.init()  
pygame.display.set_caption('adding images')  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loo
Link = pygame.image.load('C:/Users/768588/Downloads/pixil-frame-0 (4).png') #load your spritesheet
Link.set_colorkey((255, 0, 255))

#CONSTANTS
LEFT=0
RIGHT=1
UP = 2
DOWN = 3

backround = pygame.image.load("C:/Users/768588/Downloads/bcs_609_gl_1005_0864-rt_sq-b46e2366ee97c73cbbcffa4f3c105321cb2ca2da-s800-c85.jpg")

#player variables
xpos = 500 #xpos of player
ypos = 300 #ypos of player
vx = 0 #x velocity of player
vy = 0 #y velocity of player
keys = [False, False, False, False] #this list holds whether each key has been pressed
isOnGround = False #this variable stops gravity from pulling you down more when on a platform
health = 100

frameWidth = 64
frameHeight = 64
RowNum = 0 #for left animation, this will need to change for other animations
frameNum = 0
ticker = 0

def add_character_at_location(x,y):
    game_display.blit(character, (x,y))
    
x = (xpos * 0.95)
y = (ypos * 0.5)

#enemy variables
#expos = 200
#eypos = 630
#timer = 0
enemy1=[220, 630, 0]
enemy2 = [165, 730,45]
enemy3 = [360, 530,40]
def enemyMove(enemyInfo):
    #print(enemyInfo)
    enemyInfo[2]+=1
    if enemyInfo[2]<= 80:
        enemyInfo[0]+=1
    elif enemyInfo[2]<=160:
        enemyInfo[0]-=1
    else:
        enemyInfo[2]= 0 #resets timer
    
def enemyCollide(enemyInfo, xpos, ypos):
    if xpos+7>enemyInfo[0]: #right side of player, left side of enemy
        if xpos < enemyInfo[0]+7: #left side of player, right side of enemy
            if ypos < enemyInfo[1]+60: #top of player bottom of enemy
                if ypos+60 > enemyInfo[1]:
                    return True
    else:
        return False

jump = pygame.mixer.Sound('C:/Users/768588/Downloads/Y2Mate.is - Mike Ehrmantraut  finger say Waltuh sound effect-JT23uK39BAY-128k-1654568025031.mp3')#load in sound effect
music = pygame.mixer.music.load('C:/Users/768588/Downloads/Y2Mate.is - Better Call Saul Main Title Theme (Extended)-5AI44gnaLxY-160k-1654318173865.mp3')#load in background music
pygame.mixer.music.play(-1)#start background music

  
jumpvolume = 1
#end function definition 
while not gameover and health >0: #GAME LOOP############################################################
    clock.tick(60) #FPS
    
    #Input Section------------------------------------------------------------
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

          
    #physics section--------------------------------------------------------------------
    #LEFT MOVEMENT
    if keys[LEFT]==True:
        vx=-3   
    #RIGHT MOVEMENT
    elif keys[RIGHT] == True:
        vx = 3
    #turn off velocity
    else:
        vx = 0   


        #JUMPING
    if keys[UP] == True and isOnGround == True: #only jump when on the ground
        vy = -8
        isOnGround = False
        direction = UP
        pygame.mixer.Sound.play(jump)
        


    
    #function call for enemy movement
    enemyMove(enemy1)
    enemyMove(enemy2)
    enemyMove(enemy3)
    
    if enemyCollide(enemy1, xpos, ypos):
        print("hit")
        health -= 10
    if enemyCollide(enemy2, xpos, ypos):
        print("hit")
        health -= 10
    if enemyCollide(enemy3, xpos, ypos):
        print("hit")
        health -= 10
    
    #COLLISION
    if xpos>100 and xpos<200 and ypos+40 >730 and ypos+40 <770:
        ypos = 730-40
        isOnGround = True
        vy = 0
    elif xpos>200 and xpos<300 and ypos+40 >630 and ypos+40 <670:
        ypos = 630-40
        isOnGround = True
        vy = 0
    elif xpos>300 and xpos<400 and ypos+40 >530 and ypos+40 <570:
        ypos = 530-40
        isOnGround = True
        vy = 0
    elif xpos>400 and xpos<500 and ypos+40 >430 and ypos+40 <470:
        ypos = 430-40
        isOnGround = True
        vy = 0
    elif xpos>500 and xpos<600 and ypos+40 >330 and ypos+40 <370:
        ypos = 330-40
        isOnGround = True
        vy = 0
    elif xpos>600 and xpos<700 and ypos+40 >230 and ypos+40 <270:
        ypos = 230-40
        isOnGround = True
        vy = 0
    elif xpos>700 and xpos<800 and ypos+40 >130 and ypos+40 <170:
        ypos = 130-40
        isOnGround = True
        vy = 0
    else:
        isOnGround = False


    
    #stop falling if on bottom of game screen
    if ypos > 741:
        isOnGround = True
        vy = 0
        ypos = 741
    
    #gravity
    if isOnGround == False:
        vy+=.2 #notice this grows over time, aka ACCELERATION
    

    #update player position
    xpos+=vx 
    ypos+=vy
    
    

  
    # RENDER Section--------------------------------------------------------------------------------
    
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
        
            
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
        
    screen.blit(backround, (0,0))
  #player
    #pygame.draw.rect(screen, (255, 255, 255), (xpos, ypos, 20, 40))
    screen.blit(Link, (xpos, ypos), (frameWidth*frameNum, RowNum*frameHeight, frameWidth, frameHeight))
    #enemy
    pygame.draw.rect(screen, (255, 255, 255), (enemy1[0], enemy1[1], 20, 20))
    pygame.draw.rect(screen, (200, 255, 255), (enemy2[0], enemy2[1], 20, 20))
    pygame.draw.rect(screen, (250, 255, 255), (enemy3[0], enemy3[1], 20, 20))

    
    #first platform
    pygame.draw.rect(screen, (200, 0, 100), (120, 750, 100, 20))
    
    #second platform
    pygame.draw.rect(screen, (50, 100, 0), (220, 650, 100, 20))
    
    pygame.draw.rect(screen, (100, 100, 0), (320, 550, 100, 20))
    
    pygame.draw.rect(screen, (0, 200, 0), (420, 450, 100, 20))
    
    pygame.draw.rect(screen, (0, 100, 200), (520, 350, 100, 20))
    
    pygame.draw.rect(screen, (100, 100, 0), (620, 250, 100, 20))
    
    pygame.draw.rect(screen, (200, 0, 200), (720, 150, 100, 20))
    
    pygame.display.flip()#this actually puts the pixel on the screen
    


if health <=0:
    print("Game over, you died")
#end game loop------------------------------------------------------------------------------
pygame.quit()