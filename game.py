import pygame as pg


pg.init()

screen_width = 800
screen_height = 600

display = pg.display.set_mode((screen_width,screen_height))

pg.display.set_caption('Space invaders')
icon_img = pg.image.load('resources/img/ufo.png')
pg.display.set_icon(icon_img)

background_img = pg.image.load('resources/img/background.png')
display.blit(background_img, (0,0))

sysfont = pg.font.SysFont('arial',50)
text_img = sysfont.render('Heinko',True,'red')
#display.blit(Heinko_img,(400,300))
#font = pg.font.Font('resources/font/648_19__.TTF',48)
w = text_img.get_width()
h = text_img.get_height()
x = 0
y = screen_height-h



running = True

while running:
    #display.fill('blue',(20, 50, 100, 250))
    display.blit(text_img,(x,y))
    pg.display.update()

    for event in pg.event.get():
        if event.type==pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            running = False

        if event.type == pg.KEYUP and event.key == pg.K_m:

            print('Press m')
            display.blit(text_img,(x,y))


pg.quit()







pg.quit()