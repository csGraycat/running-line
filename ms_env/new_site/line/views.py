from django.http import HttpResponse
from PIL import Image, ImageFont, ImageDraw
from django.http import FileResponse
import sqlite3

def index(request):
	return HttpResponse("Enter your text into address bar")
	
def save_request(request, text):
	sqlite_connection = sqlite3.connect('db.sqlite3')
	cursor = sqlite_connection.cursor()
	sqlite_insert_with_param = """INSERT INTO requests
		(method, text)
		VALUES (?, ?);"""
	
	data_tuple = (request.method, text)
	cursor.execute(sqlite_insert_with_param, data_tuple)
	sqlite_connection.commit()
	cursor.close()
		
def video(request, text):

	save_request(request, text)	
	
	images = []
	font_size = 50
	var = text
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


