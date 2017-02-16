from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    dx = x1 - x0
    dy = y1 - y0
    if abs(dx) > abs(dy):
        if dx > 0:
            if dy > 0:
                draw_line1( x0, y0, x1, y1, screen, color )
            else:
                draw_line8( x0, y0, x1, y1, screen, color )
        else:
            if dy > 0:
                draw_line4( x0, y0, x1, y1, screen, color )
            else:
                draw_line5( x0, y0, x1, y1, screen, color )
    if abs(dy) > abs(dx):
        if dx > 0:
            if dy > 0:
                draw_line2( x0, y0, x1, y1, screen, color )
            else:
                draw_line7( x0, y0, x1, y1, screen, color )
        else:
            if dy > 0:
                draw_line3( x0, y0, x1, y1, screen, color )
            else:
                draw_line6( x0, y0, x1, y1, screen, color )
                
#helpers:
#octant 1
def draw_line1( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    A = y1-y
    B = x-x1
    d = 2*A + B
    while (x < x1):
        plot(screen, color, x, y)
        if d > 0:
            y = y+1
            d = d + 2*B
        x = x + 1
        d = d + 2*A

#octant 2
def draw_line2( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    A = y1-y
    B = x-x1
    d = A + 2*B
    while (y < y1):
        plot(screen, color, x, y)
        if d < 0:
            x = x+1
            d = d + 2*A
        y = y + 1
        d = d + 2*B

#octant 3
def draw_line3( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    A = y1-y
    B = x-x1
    d = A + 2*B
    while (y < y1):
        plot(screen, color, x, y)
        if d < 0:
            x = x-1
            d = d + 2*A
        y = y + 1
        d = d - 2*B

#octant 4
def draw_line4( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    A = y1-y
    B = x-x1
    d = 2*A + B
    while (x > x1):
        plot(screen, color, x, y)
        if d > 0:
            y = y+1
            d = d - 2*B
        x = x - 1
        d = d + 2*A

#octant 5
def draw_line5( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    A = y1-y
    B = x-x1
    d = 2*A - B
    while (x > x1):
        plot(screen, color, x, y)
        if d < 0:
            y = y-1
            d = d + 2*B
        x = x - 1
        d = d + 2*A

#octant 6
def draw_line6( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    A = y1-y
    B = x-x1
    d = A - 2*B
    while (y > y1):
        plot(screen, color, x, y)
        if d > 0:
            x = x-1
            d = d + 2*A
        y = y - 1
        d = d + 2*B

#octant 7
def draw_line7( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    A = y1-y
    B = x-x1
    d = A - 2*B
    while (y > y1):
        plot(screen, color, x, y)
        if d > 0:
            x = x+1
            d = d + 2*A
        y = y - 1
        d = d - 2*B

#octant 8
def draw_line8( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    A = y1-y
    B = x-x1
    d = 2*A - B
    while (x < x1):
        plot(screen, color, x, y)
        if d < 0:
            y = y-1
            d = d - 2*B
        x = x + 1
        d = d + 2*A


