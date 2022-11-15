import turtle
turtle.init()
pturtle.display.set_caption("flowers!")
screen = turtle.display.set_mode((1000, 1000))
screen.fill((0, 0, 0))

RED = (250,0,0)
ORANGE = (200,150,0)
GREEN = (0,150,0)
BLUE = (0, 0, 200)
PURPLE = (150, 0, 150)
WHITE = (250, 250, 250)
YELLOW = (250, 250, 0)
CYAN = (0, 250, 250)
TAN =  (210, 180, 140)

pygame.draw.rect(screen, (TAN), (200, 500, 600, 600))
pygame.draw.polygon(screen, (RED), (700, 500, 444, 600))




pygame.display.flip()
