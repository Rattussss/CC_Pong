#Hello coding club! Here is where we will make the pong game.

#Import and initialize pygame
import pygame
pygame.init()

#Set the display size, make the display, give it a title
display_size = (800, 800)
display = pygame.display.set_mode(display_size)
pygame.display.set_caption("Snake")

#Start the game loop
running = True
while running:

    #This code runs whenever the window is closed. It doesn't do anything important right now
    #If we want to save the game or something like that in the future though we will put the code to do that down
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #Down here!
            running = False

    #This sets the entire display/window to be the RGB of 0, 0, 0 which is black. I believe it is black by default but this allows different colors in the future
    display.fill((0, 0, 0))

    #This creates a new rectangle variable that stores the position (x, y) and size (width, height) of a rectangle
    paddle1_rect = pygame.Rect(5, 400, 20, 100)

    #Creates a new rgb color for our paddle. 255, 255, 255 is white.
    paddle1_color = (255, 255, 255)

    #This draws the rectangles using 3 arguments. Surface to draw on, color (the color we just set), and what shape to draw (the rectangle we made just before this)
    pygame.draw.rect(display, (255, 255, 255), paddle1_rect)

    #This must be done in order to show the changes made to the displayer
    pygame.display.update()

pygame.quit()