import pygame
pygame.init()

screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("Pong")


bx = 350
by = 250
bVx = 5
bVy = 5

p1Score = 0
p2Score = 0

p1x = 20
p1y = 200

p2x = 660
p2y = 200

doExit = False



clock = pygame.time.Clock()

while not doExit:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True
            

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        p1y-=5
    if keys[pygame.K_s]:
        p1y+=5
        
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        p2y-=5
    if key[pygame.K_DOWN]:
        p2y+=5


    bx += bVx
    by += bVy
    
    if bx < 0 or bx + 20 > 700:
        bVx *= -1
        
    if by <0 or by +20 >500:
        bVy *=-1

    #collision with paddle1
    if bx < p1x + 35 and by +35 > p1y and by <p1y +100:
        bVx*=-1
        print("collision with 1", end = " ")
    
    #collision with paddle2
    if bx+10 > p2x and bx < p2x+35 and by <p2y +100 and by > p2y:
        bVx*=-1
        print("collision with 2", end = " ")
    
    #collision with LEFT wall
    if bx < 0:
     
        p2Score += 1
            
    #collision with RIGHT wall 
    if bx +20 > 700:
  
        p1Score+=1
    

        
    screen.fill((0,0,0))
    
    font = pygame.font.Font(None,74)
    text = font.render(str(p1Score), 1, (255, 255, 255))
    screen.blit(text, (250,10))
    text = font.render(str(p2Score), 1, (255, 255, 255))
    screen.blit(text, (420,10))

    pygame.draw.line(screen, (255, 255, 255), [349, 0], [349, 500], 5)

   
    pygame.draw.rect(screen, (255, 255, 255), (p1x, p1y, 20, 100), 1)
    
    pygame.draw.rect(screen, (255, 255, 255), (p2x, p2y, 20, 100), 1)
    
    pygame.draw.circle(screen, (255, 255, 255), (bx, by), 10)
    
    
    pygame.display.flip()




pygame.quit()
            
            
            
