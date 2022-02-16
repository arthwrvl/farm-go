from random import randint
import pygame
from scripts.Fruit import Fruit

from scripts.constants import CORRECT, SCALE, WRONG, play_sound

class Car(pygame.sprite.Sprite):
    def __init__(self, pos, size, groups):
        pygame.sprite.Sprite.__init__(self, groups)
        self.pos = pos
        self.size = size
        self.image = pygame.image.load("data/sprites/scenary/car.png")
        self.image = pygame.transform.scale(self.image, (int(self.size[0]*SCALE), int(self.size[1]*SCALE)))
        self.rect = self.image.get_rect(topleft = self.pos)
        self.hitbox = pygame.Rect(self.rect.x, self.rect.y + self.rect.height*0.13, self.rect.width, self.rect.height*0.87)
        self.y = self.pos[1]
        self.deliver = list()
        self.hitbox_interact = pygame.Rect(self.pos[0], self.pos[1]  - int(self.size[1]*SCALE*0.1), int(self.size[0]*SCALE), int(self.size[1]*SCALE*1.1))

    def Interact(self, player):
        if isinstance(player.inventory.itens[player.inventory.selected].item, Fruit):
            if len(self.deliver) < 5:
                self.deliver.append(player.inventory.itens[player.inventory.selected].item)
                player.inventory.removeItembyIndex(player.inventory.selected)
    
    def drawDeliver(self, screen):
        for i in range(0, len(self.deliver)):
            deliver_image = self.deliver[i].image.copy()
            deliver_rect = deliver_image.get_rect(topleft = (self.pos[0] + self.size[0]*0.2*SCALE + deliver_image.get_rect().width * i + 2*SCALE*i, self.pos[1] + self.size[1]*0.5*SCALE))
            screen.blit(deliver_image, deliver_rect)
            print("drew")

    def Deliver(self, orderlist, player):
        if len(self.deliver) > 0:
            for i in orderlist:
                if i.random_fruit in self.deliver:
                    if self.deliver.count(i.random_fruit) >= i.number:
                        player.money += i.random_fruit.sale_price * i.number
                        player.score += randint(10*i.number, 15*i.number)
                        self.deliver = list()
                        play_sound(CORRECT)
                    else:
                        player.money += int(i.random_fruit.sale_price * self.deliver.count(i.random_fruit)/2)
                        player.score += randint(5*self.deliver.count(i.random.fruit), 15*self.deliver.count(i.random_fruit))
                        self.deliver = list()
                        play_sound(WRONG)
                    return orderlist.index(i)
            
            player.score -= randint(10*orderlist[0].number, 15**orderlist[0].number)
            self.deliver = list()
            print(player.score)
            print(player.money)
            play_sound(WRONG)
            return 0



                


            
