import pygame as py
import obj
import os
from random import randint
from pygame.locals import * 
from sys import exit

py.init()

color = {'Blue': (0, 0, 255), 'Red': (255, 0, 0), 'Green': (0, 255, 0),
        'White': (255, 255, 255), 'Gray': (100, 100, 100)}

defalt_dir = os.path.dirname(__file__)
img_dir = os.path.join(defalt_dir, "img")
bird_sheet = os.path.join(img_dir, 'bird.png')
largura, altura = 500, 800
tela = py.display.set_mode((largura, altura))
py.display.set_caption('Flappy Bird')
fps = py.time.Clock()

while True:
    start = False
    restart = True
    play = True

    all_sprites = py.sprite.Group()
    wall_sprites = py.sprite.Group()

    for c in range(2):
        bg = obj.Bg(os.path.join(img_dir, 'bg.png'), c, 1000, 1)
        all_sprites.add(bg)

    for c in range(3):
        ys = obj.pipeys()
        x = c*245 + 450
        pipe = obj.Pipe(os.path.join(img_dir, 'pipe.png'), x, ys[0], 3)
        pipe1 = obj.Pipe(os.path.join(img_dir, 'pipe.png'), x, ys[1], 3, True)
        all_sprites.add(pipe)
        all_sprites.add(pipe1)
        wall_sprites.add(pipe)
        wall_sprites.add(pipe1)

    for c in range(2):
        piso = obj.Bg(os.path.join(img_dir, 'base.png'), c, 150, 3)
        all_sprites.add(piso)

    bird = obj.Bird(bird_sheet, 200, 300)
    all_sprites.add(bird)

    while play:
        
        tela.fill(color['Gray'])
        fps.tick(60)
        
        for event in py.event.get():
            if event.type == QUIT:
                py.quit()
                exit()
            if event.type == KEYDOWN:
                start = True
                if event.key == K_SPACE:
                    bird.jump()
                if event.key == K_r:
                    play = False
                if event.key == K_ESCAPE:
                    restart = False

        colide = py.sprite.spritecollide(bird, wall_sprites, False, py.sprite.collide_mask)
        
        all_sprites.draw(tela)
        if not restart:
            break
        elif not start:
            pass
        elif colide or bird.y_img > altura - 210:
            pass 
        else:
            all_sprites.update()
        
        if pipe.x_img <= -84:
            ys = obj.pipeys()
            pipe.y_img = ys[0]
            pipe1.y_img = ys[1]

        py.display.flip()
    
    if not restart:
        break
