#Hello coding club! Here is where we will make the pong game.

#Hello!

#Import and initialize pygame
import pygame
pygame.init()

#Set the display size, make the display, give it a title
display_width = 800
display_height = 800
display_size = (display_width, display_height)
display = pygame.display.set_mode(display_size)
pygame.display.set_caption("Snake")

#Set the starting position for paddle1
paddle1_y = 400

paddle1_height = 100

#Start the game loop
running = True
while running:

    #This for loop handles all pygame events such as when the window is closed and when a key is pressed
    for event in pygame.event.get():
        #Set running to false when the window is closed
        if event.type == pygame.QUIT:
            running = False

    #This line makes a list of bools for each key on the keyboard, true if it is pressed
    keys = pygame.key.get_pressed()

    #Here we check if the keys "w" or "s" from the list are pressed and if they are (and the paddle is within the screen height) we move paddle 1 up or down (the y is flipped)
    if keys[pygame.K_w] and paddle1_y >= 0:
        paddle1_y -= 0.5

    if keys[pygame.K_s] and paddle1_y <= (display_height - paddle1_height):
        paddle1_y += 0.5


    #This sets the entire display/window to be the RGB of 0, 0, 0 which is black. I believe it is black by default but this allows different colors in the future
    display.fill((0, 0, 0))

    #This creates a new rectangle variable that stores the position (x, y) and size (width, height) of a rectangle
    paddle1_rect = pygame.Rect(5, paddle1_y, 20, 100)

    #Creates a new rgb color for our paddle. 255, 255, 255 is white.
    paddle1_color = (255, 255, 255)

    #This draws the rectangles using 3 arguments. Surface to draw on, color (the color we just set), and what shape to draw (the rectangle we made just before this)
    pygame.draw.rect(display, (255, 255, 255), paddle1_rect)

    #This must be done in order to show the changes made to the displayer
    pygame.display.update()

pygame.quit()