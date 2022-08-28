import pygame as py
from pygame.locals import *
from random import randint


largura, altura = 500, 800

class Bird(py.sprite.Sprite):
    def __init__(self, dir_img, x_img, y_img):
        py.sprite.Sprite.__init__(self)
        
        self.dir_img = dir_img
        self.x_img = x_img
        self.y_img = y_img
        self.altura = altura
        self.corremais = 0
        self.corre = 0
        self.pula = False
        self.angulo = 0
        
        self.bird_sheet = py.image.load(self.dir_img).convert_alpha()
        self.bird_sheet = py.transform.scale(self.bird_sheet, (0.70*self.bird_sheet.get_width(), 0.70*self.bird_sheet.get_height()))
        
        self.sprite_list = []
        for c in range(3):
            img = self.bird_sheet.subsurface((c*(0.70*86), 0), (0.70*86, 0.70*64))
            self.sprite_list.append(img)
        
        self.n_sprite = 0
        self.image = self.sprite_list[self.n_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x_img, self.y_img)
        self.mask = py.mask.from_surface(self.image)
    
        
    def jump(self):
        self.pula = True
    
    
    def update(self):
        self.n_sprite += 0.15
            
        if self.y_img > altura - 190:
            self.corremais = 0
            self.y_img = altura - 190
            
        if self.n_sprite >= 3:
            self.n_sprite = 0
            
        if self.pula:
            self.corremais = -6
            self.pula = False
        a = 180
        
        self.corremais += 0.30
        self.y_img += self.corremais
        self.image = self.sprite_list[int(self.n_sprite)]
        if self.corremais > 0 and self.angulo > -35:
            self.angulo -= 2
        elif self.corremais < 0 and self.angulo < 35:
            self.angulo += 5
        self.image = py.transform.rotate(self.image, self.angulo)
        py.mask.Mask.clear(self.mask)
        self.mask = py.mask.from_surface(self.image)
        self.rect.topleft = (self.x_img, self.y_img)
        

class Bg(py.sprite.Sprite):
    def __init__(self, dir_img,  x_img, y_img, speed = 1):
        py.sprite.Sprite.__init__(self)
        
        self.dir_img = dir_img
        self.image = py.transform.scale2x(py.image.load(self.dir_img).convert_alpha())
        self.x_img = x_img*self.image.get_width()
        self.y_img = 800 - y_img
        self.speed = speed
        
        
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x_img, self.y_img
    
    
    def update(self): 
        self.x_img -= self.speed
        self.rect.topleft = self.x_img, self.y_img
        if self.x_img <= -self.image.get_width():
             self.x_img = self.image.get_width()
             
             
class Pipe(py.sprite.Sprite):
    def __init__(self, dir_img,  x_img, y_img, speed, rotate=False): 
        
        py.sprite.Sprite.__init__(self)
        
        self.rotate = rotate
        self.dir_img = dir_img
        self.x_img = x_img
        self.y_img = y_img
        self.speed = speed
        
        self.image = py.image.load(self.dir_img).convert_alpha()
        self.image = py.transform.scale(self.image, (self.image.get_width()*1.70, self.image.get_height()*1.70))
        self.rect = self.image.get_rect()
        self.mask = py.mask.from_surface(self.image)
        
        if self.rotate:
            self.image = py.transform.flip(self.image, False, True)
            self.rect.bottomleft = self.x_img, self.y_img
        else:
            self.rect.topleft = self.x_img, self.y_img
              
              
    def update(self): 
        self.x_img -= self.speed
        if self.rotate:
            self.rect.bottomleft = self.x_img, self.y_img
        else:
            self.rect.topleft = self.x_img, self.y_img
            
        if self.x_img <= -self.image.get_width():
            self.x_img = 640


def pipeys():
    y_a = randint(300, 550)
    y_b = y_a - 145
    ys = (y_a, y_b)
    
    return ys
