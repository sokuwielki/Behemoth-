import pygame
from classes import Button, font, Player
import time

gray = (124, 124, 124)
behemoth_font = pygame.font.Font(None, 128)
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

def create_button(xpos,ypos, image_path, image_scale, color):
    img = pygame.image.load(image_path)
    img = pygame.transform.scale(img, (img.get_size()[0] * image_scale, img.get_size()[1] * image_scale))
    but1 = Button(xpos,ypos, img)
    but1.color = color
    but1.buttonUpdate(screen)

    return but1

def create_game_menu():
    but1 = create_button(300, 100, "pygame/assets/Sprite-0001.png", 2, (50,50,50))
    but2 = create_button(900, 100, "pygame/assets/Sprite-0001.png", 2, (50,50,50))
    but3 = create_button(300, 600, "pygame/assets/Sprite-0001.png", 2, (50,50,50))
    but4 = create_button(900, 600, "pygame/assets/Sprite-0001.png", 2, (50,50,50))
    return [[but1, but2,], [but3, but4]]

def reload_game_menu(game_menu, screen, player):
    for button_list in game_menu:
        for button in button_list:
            button.buttonUpdate(screen)
            button.color = (gray)
            button.buttonFocus(screen)
    game_menu[player.menupos[0]][player.menupos[1]].color = (255, 0, 0)
    game_menu[player.menupos[0]][player.menupos[1]].buttonFocus(screen)

def create_main_menu():
    but1 = create_button(100, 100, "pygame/assets/Sprite-0001.png", 2, (50,50,50))
    but2 = create_button(100, 300, "pygame/assets/Sprite-0001.png", 2, (50,50,50))
    but3 = create_button(100, 500, "pygame/assets/Sprite-0001.png", 2, (50,50,50))

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
            #prolly need to add sleep(5) here or wait until user input
            background = pygame.image.load(r"pygame/assets/Main_Menu_Background.jpg")
            background = pygame.transform.scale(background, (1280, 720))
            screen.blit(background, (0,0))
            game_menu = create_game_menu()

        
        
        ###MAIN GAME
        case 2:
            if pygame.key.get_just_pressed()[pygame.K_a]:
                player.menupos[1] -= 1
                player.menupos[1] = player.menupos[1] % 2
            if pygame.key.get_just_pressed()[pygame.K_d]:
                player.menupos[1] += 1
                player.menupos[1] = player.menupos[1] % 2
            if pygame.key.get_just_pressed()[pygame.K_s]:
                player.menupos[0] -= 1
                player.menupos[0] = player.menupos[0] % 2
            if pygame.key.get_just_pressed()[pygame.K_w]:
                player.menupos[0] += 1
                player.menupos[0] = player.menupos[0] % 2
            reload_game_menu(game_menu, screen, player)

            #focus to menupos
        
        
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

