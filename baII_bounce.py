import pygame

pygame.init()
clock =pygame.time.Clock()

screen = pygame.display.set_mode((500,300))
pygame.display.set_caption("Bouncing Ball Game")

x1=250
y1=150

x2=285
y2=150

velocityb1 = 4
velocityb2 = 4

red =(255,0,0)
green = (0,255,0)


bounce= True

background = pygame.image.load("bg.jpg").convert()

while bounce:
    
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
           bounce= False   

    y1 = y1 + velocityb1
    y2 = y2 - velocityb2
    
   
    if y1 >= 285:
        velocityb1 -=4
    if y1 <= 15:
        velocityb1 +=4
    if y2 >= 285:
        velocityb2 +=4
    if y2 <= 15:
        velocityb2 -=4
        
        

    screen.blit(background,[0,0])
    
  
    pygame.draw.circle(screen, red, (x1,y1), 15)
    pygame.draw.circle(screen, green, (x2,y2), 15)
    
    pygame.display.update()
    clock.tick(40)
pygame.quit()                 
       
                                              
                    
                    
                
        