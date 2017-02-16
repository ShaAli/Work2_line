from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

draw_line1(250,250,450,350, screen, color)

draw_line2(250,250,350,450, screen, [255, 0, 0])

draw_line3(250,250,150,450, screen, [0, 0, 255])

draw_line4(250,250,50,350, screen, [255, 255, 0])

draw_line5(250,250,50,150, screen, [255, 0, 255])

draw_line6(250,250,150,50, screen, [0, 255, 255])

draw_line7(250,250,350,50, screen, [100, 100, 100])

draw_line8(250,250,450,150, screen, [255, 255, 255])


display(screen)
save_extension(screen, 'img.png')
