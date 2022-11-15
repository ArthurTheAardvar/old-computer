import pygame
import random

print("hello world")#left for testing purposes
pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Dino Jumper")
doExit=False
touchGround = False
clock = pygame.time.Clock()
#game variables go here, above the game loop
p1x = 20
p1y = 200

yVel = 200
xVel =  20

CactusImg = pygame.image.load('C:/Users/768588/Downloads/ok cactus.jpg')

CactusHeights = [80,40,20,80,30]

CactusXpos=[]

for x in range(1, 5): #a loop that runs 5 times
    #the append function adds an entry to our array
    CactusXpos.append(random.randrange(200, 3000))
#game loop
while not doExit:
    
    clock.tick(60)
    CactusXpos = [x - 5 for x in CactusXpos]
    
    for x, y in zip(CactusXpos, CactusHeights):
        a = pygame.Rect((x, 480-y), (30, 80))
        b = pygame.Rect((p1x, p1y), (30, 30))
        if a. colliderect(b) == True:
            print("COLLISION")
    
    for x in range(len(CactusXpos)):
        if CactusXpos[x]<0:
            CactusXpos[x]=random.randrange(640, 5000)
            print("reset to ", CactusXpos[x])
    for event in pygame.event.get(): #event queue
        if event.type == pygame.QUIT:
            doExit = True;
    p1y += yVel
          
    if (p1y+30) <480:
        p1y+=1
    
    if (p1y+30) == 480:
        touchGround = True
    else:
        touchGround = False
        
        
    if touchGround == False:
        yVel += 1
    else:
        yVel = 0
    
    #input section
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and touchGround == True:
        p1y-=20
    #render section
    screen.fill((0,0,0))
    
    for x, y in zip(CactusXpos, CactusHeights):
        screen.blit(CactusImg, (x-15,480-y))
    
    pygame.draw.rect(screen, (255, 255, 255), (p1x, p1y, 200, 200), 1)
    
    pygame.display.flip()
    

#end game loop

pygame.quit()
