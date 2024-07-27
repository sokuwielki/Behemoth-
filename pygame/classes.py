import pygame

try:
    user_settings = open("settings.txt", "r")
except FileNotFoundError:
    user_settings = open("settings.txt", "a")
    user_settings.write("default settings") #TODO

#print("penis")
#print(user_settings.readlines())



pygame.font.init()
font = pygame.font.Font(None, 36)

class Game:
    def __init__(self):
        pass

    #somewhere here put reading from the settings.txt

    def start_new_game(self, user_name):
        open(user_name + ".txt", "a")


    def load_save(self, save_path): #Users gonna need to input their paths here, otherwise some permision shit might happen ¯\_(ツ)_/¯
        save_file = open(save_path, "r")
        print(save_file.readline())


class Behemoth:
    def __init__(self, name, hp, atk, defense, stamina):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.stamina = stamina
        self.moves = []
        self.type = ""

    def attack(self, other):
        pass

    def defense(self, other):
        pass

    def special_move(self, other, move):
        pass

class Player:
    def __init__(self):
        self.player_input = ""
        self.inventory = []
        self.team = []
        self.level = 0
        self.exp = 0
        self.choice = 0
        self.state = "Main_Menu"
        self.progress = 0
        self.menupos = [0, 0]





class Button:
    def __init__(self, x, y, img):
        self.pos = (x,y)
        self.img = img
        self.offset = 10
        self.rect = pygame.Rect(x-(self.offset/2), y-(self.offset/2), img.get_size()[0]+self.offset, img.get_size()[1]+self.offset)
        self.color = (0,0,0)
        self.text = ""
    
    def buttonUpdate(self, screen):
        screen.blit(self.img, self.pos)

    def buttonFocus(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, width=3)

    def displayText(self, screen, text):
        text_surface = font.render(text, True, (255,255,255))
        screen.blit(text_surface, (self.pos[0]+(self.rect.width/2), self.pos[1]+(self.rect.height/2)))