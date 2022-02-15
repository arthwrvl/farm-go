import pygame

class BadFruit:
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image

badfruits = list()
badfruits.append(BadFruit(pygame.image.load("data/sprites/itens/Fruit/bad/apple.png")))
badfruits.append(BadFruit(pygame.image.load("data/sprites/itens/Fruit/bad/avocado.png")))
badfruits.append(BadFruit(pygame.image.load("data/sprites/itens/Fruit/bad/banana.png")))
badfruits.append(BadFruit(pygame.image.load("data/sprites/itens/Fruit/bad/blueberry.png")))
badfruits.append(BadFruit(pygame.image.load("data/sprites/itens/Fruit/bad/carrot.png")))
badfruits.append(BadFruit(pygame.image.load("data/sprites/itens/Fruit/bad/lemon.png")))
badfruits.append(BadFruit(pygame.image.load("data/sprites/itens/Fruit/bad/orange.png")))
badfruits.append(BadFruit(pygame.image.load("data/sprites/itens/Fruit/bad/papaya.png")))
badfruits.append(BadFruit(pygame.image.load("data/sprites/itens/Fruit/bad/plum.png")))
badfruits.append(BadFruit(pygame.image.load("data/sprites/itens/Fruit/bad/potato.png")))