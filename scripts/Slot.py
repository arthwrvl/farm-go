from textwrap import fill
import pygame

from scripts.constants import SCALE, get_font

class Slot:
    def __init__(self, pos, size, item, count):
        self.pos = pos
        self.size = size
        self.item = item
        self.count = count
        self.images = list()
        self.images.append(pygame.image.load("data/sprites/inventory/slot/slot.png").convert_alpha())
        self.images.append(pygame.image.load("data/sprites/inventory/slot/selected.png").convert_alpha())
        self.image = self.images[0]

        self.rect = self.image.get_rect(topleft = pos)
    

    def drawSlot(self, screen, pos, selected):
        if selected:
            self.image = self.images[1]
            self.image = pygame.transform.scale(self.image, (int(self.size * SCALE), int(self.size * SCALE)))
        else:
            self.image = self.images[0]
            self.image = pygame.transform.scale(self.image, (int(self.size * SCALE), int(self.size * SCALE)))

        self.rect = self.image.get_rect(topleft = pos)
        screen.blit(self.image, self.rect)
        if self.item != None:
            item_icon = self.item.image
            item_icon = pygame.transform.scale(item_icon, (int(self.size*0.7 * SCALE), int(self.size*0.7 * SCALE)))
            if selected:
                item_icon.set_alpha(255)
            else:
                item_icon.set_alpha(100)
            icon_rect = item_icon.get_rect(center = self.rect.center)
            screen.blit(item_icon, icon_rect)
        if self.count > 1:
            count_text = get_font(int(5*SCALE)).render(str(self.count), True, "#48180e")
            if selected:
                count_text.set_alpha(255)
            else:
                count_text.set_alpha(100)
            count_rect = count_text.get_rect(bottomright = self.rect.bottomright)
            screen.blit(count_text, count_rect)
        if hasattr(self.item, "value"):
            bar = pygame.Surface((self.rect.width *0.8, self.rect.height*0.08))
            fill = pygame.Surface((self.rect.width *0.8 * self.item.value/self.item.maxvalue, self.rect.height*0.08))
            if not selected:
                bar.set_alpha(100)
                fill.set_alpha(100)
            else:
                bar.set_alpha(255)
                fill.set_alpha(255)
            bar.fill("#2f0a07")
            fill.fill("#2aa5ff")
            screen.blit(bar, (self.rect.left + 1.5 *SCALE, self.rect.top + self.rect.height* 0.85))
            screen.blit(fill, (self.rect.left + 1.5 *SCALE, self.rect.top + self.rect.height* 0.85))
            #pygame.draw.rect(screen, "#2f0a07", pygame.Rect(self.rect.left + 1.5 *SCALE, self.rect.top + self.rect.height* 0.85, self.rect.width *0.8, self.rect.height*0.08))
            #pygame.draw.rect(screen, "#2aa5ff", pygame.Rect(self.rect.left + 1.5 *SCALE, self.rect.top + self.rect.height* 0.85, self.rect.width *0.8 * self.item.value/self.item.maxvalue, self.rect.height*0.08))
