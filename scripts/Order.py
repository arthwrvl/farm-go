import pygame 
from pygame.locals import *
from scripts import Fruit
from random import randint


class Order:
    def __init__(self):
        self.random_fruit = Fruit.Fruit.random_fruit()
        self.fruit = [self.random_fruit.name, self.random_fruit.shelf_life, self.random_fruit.img]
        self.number = randint(1, 3)
        self.waiting_time = 0
        self.show = False

    def DrawOrder(self, screen):
        if self.show == True:
            background = pygame.Rect((screen.get_width()*0.88,screen.get_height()*0.1),(screen.get_width()*0.1, screen.get_height()*0.2))
            region = pygame.Rect((0,0), (background.width*0.90, background.height*0.94))
            region.midbottom = background.midbottom + pygame.Vector2(0, -background.height*0.02)
            pygame.draw.rect(screen, (152,139,93), background, border_radius=20)
            pygame.draw.rect(screen, (68,62,36), region, border_radius=20)

    def NewOrder(self, aux_current_time, screen):
        self.current_time = pygame.time.get_ticks() // 1000
        if self.current_time > aux_current_time:
            aux_current_time = self.current_time
            print(aux_current_time)

            if aux_current_time % (self.waiting_time + 5) == 0:
                self.order = Order()
                print(f"self.waiting_time = {self.waiting_time + 5}")
                print(self.order.fruit[0])

            if aux_current_time % (self.waiting_time + 5) == 1 and aux_current_time != 1:
                self.order.show = True
            
        if self.current_time > (self.waiting_time + 5):
            self.order.DrawOrder(screen)

    def GetCurrentTime(self):
        return self.current_time