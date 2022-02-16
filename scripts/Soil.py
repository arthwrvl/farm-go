import pygame
from scripts import Seed
from pygame.locals import *
from scripts import BadFruit
from scripts.Can import Can
from random import randint
from scripts import Fruit

from scripts.Hoe import Hoe


class Soil(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        pygame.sprite.Sprite.__init__(self)
        self.seed = None
        self.selected = False
        #*load images
        self.dry = []
        self.prepared = []
        for i in range(1,4):
            self.dry.append(pygame.image.load(f"data/sprites/scenary/Soil/dry/{i}.png"))
            self.prepared.append(pygame.image.load(f"data/sprites/scenary/Soil/prepared/{i}.png"))
        self.water = pygame.image.load("data/sprites/scenary/Soil/water_drop.png")
        #*set state
        self.state = 0 # 0 = dry, 1 = prepared, 2 = need water, 3 = planted, 4 = ready, 5 = bad

        #*set image
        self.image = self.dry[randint(0,2)]
        self.lastImage = self.image

        self.pos = pos
        

        #*set size
        self.size = size
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect(topleft = self.pos)
        self.hitbox = pygame.Rect(self.pos[0], self.pos[1], self.size, self.size)
    
    def AddSeed(self, seed, screen):
        self.seed = seed
        #print(self.seed.fruit)
        #self.seed.show_image(self.seed.image, self.size/3, self.size/3)
        #self.state = 4
        #self.selected = False
            
    def grow_seed(self):
        #print("grow")
        if self.state != 4:
            self.state = 4
            self.image = self.dry[randint(0,2)]
            self.Redraw()
    def bad_fruit(self):
        self.state = 5
        #self.seed.show_fruit(screen, self.size/3, self.size/3)
        #self.state = 5

   
    def ChangeState(self):
        if self.state == 0:
            self.image = self.dry[randint(0,2)]
        elif self.state == 1:
            index = randint(0,2)
            self.image = self.prepared[index]
            self.lastImage = self.prepared[index]
            self.Select()
        elif self.state == 2:
            pass
            #print("planted")
            #self.AddSeed()
            #add seed sprite
        elif self.state == 3:
            pass
        elif self.state == 4:
            self.image = self.dry[randint(0,2)]
            #print("need water")
            #add water sprite
        elif self.state == 5:
            self.image = self.dry[randint(0,2)]
        self.Redraw()

    def Interact(self, player, screen):
        #print(self.state)
        if self.state == 0:
            if isinstance(player.inventory.itens[player.inventory.selected].item, Hoe):
                self.state = 1
                self.ChangeState()
        elif self.state == 1 and self.seed == None:
            if isinstance(player.inventory.itens[player.inventory.selected].item, Seed.Seed):
                self.AddSeed(player.inventory.itens[player.inventory.selected].item, screen)
                player.inventory.removeItembyIndex(player.inventory.selected)
                self.state = 2
                self.ChangeState()
        elif self.state == 2:
            if isinstance(player.inventory.itens[player.inventory.selected].item, Can):
                if player.inventory.itens[player.inventory.selected].item.use():
                    self.state = 3
                    self.ChangeState()
        elif self.state == 4:
            if player.inventory.hasItem(BadFruit.badfruits[Fruit.fruits.index(self.seed.fruit)]) == False or player.inventory.IsFull() == False:
                player.inventory.addItem(self.seed.fruit)
                self.state = 0
                self.seed = None
                self.ChangeState()
        elif self.state == 5:
            if player.inventory.hasItem(BadFruit.badfruits[Fruit.fruits.index(self.seed.fruit)]) == False or player.inventory.IsFull() == False:
                player.inventory.addItem(BadFruit.badfruits[Fruit.fruits.index(self.seed.fruit)])
                self.state = 0
                self.seed = None
                self.ChangeState()
        

    def Select(self):
        if self.selected == False:
            self.lastImage = self.image.copy()
            self.color = pygame.Surface(self.image.get_size()).convert_alpha()
            self.color.fill(pygame.Color("#FFFFFFAA"))
            self.image.blit(self.color, (0, 0), special_flags=BLEND_RGBA_MULT)
            self.selected = True

    def Deselect(self):
        if self.selected == True:
            self.image = self.lastImage
            self.image = pygame.transform.scale(self.image, (self.size, self.size))
            self.selected = False

    def Redraw(self):
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect(topleft = self.pos)

    def overdraw(self, screen):
        print(self.state)
        if self.state == 2:
            seed_image = pygame.transform.scale(self.seed.image, (int(self.size/3), int(self.size/3)))
            seed_rect = seed_image.get_rect(center = self.rect.center)
            screen.blit(seed_image, seed_rect)
            self.water = pygame.transform.scale(self.water, (int(self.size*0.6), int(self.size*0.6)))
            screen.blit(self.water, self.pos)
        elif self.state == 3:
            seed_image = pygame.transform.scale(self.seed.image, (int(self.size/3), int(self.size/3)))
            seed_rect = seed_image.get_rect(center = self.rect.center)
            screen.blit(seed_image, seed_rect)
        if self.state == 4:
            if(self.seed != None):
                fruit_image = self.seed.fruit.image.copy()
                fruit_image = pygame.transform.scale(fruit_image, (int(self.size*0.8), int(self.size*0.8)))
                fruit_rect = fruit_image.get_rect(center = self.rect.center)
                screen.blit(fruit_image, fruit_rect)
        if self.state == 5:
            print("bad")
            if self.seed != None:
                print("drawing")
                index = Fruit.fruits.index(self.seed.fruit)
                fruit_image = BadFruit.badfruits[index].image.copy()
                fruit_image = pygame.transform.scale(fruit_image, (int(self.size*0.8), int(self.size*0.8)))
                fruit_rect = fruit_image.get_rect(center = self.rect.center)
                screen.blit(fruit_image, fruit_rect)


'''

'''

        

            
        
