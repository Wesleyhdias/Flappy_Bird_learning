# lugar para testar mudanças no programa principal sem fazer merda!!
import pygame as py
import obj
import os
from random import randint
from pygame.locals import * 
from sys import exit

py.init()

defalt_dir = os.path.dirname(__file__)
img_dir = os.path.join(defalt_dir, "img")
bird_sheet = os.path.join(img_dir, 'bird.png')
par_pipes = []

largura, altura = 500, 800
tela = py.display.set_mode((largura, altura))

for c in range(3):
    ys = obj.pipeys()
    x = c*245 + 450
    down_pipe = obj.Pipe(os.path.join(img_dir, 'pipe.png'), x, ys[0], 3)
    up_pipe = obj.Pipe(os.path.join(img_dir, 'pipe.png'), x, ys[1], 3, True)
    par_pipes.append(down_pipe)
    par_pipes.append(up_pipe)
    
print(par_pipes[2].x_img)
