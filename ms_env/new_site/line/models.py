from django.db import models

class Video(models.Model):
	name = models.CharField(max_length=150, db_index=True, verbose_name='Name')
	slug = models.SlugField(max_length=150, unique=True)
		
	def download():
		images = []
		font_size = 50
		var = 'Hello World!'
		x = 100

		base = Image.new(mode='RGBA', size=(100, 100), color=(0, 0, 50, 255))  # create background layer
		fnt = ImageFont.truetype(r'/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf', font_size)

		while len(images) * 30 < 3000:  # make sure that the file is less than 3s
			txt = Image.new('RGBA', base.size, (255, 255, 255, 0))
			d = ImageDraw.Draw(txt)
			d.text((x, 20), var, font=fnt, fill=(255, 255, 255, 255))  # re-draw text at (x,20) coords
			out = Image.alpha_composite(base, txt)  # connect background and text
			images.append(out)
			x -= (1 + len(var) * 0.3)  # shift text by x pixels (x increases with string's length)

		images[0].save(
			'video.gif',
			save_all=True,
			append_images=images[1:],  # split that skips the first frame
			optimize=True,
			duration=30,
			oprimize = True,
			loop = 0
		)

		file = open("video.gif", "r+b")
		response = FileResponse(file, content_type='gif')
		response['Content-Disposition'] = 'attachment; filename=my_video.gif'

		return response
