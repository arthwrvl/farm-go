import pygame 
from pygame.locals import *
from scripts import Fruit
from scripts import Seed
from random import randint
from scripts.constants import *


class Order:
    def __init__(self):
        #self.random_fruit = Fruit.Fruit.random_fruit()
        self.random_id = randint(0, len(Fruit.fruits) - 1)
        self.random_fruit = Fruit.fruits[self.random_id]
        self.fruit = [self.random_fruit.name, self.random_fruit.shelf_life, self.random_fruit.image, self.random_fruit.sale_price]
        self.number = randint(1, 3)
        self.waiting_time = 40
        self.show = False
        self.screen = pygame.display.get_surface()
        self.background = pygame.Rect((self.screen.get_width()*0.88,self.screen.get_height()*0.1),(self.screen.get_width()*0.1, self.screen.get_height()*0.2))
        self.region = pygame.Rect((0,0), (self.background.width*0.90, self.background.height*0.94))
        self.region.midbottom = self.background.midbottom + pygame.Vector2(0, -self.background.height*0.02)

    def DrawOrder(self, screen, order):
        if self.show == True:
            pygame.draw.rect(screen, (68,62,36), self.background, border_radius=20)
            pygame.draw.rect(screen, (152,139,93), self.region, border_radius=20)
            order.random_fruit.show_img(screen, screen.get_width()*0.905, screen.get_height()*0.125)
            text = get_font(int(10*SCALE)).render(str(order.number), 1, "#48180e")
            text_rect = text.get_rect(center=(screen.get_width()*0.937, screen.get_height()*0.26))
            screen.blit(text, text_rect)

    def NewOrder(self, aux_current_time, screen):
        self.current_time = pygame.time.get_ticks() // 1000
        if self.current_time > aux_current_time:
            aux_current_time = self.current_time
            print(aux_current_time)

            if aux_current_time % self.waiting_time == 0:
                self.order = Order()
                print(f"WAITING TIME = {self.waiting_time}")
                print(f"NUMBER 0F FRUITS = {self.order.number}")
                print(self.order.fruit[0])

            if aux_current_time % (self.waiting_time) == 1 and aux_current_time != 1:
                self.order.show = True
   
        if self.current_time > (self.waiting_time):
            self.order.DrawOrder(screen, self.order)
        
    def GetCurrentTime(self):
        return self.current_time

    def CheckOrderCollision(self, player_hitbox, player):
        if player_hitbox.colliderect(self.region):
            if self.order.number <= Seed.Seed.picked_fruits[self.order.fruit[0]]:
                print("sold")
                player.money += self.order.fruit[3] * self.order.number
                print(f"MONEY = {player.money}")
                player.score += self.order.number * 5
                print(f"SCORE = {player.score}")
                Seed.Seed.picked_fruits[self.order.fruit[0]] -= self.order.number
                self.order.show = False

