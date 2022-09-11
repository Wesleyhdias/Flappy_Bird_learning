import pygame as py
import obj
import os
from random import randint
from pygame.locals import * 
from sys import exit

py.init()

color = {'Blue': (0, 0, 255), 'Red': (255, 0, 0), 'Green': (0, 255, 0),
        'White': (255, 255, 255), 'Gray': (100, 100, 100), 'Black': (0, 0, 0)}

defalt_dir = os.path.dirname(__file__)
img_dir = os.path.join(defalt_dir, "img")
bird_sheet = os.path.join(img_dir, 'bird.png')
largura, altura = 500, 800
tela = py.display.set_mode((largura, altura))
py.display.set_caption('Flappy Bird')
fps = py.time.Clock()
pontos = 0

sub_end_txt = obj.Text('Press \'R\' to Restart', 30, color['Black'], bold=True, italic=True)
end_txt = obj.Text('Game Over', 80, color['Black'], bold=True)

while True:
    start = False
    restart = True
    play = True
    pontos = 0
    pipe1 = pipe2 = pipe3 = False
    pipes = []

    all_sprites = py.sprite.Group()
    wall_sprites = py.sprite.Group()

    for c in range(2):
        bg = obj.Bg(os.path.join(img_dir, 'bg.png'), c, 1000)
        all_sprites.add(bg)

    for c in range(3):
        ys = obj.pipeys()
        x = c*245 + 450
        down_pipe = obj.Pipe(os.path.join(img_dir, 'pipe.png'), x, ys[0], 3)
        up_pipe = obj.Pipe(os.path.join(img_dir, 'pipe.png'), x, ys[1], 3, True)
        all_sprites.add(down_pipe)
        all_sprites.add(up_pipe)
        wall_sprites.add(down_pipe)
        wall_sprites.add(up_pipe)
        pipes.append(up_pipe)
    
    for c in range(2):
        piso = obj.Bg(os.path.join(img_dir, 'base.png'), c, 150, 3)
        all_sprites.add(piso)

    bird = obj.Bird(bird_sheet, 200, 300)
    all_sprites.add(bird)
    
    sub_end_txt.escreve_txt(-275, 360, tela)
    end_txt.escreve_txt(650, 280, tela)

    while play:
        
        score = obj.Text(f'PONTOS:{pontos}', 40, color['White'], bold=True, font='consolas')
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
            end_txt.anima_txt_y(35, 280, 35)
            sub_end_txt.anima_txt_y(125, 360, 30)
        else:
            all_sprites.update()        
            
        score.escreve_txt(15, 25, tela)
        
        if (pipes[0].x_img - bird.x_img) < 5 and pipe1 == False:
            pontos += 1
            pipe1 = True
            pipe2 = False
        elif (pipes[1].x_img - bird.x_img) < 5 and pipe2 == False:
            pontos += 1
            pipe2 = True
            pipe3 = False
        elif (pipes[2].x_img - bird.x_img) < 5 and pipe3 == False:
            pontos += 1
            pipe3 = True
            pipe1 = False
        
        if down_pipe.x_img <= -84:
            ys = obj.pipeys()
            down_pipe.y_img = ys[0]
            up_pipe.y_img = ys[1]

        py.display.flip()
    
    if not restart:
        break
