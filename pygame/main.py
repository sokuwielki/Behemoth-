import pygame
from classes import Button, font, Player
import time

gray = (124, 124, 124)
behemoth_font = pygame.font.Font(None, 128)
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True


def create_main_menu():
    img = pygame.image.load("assets/Sprite-0001.png")
    img = pygame.transform.scale(img, (img.get_size()[0] * 2, img.get_size()[1] * 2))
    but1 = Button(100,100, img)
    but1.color = (50,50,50)
    but1.buttonUpdate(screen)
    

    img = pygame.image.load("assets/Sprite-0001.png")
    img = pygame.transform.scale(img, (img.get_size()[0] * 2, img.get_size()[1] * 2))
    but2 = Button(100,300, img)
    but2.color = (50,50,50)
    but2.buttonUpdate(screen)


    img = pygame.image.load("assets/Sprite-0001.png")
    img = pygame.transform.scale(img, (img.get_size()[0] * 2, img.get_size()[1] * 2))
    but3 = Button(100,500, img)
    but3.color = (50,50,50)
    but3.buttonUpdate(screen)


    main_menu = [but1, but2, but3]

    return main_menu

def reload_main_menu(main_menu, screen, player):

    for button in main_menu:
        button.buttonUpdate(screen)
        button.color = (gray)
        button.buttonFocus(screen)
    match player.player_input:
        case 's':
            player.choice += 1
            if player.choice > len(main_menu)-1:
                player.choice = 0
        case 'w':
            player.choice -= 1
            if player.choice < 0:
                player.choice = len(main_menu)-1        
    
    main_menu[player.choice].color = (255, 0, 0)
    main_menu[player.choice].buttonFocus(screen)
    
    #return player.choice

def play_cutscene(progress, screen):

    text = ''  # Initialize the text to be displayed
    string = "Let's test it out"

    match progress:
        case 0:
            #pass # first cutscene, something along the lines of "World is full of monsters, some of them are called Behemoths"
            for letter in string:
                text += letter  # Add the next letter to the text
                rendered_text = font.render(text, True, (255, 255, 255))  # Render the text
                screen.blit(rendered_text, (200, 200))  # Display the text on the screen
                pygame.display.flip()  # Update the display
                time.sleep(0.1)  # Add a delay to control the speed of printing

        case 1:
            pass

        case 2:
            pass

player = Player()

main_menu = create_main_menu()

##############BACKGROUND
screen.fill("purple")

text_surface = behemoth_font.render("BEHEMOTH", True, (255,255,255))
screen.blit(text_surface, (400, 200))



reload_main_menu(main_menu, screen, player)

states = {"Main_Menu":0, "Cutscene":1, "Main_Game":2, "Battle_Phase":3}

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Save the pressed key
            player.player_input = pygame.key.name(event.key)

    # fill the screen with a color to wipe away anything from last frame
    match states[player.state]:
        # Main Menu Part
        case 0:
            #reload_main_menu(main_menu, screen, player)
            """while running:
                # poll for events
                # pygame.QUIT event means the user clicked X to close your window
                for event2 in pygame.event.get():
                    if event2.type == pygame.QUIT:
                        running = False
                    if event2.type == pygame.KEYDOWN:
                        # Save the pressed key
                        player.player_input = pygame.key.name(event2.key)"""
            if pygame.key.get_just_pressed()[pygame.K_w] or pygame.key.get_just_pressed()[pygame.K_s]:
                reload_main_menu(main_menu, screen, player)

            ### MOVE TO THE GAME

            if pygame.key.get_just_pressed()[pygame.K_SPACE] and player.choice == 0:
                player.state = "Cutscene"


            ### QUIT
            if pygame.key.get_just_pressed()[pygame.K_SPACE] and player.choice == len(main_menu)-1:
                pygame.quit()
        
        
        ###OPENING CUTSCENE
        case 1: #All cutscenes played here, all handled by the play_cutscene function
            screen.fill("purple")
            play_cutscene(player.progress, screen)
            player.state = "Main_Game"

        
        
        ###MAIN GAME
        case 2: #main game loop, battle will be most likely outside of it, will take most code anyway
            print("works")
            #load_background -> should do stuff like, move the background, maybe with a nice sliding animation when we move
            #actually, only the background needs to move, we don't have to move the player (maybe for a cutscene, but we gotta center it back then)

            #saving where we're at on the map and npc states are gonna be hard

        
        
        case 3: #Battle Phase
            pass #could do stuff like difficulty 


    


   


    #TODO:
    #split phases with something like phase[player.choice]()
    

    
    #print(img.get_size())
    

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

