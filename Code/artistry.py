
''' simple drawing using pillow - AR
 '''

from PIL import Image, ImageDraw

def picture() :

    # replace dimensions and background as you see fit
    WIDTH  = 500
    HEIGHT = 500

    DIMENSIONS = [ WIDTH, HEIGHT]

    BACKGROUND_COLOR = "Black"

    # create image of appropriate size
    im = Image.new( 'RGB', DIMENSIONS, BACKGROUND_COLOR )

    # get a drawable canvas of image im
    canvas = ImageDraw.Draw( im )

    # put your drawing commands here

    # water
    x = 0
    y = 250
    w = 500
    h = 250
    xy = [(x, y), (x + w, y + h)]

    canvas.rectangle(xy, fill='MidnightBlue')

    # star 1
    p0 = (25, 25)
    p1 = (20, 35)
    p2 = (30, 35)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='LemonChiFFon')

    p0 = (25, 45)
    p1 = (20, 35)
    p2 = (30, 35)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='LemonChiFFon')

    # star 2
    p0 = (75, 75)
    p1 = (70, 85)
    p2 = (80, 85)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='LemonChiFFon')

    p0 = (75, 95)
    p1 = (70, 85)
    p2 = (80, 85)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='LemonChiFFon')

    # star 3
    p0 = (155, 35)
    p1 = (150, 45)
    p2 = (160, 45)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='LemonChiFFon')

    p0 = (155, 55)
    p1 = (150, 45)
    p2 = (160, 45)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='LemonChiFFon')

    # star 4
    p0 = (250, 60)
    p1 = (245, 70)
    p2 = (255, 70)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='LemonChiFFon')

    p0 = (250, 80)
    p1 = (245, 70)
    p2 = (255, 70)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='LemonChiFFon')

    # star 7
    p0 = (475, 25)
    p1 = (470, 35)
    p2 = (480, 35)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='LemonChiFFon')

    p0 = (475, 45)
    p1 = (470, 35)
    p2 = (480, 35)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='LemonChiFFon')

    # star 6
    p0 = (425, 75)
    p1 = (420, 85)
    p2 = (430, 85)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='LemonChiFFon')

    p0 = (425, 95)
    p1 = (420, 85)
    p2 = (430, 85)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='LemonChiFFon')

    # star 5
    p0 = (345, 35)
    p1 = (340, 45)
    p2 = (350, 45)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='LemonChiFFon')

    p0 = (345, 55)
    p1 = (340, 45)
    p2 = (350, 45)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='LemonChiFFon')

    # star 1 reflection
    p0 = (25, 470)
    p1 = (20, 460)
    p2 = (30, 460)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='LightYellow')

    p0 = (25, 450)
    p1 = (20, 460)
    p2 = (30, 460)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='LightYellow')

    # star 2 reflection
    p0 = (75, 425)
    p1 = (70, 415)
    p2 = (80, 415)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='LightYellow')

    p0 = (75, 405)
    p1 = (70, 415)
    p2 = (80, 415)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='LightYellow')

    # star 3 reflection
    p0 = (155, 455)
    p1 = (150, 465)
    p2 = (160, 465)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='LightYellow')

    p0 = (155, 475)
    p1 = (150, 465)
    p2 = (160, 465)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='LightYellow')

    # star 4 reflection
    p0 = (250, 440)
    p1 = (245, 430)
    p2 = (255, 430)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='LightYellow')

    p0 = (250, 420)
    p1 = (245, 430)
    p2 = (255, 430)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='LightYellow')

    # star 7 reflection
    p0 = (475, 475)
    p1 = (470, 465)
    p2 = (480, 465)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='LightYellow')

    p0 = (475, 455)
    p1 = (470, 465)
    p2 = (480, 465)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='LightYellow')

    # star 6 reflection
    p0 = (425, 425)
    p1 = (420, 415)
    p2 = (430, 415)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='LightYellow')

    p0 = (425, 405)
    p1 = (420, 415)
    p2 = (430, 415)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='LightYellow')

    # star 5 reflection
    p0 = (345, 465)
    p1 = (340, 455)
    p2 = (350, 455)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='LightYellow')

    p0 = (345, 445)
    p1 = (340, 455)
    p2 = (350, 455)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='LightYellow')

    # moon
    x = 200
    y = 100
    w = 100
    h = 100
    xy = [(x, y), (x + w, y + h)]

    canvas.ellipse(xy, fill='Ivory')

    # moon reflection
    x = 205
    y = 300
    w = 95
    h = 95
    xy = [(x, y), (x + w, y + h)]

    canvas.ellipse(xy, fill='FloralWhite')

    # mountain 3
    p0 = (185, 120)
    p1 = (120, 250)
    p2 = (250, 250)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='Grey', outline='Black')

    # snow cap 3
    p0 = (185, 120)
    p1 = (163, 165)
    p2 = (206, 165)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='White')

    # mountain 1
    p0 = (50, 100)
    p1 = (0, 250)
    p2 = (100, 250)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='Grey', outline='Black')

    # snow cap 1
    p0 = (50, 100)
    p1 = (35, 150)
    p2 = (65, 150)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='White')

    # mountain 2
    p0 = (115, 50)
    p1 = (50, 250)
    p2 = (180, 250)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='Grey', outline='Black')

    # snow cap 2
    p0 = (115, 50)
    p1 = (95, 115)
    p2 = (135, 115)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='White')

    # mountain 4
    p0 = (315, 120)
    p1 = (250, 250)
    p2 = (380, 250)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='Grey', outline='Black')

    # snow cap 4
    p0 = (315, 120)
    p1 = (293, 165)
    p2 = (336, 165)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='White')

    # mountain 6
    p0 = (450, 100)
    p1 = (400, 250)
    p2 = (500, 250)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='Grey', outline='Black')

    # snow cap 6
    p0 = (450, 100)
    p1 = (435, 150)
    p2 = (465, 150)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='White')

    # mountain 5
    p0 = (385, 50)
    p1 = (320, 250)
    p2 = (450, 250)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='Grey', outline='Black')

    # snow cap 5
    p0 = (385, 50)
    p1 = (365, 115)
    p2 = (405, 115)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='White')




    # mountain 3 reflection
    p0 = (185, 380)
    p1 = (120, 250)
    p2 = (250, 250)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='DarkGrey', outline='MidnightBlue')

    # snow cap 3 reflection
    p0 = (185, 380)
    p1 = (163, 335)
    p2 = (206, 335)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='Snow')

    # mountain 1 reflection
    p0 = (50, 400)
    p1 = (0, 250)
    p2 = (100, 250)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='DarkGrey', outline='MidnightBlue')

    # snow cap 1 reflection
    p0 = (50, 400)
    p1 = (35, 350)
    p2 = (65, 350)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='Snow')

    # mountain 2 reflection
    p0 = (115, 450)
    p1 = (50, 250)
    p2 = (180, 250)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='DarkGrey', outline='MidnightBlue')

    # snow cap 2 reflection
    p0 = (115, 450)
    p1 = (93, 380)
    p2 = (137, 380)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='Snow')

    # mountain 4 reflection
    p0 = (315, 380)
    p1 = (250, 250)
    p2 = (380, 250)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='DarkGrey', outline='MidnightBlue')

    # snow cap 4 reflection
    p0 = (315, 380)
    p1 = (293, 335)
    p2 = (336, 335)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='Snow')

    # mountain 6 reflection
    p0 = (450, 400)
    p1 = (400, 250)
    p2 = (500, 250)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='DarkGrey', outline='MidnightBlue')

    # snow cap 6 reflection
    p0 = (450, 400)
    p1 = (435, 350)
    p2 = (465, 350)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='Snow')

    # mountain 5 reflection
    p0 = (385, 450)
    p1 = (320, 250)
    p2 = (450, 250)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='DarkGrey', outline='MidnightBlue')

    # snow cap 5 reflection
    p0 = (385, 450)
    p1 = (363, 380)
    p2 = (407, 380)
    seq = [p0, p1, p2]

    canvas.polygon(seq, fill='Snow')


    # return the art
    return im

# no changes to the below
# -----------------------

if ( __name__ == "__main__" ) :

    im = picture()

    im.show()

    im.save( 'my-artistry.jpg' )
