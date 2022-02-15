

from tkinter import CENTER
from scripts.Slot import Slot
from scripts.constants import SCALE, get_font


class Inventory:
    def __init__(self, quantity, pos, size):
        self.quantity = quantity
        self.pos = pos
        self.itens = list()
        self.selected = 0
        for i in range(quantity):
            self.itens.append(Slot(pos, size, None, 0))

    
    def drawInventory(self, screen):
        for i in range(self.quantity):
            self.itens[i].drawSlot(screen, (self.pos[0] + 1*SCALE*i + self.itens[i].size * i * SCALE, self.pos[1]), i == self.selected)
            count_text = get_font(int(5*SCALE)).render(str(i + 1), True, "#48180e")
            if i != self.selected:
                 count_text.set_alpha(120)
            else: 
                count_text.set_alpha(255)
            count_rect = count_text.get_rect(center = self.itens[i].rect.center)
            count_rect.top = self.itens[i].rect.bottom + SCALE
            screen.blit(count_text, count_rect)
    def addItem(self, item):
        print(self.hasItem(item))
        if self.hasItem(item):
            for i in range(self.quantity):
                if self.itens[i].item == item:
                    self.itens[i].count += 1
                    break
        else:
            for i in range(self.quantity):
                if self.itens[i].item == None:
                    self.itens[i].item = item
                    self.itens[i].count += 1
                    break
    def hasItem(self, item):
        for i in range(self.quantity):
            if self.itens[i].item == item:
                return True
        return False
    def removeItem(self, item):
        for i in range(self.quantity):
            if self.itens[i].item == item:
                self.itens[i].count -= 1
                if self.itens[i].count == 0:
                    self.itens[i].item = None
    def removeItembyIndex(self, index):
        self.itens[index].count -= 1
        if self.itens[index].count == 0:
            self.itens[index].item = None