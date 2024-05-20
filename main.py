from PIL import Image, ImageFont, ImageDraw

if __name__ == '__main__':
    images = []
    font_size = 50
    var = 'Hello World!'
    x = 100

    base = Image.new(mode='RGBA', size=(100, 100), color=(0, 0, 0, 255))  # create background layer
    fnt = ImageFont.truetype('calibri.ttf', font_size)

    while len(images) * 30 < 3000:  # make sure that the file is less than 3s
        txt = Image.new('RGBA', base.size, (255, 255, 255, 0))
        d = ImageDraw.Draw(txt)
        d.text((x, 30), var, font=fnt, fill=(255, 255, 255, 255))  # re-draw text at (x,30) coords
        out = Image.alpha_composite(base, txt)  # connect background and text
        images.append(out)
        x -= (1 + len(var) * 0.3)  # shift x by several pixels (x increases with string's length)

    images[0].save(
        'video.gif',
        save_all=True,
        append_images=images[1:],  # split that skips the first frame
        optimize=True,
        duration=30,
        loop=0
    )



