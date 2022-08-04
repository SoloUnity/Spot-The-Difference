from math import pi
import pygame
import time
pygame.font.get_fonts()


pygame.init()
screen = pygame.display.set_mode((1024, 768))
done = False
color = (0, 0, 204)
x = 100
y = 100

plate = 0
ketchup = 0
hat = 0
differences = 3
guesses = 3

x2 = 200
y2 = 100

x3 = 100
y3 = 100


img = pygame.image.load('/Users/gordonng/Documents/Coding/Python/High School Python Assignments/Differences spoongebob/sponge.jpeg')

clock = pygame.time.Clock()

while not done:

        mousePress = pygame.mouse.get_pressed() #Returns if a mouse button has been pressed
        mouse = pygame.mouse.get_pos() #Returns the mouse position
        print ("x coordinate:", mouse[0])
        print ("y coordinate:", mouse[1])

        screen.fill((0, 0, 0)) #paint the screen black

        screen.blit(img, (0, 0)) #attach your image to the screen at specific location. Step 2

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.MOUSEBUTTONUP:
                        guesses = guesses - 1


        if plate == 0 or ketchup == 0 or hat == 0:
                pygame.draw.rect(screen, color, pygame.Rect(0, 0, 1024, 75))
                pygame.draw.rect(screen, color, pygame.Rect(509, 0, 12, 768))

                fontInfo = pygame.font.Font('freesansbold.ttf',50)
                textBox = fontInfo.render("Spot the Difference", True, (0,0,0) )
                screen.blit(textBox,(290,15))

                fontInfo2 = pygame.font.Font('freesansbold.ttf',20)
                textBox2 = fontInfo2.render("Differences left =" , True, (0,0,0))
                screen.blit(textBox2,(800,50))
                textBox3 = fontInfo2.render(str(differences) , True, (0,0,0))
                screen.blit(textBox3,(970,50))


                textBox4 = fontInfo2.render("Guesses left =" , True, (0,0,0))
                screen.blit(textBox4,(10,50))
                textBox5 = fontInfo2.render(str(guesses) , True, (0,0,0))
                screen.blit(textBox5,(160,50))

                if event.type == pygame.MOUSEBUTTONUP:
                        if mouse[0] > 910 and mouse[0] < 980 and mouse[1] > 360 and mouse[1] < 450:
                                plate = plate + 1
                        if mouse[0] > 890 and mouse[0] < 960 and mouse[1] > 190 and mouse[1] < 260:
                                ketchup = ketchup + 1
                        if mouse[0] > 765 and mouse[0] < 835 and mouse[1] > 305 and mouse[1] < 375:
                                hat = hat + 1

                if plate != 0:
                        pygame.draw.arc(screen, (255, 0, 0),[910, 360, 100, 100], 0, 2*pi, 7)
                        differences = 2
                if ketchup != 0:
                        pygame.draw.arc(screen, (255, 0, 0),[890, 190, 100, 100], 0, 2*pi, 7)
                        differences = 2
                if hat != 0:
                        pygame.draw.arc(screen, (255, 0, 0),[765, 305, 100, 100], 0, 2*pi, 7)
                        differences = 2

                if plate != 0 and ketchup != 0:
                        differences = 1
                elif plate != 0 and hat != 0:
                        differences = 1
                elif ketchup != 0 and hat != 0:
                        differences = 1

                if hat != 0 and ketchup != 0 and plate != 0:
                        differences = 0
        if guesses <= 0 and differences != 0:
                pygame.draw.rect(screen, color, pygame.Rect(0, 0, 1024, 768))
                fontInfo = pygame.font.Font('freesansbold.ttf',150) #Sets up font and sie
                textBox = fontInfo.render("YOU LOSE!", True, (0,0,0) ) #Attach some text and color to font
                screen.blit(textBox,(130,250)) #Place text on screen at a specific location
        elif differences == 0:
                pygame.draw.rect(screen, color, pygame.Rect(0, 0, 1024, 768))
                fontInfo = pygame.font.Font('freesansbold.ttf', 150)  # Sets up font and sie
                textBox4 = fontInfo.render("YOU WIN!", True, (0, 0, 0))  # Attach some text and color to font
                screen.blit(textBox4, (130, 250))  # Place text on screen at a specific location

        pygame.display.flip()
        # will block execution until 1/60 seconds have passed
        # since the previous time clock.tick was called.
        clock.tick(60)


