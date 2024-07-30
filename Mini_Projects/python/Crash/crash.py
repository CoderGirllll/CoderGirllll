import pygame
import random

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)


block_color = (100, 125, 165)

car_width = 73

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Crash')
clock = pygame.time.Clock()

carImg = pygame.image.load('Mini_Projects\python\Effects\\racecar.png')
gameIcon = pygame.image.load("Mini_Projects\python\Effects\\carIcon.png")
crash_sound = pygame.mixer.Sound("Mini_Projects\python\Effects\\crash.wav")
pygame.mixer.music.load("Mini_Projects\python\Effects\\backmusic.wav")

pygame.display.set_icon(gameIcon)


def things_dodged(count):
    font = pygame.font.SysFont(None, 30)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text, (0, 0))


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def car(x,y):
    gameDisplay.blit(carImg, (x,y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()


def crash():
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()

    message_display("You Crashed")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
    
        button("Play Again", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
        
        gameDisplay.fill(white)

        #Title
        message_display("Crash")

        #Buttons
        button("GO!", 150, 450, 100, 50, green, bright_green, game_loop)
        button("QUIT!", 550, 450, 100, 50, bright_red, red, quitgame)

        pygame.display.update()
        clock.tick(15)


def button(msg, x, y, w, h, ic, ac, action=None):
    #Getting the positions of the mouse
    mouse = pygame.mouse.get_pos()
    #Checking if mouse clicked
    click = pygame.mouse.get_pressed()

    #Making button change color to seem interactive
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    #Text for button
    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)


def game_loop():
    pygame.mixer.music.play(-1)

    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    #Dimensions of rectangles
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    thingCount = 1

    dodged = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                quitgame()
            
            #User input and car movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    global pause
                    pause = True
                    paused()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill((240, 180, 112))   #Was white, changed background color

        #Using the function things to draw rectangles on screen
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)
        
        #Adding boundaries for car
        if x > display_width - car_width or x < 0:
            crash()

        #Moving rectangles
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged + 1.2)
        
        #Car crashing with rectangle
        if y < thing_starty+thing_height: #Checking for y coordinate
            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width: #Checking for x coordinate
                crash()

        pygame.display.update()
        clock.tick(60)


def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False


def paused():
    pygame.mixer.music.pause()

    message_display("Paused")

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
        
        button("Continue", 150, 450, 100, 50, green, bright_green, unpause)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def quitgame():
    pygame.quit()
    quit()


game_intro()
quitgame()