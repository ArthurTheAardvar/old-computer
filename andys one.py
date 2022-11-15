import pygame
pygame.init()
pygame.display.set_caption("sprite sheet")
screen = pygame.display.set_mode((800, 800))
screen.fill((0,0,0))
clock = pygame.time.Clock()
gameover = False

#CONSTANTS
LEFT=0
RIGHT=1
UP = 2
DOWN = 3

Link = pygame.image.load('C:/Users/768588/Downloads/link.png')
Link.set_colorkey((255, 0, 255))


xpos = 500
ypos = 200
vx = 0
vy = 0
keys = [False, False, False, False]



frameWidth = 64
frameHeight = 96
RowNum = 0
frameNum = 0
ticker = 0

while not gameover:
    clock.tick(60)
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
    if event.type == pygame.KEYDOWN: #keyboard input
        if event.key == pygame.K_LEFT:
            keys[0]=True
               
        elif event.key == pygame.K_RIGHT:
             keys[1]=True
               
        elif event.key == pygame.K_UP:
            keys[2]=True
               
        elif event.key == pygame.K_DOWN:
             keys[3]=True
               
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            keys[0]=False
           
        elif event.key == pygame.K_RIGHT:
            keys[1]=False
               
        elif event.key == pygame.K_UP:
            keys[2]=False
               
        elif event.key == pygame.K_DOWN:
            keys[3]=False
        #left
    if keys[LEFT]==True:
        vx=-3
        direction = 0
        #right
    elif keys[RIGHT]==True:
        vx = 3
        direction = 1
    elif keys[UP]==True:
        vy = -3
        direction = 2
    elif keys[DOWN]==True:
        vy = 3
        direction = 3
    else:
        vx=0
        vy=0
   
       
    xpos+=vx
    ypos+=vy
       
        #animation
    if vx < 0:
        RowNum=0
        ticker+=1
        if ticker%5==0:
            frameNum+=1
        if frameNum>7:
            frameNum = 0
    if vx > 0:
        RowNum=1
        ticker+=1
        if ticker%5==0:
            frameNum+=1
        if frameNum>7:
            frameNum = 0
        #renders
    screen.fill((0,0,0))
    screen.blit(Link, (xpos, ypos), (frameWidth*frameNum, RowNum*frameHeight, frameWidth, frameHeight))
    pygame.display.flip()
#end of loop
pygame.quit()
